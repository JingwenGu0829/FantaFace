from utils import send_request,handle_result,return_queue
import cv2,queue
from io import BytesIO
from PIL import Image
from option import args 
from os import remove
import time,threading
from multiprocessing import Process
import win32clipboard 
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

def process_image(frame,copy_to_clipboard=False,show_img=False):
    """
    This should be called by the web backend with an np-array-like image to detect features.
    The function should be called with try-except because face++ sometimes denies the request
    and returns {"error_message":"CONCURRENCY_LIMIT_EXCEEDED"}
    @param img(numpy.array):        image from backend
    @param copy_to_clipboard(bool): copy detection-generator/animation.jpg to clipboard
    @param show_img(bool):          Set to True to show the detection results using cv2.imshow()
    """
    
    cv2.imwrite('frame.jpg',frame)
    face_dict,gesture_dict=onlineDetec(frame)
    remove('frame.jpg')    
    handle_result(frame,face_dict,gesture_dict,show_img)
    #Use the same image name in processing
    if copy_to_clipboard:
        path='detection-generator/animation.jpg'
        image=Image.open(path)
        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

def process_video(path=None,dynam_wallpaper=False,show_img=False):   
    result_index=1
    print(show_img)
    if path:
        cap = cv2.VideoCapture(path)
    else:
        cap = cv2.VideoCapture(0)

    #Detect 2 frames per second(excluding the request latency)
    frame_per_sec=1
    sum = 0
    camera_fps=cap.get(cv2.CAP_PROP_FPS)
    face_dict=gesture_dict=None
    while True:
        
        ret, frame = cap.read()
        if ret == False:
            print('Unable to read video')
            break
        sum += 1
        if sum % (camera_fps//frame_per_sec) == 0:
            sum = 0
            print('sleep for 0.3s')
            time.sleep(0.3)
            if args.approach == 'Online_request':
                t1=time.time()
                cv2.imwrite('frame.jpg',img=frame)
                face_dict,gesture_dict=onlineDetec(frame)
                remove('frame.jpg')       
                handle_result(frame,face_dict,gesture_dict,result_index,show_img)
                result_index+=1
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
                   
                handle_result(frame,face_dict,gesture_dict,result_index=result_index,show_img=show_img)
                result_index+=1
                print("time used :",time.time()-t1)


if __name__ == '__main__':
    process_video(path=r'C:\Users\19051\Documents\WeChat Files\wxid_lzx03zypbnw212\FileStorage\Video\2022-08\9f7d834fdd725540c10a5b00f1d86d42.mp4',show_img=False)
    # test latency
    # total_time=0
    # iters=15
    # retry=10
    # for i in range(iters):
    #     t1=time.time()
    #     process_image(cv2.imread('detection-generator/test.jpg'),copy_to_clipboard=True,show_img=False)
    #     time_used=time.time()-t1
    #     print("time_used:",time_used)
    #     total_time+=time_used
    #     time.sleep(0.8)
    # print("-----------------------------\n",f"Average time across {iters} detections:  ",total_time/iters,' sec')
