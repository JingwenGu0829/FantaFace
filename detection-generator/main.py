import json

import cv2,requests
from option import args
import requests
import urllib
import time
def send_face_req(url, key, secret, frame):
    t1=time.time()
    filepath = r"C:\Users\19051\Desktop\前端\face.jpg"

    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('1')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append(
        "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
    data.append('--%s--\r\n' % boundary)

    for i, d in enumerate(data):
        if isinstance(d, str):
            data[i] = d.encode('utf-8')

    http_body = b'\r\n'.join(data)

    # build http request
    req = urllib.request.Request(url=url, data=http_body)

    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    try:
        # post data to server
        resp = urllib.request.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        # if you want to load as json, you should decode first,
        content=qrcont.decode('utf-8')
        print(content)
        print('time used:',time.time()-t1,)
        return content
    except urllib.error.HTTPError as e:
        print(e.read().decode('utf-8'))


def onlineMain(pic):
    result=send_face_req(url="https://api-cn.faceplusplus.com/facepp/v3/detect",key="5HpZxtRruayZt2kF_80S-CsCxkZ_vZPX",secret="YJJIsdx5ROChxAYsP2bCmhskAxQC5ekz",frame=pic)
    pass

def offlineMain(pic):
    # To be implemented
    pass


def main():
    # 1 detection/stride*frames
    stride = 30
    if args.input=='video':
        cap = cv2.VideoCapture(args.inputDir+'demo.mp3')
    elif args.input=='camera':
        cap = cv2.VideoCapture(0)
    else:
        raise Exception('Input argument invalid: please input video or camera')
    sum=0
    while True:

        ret,img=cap.read()
        if ret=='False':
            raise Exception('Unable to use camera')
        sum+=1
        if sum%stride==0:
            sum=0
            if args.approach=='Online_request':
                onlineMain(img)
            elif args.approach=='Offline_request':
                offlineMain(img)

        
            
    # cap.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

    
