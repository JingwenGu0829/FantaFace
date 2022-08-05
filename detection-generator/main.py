import json
from unicodedata import name
from utils import send_req,show_res
import cv2
from option import args
import requests
# import urllib
import time


def onlineDetec(frame):
    face_params=[("return_landmark",2),('return_attributes',\
    "gender,age,smiling,headpose,eyestatus,emotion,mouthstatus,eyegaze")]
    face=send_req('https://api-cn.faceplusplus.com/facepp/v3/detect','5HpZxtRruayZt2kF_80S-CsCxkZ_vZPX',\
                    'YJJIsdx5ROChxAYsP2bCmhskAxQC5ekz',frame,face_params)
    gesture_params=[("return_gestrue",1)]
    gesture=send_req('https://api-cn.faceplusplus.com/humanbodypp/v1/gesture','AKthm2U503hXINwtzjQ68uRj_MeLnbae',\
                    'J1Q2D9pB44I6HdzdcwTnLUjC4qz2MEgT',frame,gesture_params)
    return face,gesture

def offlineDetec(frame):
    # To be implemented
    raise NotImplementedError('别骂了，我们没时间训模型')


def main():
    # 1 detection/stride*frames
    stride = 30;face=gesture=None
    if args.input == 'video':
        cap = cv2.VideoCapture(args.inputDir + 'demo.mp3')
    elif args.input == 'camera':
        cap = cv2.VideoCapture(0)
    else:
        raise Exception('Input argument invalid: please input video or camera')
    sum = 0
    while True:
        
        ret, frame = cap.read()
        if ret == 'False':
            raise Exception('Unable to use camera')
        sum += 1
        if sum % stride == 0:
            sum = 0
            if args.approach == 'Online_request':
                t1=time.time()
                face,gesture=onlineDetec(frame)
                # show the resulting image with landmarks
                show_res(frame,face,gesture)
                print("time used :",time.time()-t1)
            elif args.approach == 'Offline_request':
                face,gesture=offlineDetec(fra)
                



if __name__ == '__main__':
    main()
