import json
from unicodedata import name
from utils import send_request,decode_result
import cv2
from option import args
import requests
# import urllib
import time


def onlineDetec(frame,test_with_img=False):
    face_params=[("return_landmark","2"),('return_attributes',\
    "headpose,eyestatus,emotion,mouthstatus,eyegaze")]
    face=send_request('https://api-cn.faceplusplus.com/facepp/v3/detect','5HpZxtRruayZt2kF_80S-CsCxkZ_vZPX',\
                    'YJJIsdx5ROChxAYsP2bCmhskAxQC5ekz',frame,face_params)
    gesture_params=[("return_gestrue","1")]
    gesture=send_request('https://api-cn.faceplusplus.com/humanbodypp/v1/gesture','AKthm2U503hXINwtzjQ68uRj_MeLnbae',\
                    'J1Q2D9pB44I6HdzdcwTnLUjC4qz2MEgT',frame,gesture_params)
    return face,gesture

def offlineDetec(frame):
    # To be implemented
    raise NotImplementedError('别骂了，我们没时间训模型')


def main():    
    if args.input == 'video':
        cap = cv2.VideoCapture(args.inputDir + 'demo.mp3')
    elif args.input == 'camera':
        cap = cv2.VideoCapture(0)
    else:
        raise Exception('Input argument invalid: please input video or camera')
    sum = 0
    #Detect 2 frames per second(excluding the request latency)
    frame_per_sec=2
    camera_fps=cap.get(cv2.CAP_PROP_FPS)
    face_res=gesture=None
    #
    while True:
        
        ret, frame = cap.read()
        if ret == 'False':
            raise Exception('Unable to use camera')
        sum += 1
        if sum % (camera_fps/frame_per_sec) == 0:
            sum = 0
            if args.approach == 'Online_request':
                t1=time.time()
                face_dict,gesture_dict=onlineDetec(frame)
                
                if face_dict['face_num']==0:
                    face_dict=0
                elif face_dict['face_num']>1:
                    face_dict=-1
                else:
                    face_dict=face_dict['faces'][0]
                # show the resulting image with landmarks
                if len(gesture_dict['hands'])==0:
                    gesture_dict=0
                else:
                    gesture_dict=gesture_dict['hands'][0]
                    
                decode_result(frame,face_dict,gesture_dict)
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
                    
                json_data=decode_result(frame,face_dict,gesture_dict)
                print("time used :",time.time()-t1)



if __name__ == '__main__':
    main()
