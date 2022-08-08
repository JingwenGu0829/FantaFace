from utils import send_request,parse_result,return_queue
import cv2,queue
from option import args 
from os import remove
import time,threading
from multiprocessing import Process

def onlineDetec(frame):
    """
    @ param test_with_img: Image file path. If not empty, this method will will only detect this image instead of frame.
    """
    face_params=[("return_landmark","2"),('return_attributes',\
    "headpose,eyestatus,emotion,mouthstatus,eyegaze")]
    gesture_params=[("return_gestrue","1")]
    #use multi-threading when sending requests
    t1=threading.Thread(target=send_request,args=['https://api-cn.faceplusplus.com/facepp/v3/detect',
                        '5HpZxtRruayZt2kF_80S-CsCxkZ_vZPX',
                        'YJJIsdx5ROChxAYsP2bCmhskAxQC5ekz',frame,face_params])  
    t2=threading.Thread(target=send_request,args=['https://api-cn.faceplusplus.com/humanbodypp/v1/gesture',
                        'AKthm2U503hXINwtzjQ68uRj_MeLnbae',\
                        'J1Q2D9pB44I6HdzdcwTnLUjC4qz2MEgT',frame,gesture_params])
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    #this return order changes from time to time,probably because the functions run and put values in queue simultaneously
    data1=return_queue.get()
    data2=return_queue.get()
    if 'faces' in data1.keys():
        face=data1
        gesture=data2
    else:
        face=data2
        gesture=data1
    return face,gesture

def offlineDetec(frame):
    # To be implemented
    raise NotImplementedError('别骂了，我们没时间训模型')

def process_image(frame,copy_to_clipboard=True):
    """
    This should be called by the web backend with an np-array-like image to detect features.
    The function should be called with try-except because face++ sometimes denies the request
    and returns {"error_message":"CONCURRENCY_LIMIT_EXCEEDED"}
    @param img(numpy.array): image from backend
    @print_time(boolean): print the time consumed by the whole detection pipeline in the terminal.
    """
    cv2.imwrite('frame.jpg',frame)
    face_dict,gesture_dict=onlineDetec(frame)
    remove('frame.jpg')    
    parse_result(frame,face_dict,gesture_dict,args.show_img)
    #Use the same image name in processing
    if copy_to_clipboard:
        animation=cv2.imread('animation.jpg')
        
def process_video(frame,dynam_wallpaper=False):
    pass

def main():   
    """
    The main fuction is for testing using your local camera or video
    """ 
    print('Main function running------------------')
    if args.input == 'video':
        cap = cv2.VideoCapture(args.inputDir + 'demo.mp3')
    elif args.input == 'camera':
        cap = cv2.VideoCapture(0)
    else:
        raise Exception('Input argument invalid: please input video or camera')


    #Detect 2 frames per second(excluding the request latency)
    frame_per_sec=4
    sum = 0
    camera_fps=cap.get(cv2.CAP_PROP_FPS)
    face_dict=gesture_dict=None
    while True:
        ret, frame = cap.read()
        if ret == False:
            raise Exception('Unable to use camera')
        sum += 1
        if sum % (camera_fps/frame_per_sec) == 0:
            sum = 0

            if args.approach == 'Online_request':
                t1=time.time()
                cv2.imwrite('frame.jpg',img=frame)
                face_dict,gesture_dict=onlineDetec(frame)
                remove('frame.jpg')       
                parse_result(frame,face_dict,gesture_dict,show_img=args.show_img)
                print("time used :",time.time()-t1)


                #Do not use this branch!!!!
            elif args.approach == 'Offline_request':
                t1=time.time()
                face_res,gesture=offlineDetec(frame)
                face_dict,gesture_dict=onlineDetec(frame)
                
                if face_dict['face_num']==0:
                    face_dict=0
                elif face_dict['face_num']>1:
                    face_dict=-1
                # show the resulting image with landmarks
                if len(gesture_dict['hands'])==0:
                    gesture_dict=0
                    #debugging gesture detection
                   
                parse_result(frame,face_dict,gesture_dict,show_img=args.show_img)
                print("time used :",time.time()-t1)


if __name__ == '__main__':
    # main()

    # test latency
    total_time=0
    iters=15
    retry=10
    for i in range(iters):
        t1=time.time()
        process_image(cv2.imread('test.jpg'))
        time_used=time.time()-t1
        print("time_used:",time_used)
        total_time+=time_used
        time.sleep(0.8)
    print("-----------------------------\n",f"Average time across {iters} detections:  ",total_time/iters,' sec')
