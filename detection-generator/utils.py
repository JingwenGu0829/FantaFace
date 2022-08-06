import json
from operator import ge
import cv2
from time import time
from urllib import request,error
def send_request(url, key, secret, frame,params,test_with_img=False):
    """
    Send request to Face++ server and return detection results.

    """
    boundary = '----------%s' % hex(int(time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    # The server only accepts bytes!!!!!
    if test_with_img :
        fr = open(test_with_img, 'rb')
    else:
        #To do: Find a method to align the format of np-array image and with that of the binary image read from open().
        #frame.to_bytes() does not work!
        cv2.imwrite('frame.jpg',frame)
        fr = open('frame.jpg', 'rb')
    data.append(fr.read())
    fr.close()
    # Optional params
    for name, value in params:
        data.append('--%s'%boundary)
        data.append('Content-Disposition: form-data; name="%s"\r\n' % name)
        data.append(value)
    data.append('--%s--\r\n' % boundary)
    for i, d in enumerate(data):
        if isinstance(d, str):
            data[i] = d.encode('utf-8')
    
    http_body = b'\r\n'.join(data)
    # build http request
    req = request.Request(url=url, data=http_body)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    try:
        # post data to server
        resp = request.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        # if you want to load as json, you should decode first,
        content = qrcont.decode('utf-8')
        content=json.loads(content)
        return content
    except error.HTTPError as e:
        print(e.read().decode('utf-8'))
def decode_result(frame,face_data,gesture_data,show=False):

    """
    This function demonstrates detection results using opencv (specified by the parameter "show"), encode
    all potentially useful attributes into JSON and send it to OSC for drawing animations .
    Output to the server:
    Face_data=-1:more than one face;   =0:no face;
    gesture_data=0: no hand
    Else: return dictionaries of labels and landmarks.
    """
    color=(255,0,0)
    fontface=cv2.FONT_HERSHEY_COMPLEX
    #face_data:landmark,attributes,face_rectangle,face_token
    if face_data:
        attribs=face_data['attributes']
        landmark=face_data['landmark']
        #Both x and y for one value in l_eye
        #Extract useful features from returned landmarks and labels, as specified by tuples of keys ()
        l_eye={key:landmark[key] for key in ("left_eye_top","left_eye_bottom","left_eye_left_corner","left_eye_right_corner")}
        r_eye={key:landmark[key] for key in ("right_eye_top","right_eye_bottom","right_eye_left_corner","right_eye_right_corner")}
        lip={key:landmark[key] for key in ("mouth_upper_lip_top","mouth_lower_lip_bottom","mouth_left_corner","mouth_right_corner")}
        #Not sure which features are useful yet
        l_eye_status=attribs['eyestatus']['left_eye_status']
        r_eye_status=attribs['eyestatus']['right_eye_status']
        mouthstatus=attribs['mouthstatus']
        emotion=attribs['emotion']

        #get key for max value
        if show:
            # for data in (l_eye,r_eye,lip):
        #     for value in data.values():
        #         x,y=value['x'],value['y']
        #         cv2.circle(frame,center=(x,y),radius=0,color=color,thickness=8)
            for point in landmark.values():
                x,y=point['x'],point['y']
                cv2.circle(frame,center=(x,y),radius=0,color=color,thickness=8)
            #y,x is the correct order    
            y,x,w,h=list(face_data['face_rectangle'].values())
            emotion=max(zip(emotion.values(),emotion.keys()))[1]
            l_eyestatus=max(zip(l_eye_status.values(),l_eye_status.keys()))[1]
            r_eyestatus=max(zip(r_eye_status.values(),r_eye_status.keys()))[1]
            mouthstatus=max(zip(mouthstatus.values(),mouthstatus.keys()))[1]
            #draw features
            cv2.rectangle(frame,(x,y),(x+w,y+h),thickness=2,color=color)
            cv2.putText(frame,text=emotion,org=(x+w,int(y+h/2)),fontScale=1,color=color,fontFace=fontface)
            cv2.putText(frame,l_eyestatus,tuple(l_eye['left_eye_top'].values()),fontScale=0.7,color=color,fontFace=fontface)
            cv2.putText(frame,r_eyestatus,tuple(r_eye['right_eye_top'].values()),fontScale=0.7,color=color,fontFace=fontface)
            cv2.putText(frame,mouthstatus,tuple(lip['mouth_lower_lip_bottom'].values()),fontScale=0.7,color=color,fontFace=fontface)
            cv2.imshow('寄',frame)
            cv2.waitKey(0)
        face_data={'attribs':attribs,'l_eye':l_eye,'r_eye':r_eye,'lip':lip,\
                   'l_eye_status':l_eye_status,'r_eye_status':r_eye_status,'mouthstatus':mouthstatus,\
                    'emotion':emotion,'eyegaze':attribs['eyegaze']
                    }
    if gesture_data:
        gesture_data=gesture_data['hands'][0]
    data={'face_data':face_data,'gesture_data':gesture_data}
    from pythonosc.udp_client import SimpleUDPClient
    from json import dump
    ip = "127.0.0.1"
    port = 1337

    client = SimpleUDPClient(ip, port)  # Create client

    client.send_message("/some/address", json.dump(data))  
