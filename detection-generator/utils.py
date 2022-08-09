import json
from operator import ge
from option import args
import os,queue
import cv2,math
from time import time
from urllib import request,error
#store return values from send_request()
return_queue=queue.Queue()
def send_request(url, key, secret, frame,params):
    """
    Send request to Face++ server and return detection results.

    """
    print("send request")
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
    #To do: Find a method to align the format of np-array image and with that of the binary image read from open().
    #frame.to_bytes() does not work!
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
        return_queue.put(content)

    except error.HTTPError as e:
        print(e.read().decode('utf-8'))


        
def handle_result(frame,face_data,gesture_data,result_index=None,show_img=False):

    """
    This function demonstrates detection results using opencv (specified by the parameter "show"), encode
    all  useful attributes into JSON and pass them to Processing for drawing animations .
    @Output :
    Face_data=-1:more than one face;   =0:no face;
    gesture_data=0: no hand
    else: return dictionaries of labels and landmarks.
    """
    if face_data['face_num']==0:
        face_data=0
    elif face_data['face_num']>1:
        face_data=-1
    else:
        face_data=face_data['faces'][0]
    # show the resulting image with landmarks
    if len(gesture_data['hands'])==0:
        gesture_data=0
    else:
        gesture_data=gesture_data['hands'][0]

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
            emotion=attribs['emotion']
            mouthstatus=attribs['mouthstatus']
            eye_gaze=[attribs['eyegaze']['left_eye_gaze']['vector_x_component'],attribs['eyegaze']['left_eye_gaze']['vector_y_component']]
            eye_gaze=math.atan2(-eye_gaze[1],eye_gaze[0])
            mouthstatus.pop('surgical_mask_or_respirator');mouthstatus.pop('other_occlusion')
            r_eye_status.pop('dark_glasses');r_eye_status.pop('occlusion')
            l_eye_status.pop('dark_glasses');l_eye_status.pop('occlusion')

             #y,x,w,h is the correct order    
            y,x,w,h=list(face_data['face_rectangle'].values())
            #get keys for max values
            emotion=max(zip(emotion.values(),emotion.keys()))[1]
            l_eyestatus=max(zip(l_eye_status.values(),l_eye_status.keys()))[1]
            r_eyestatus=max(zip(r_eye_status.values(),r_eye_status.keys()))[1]
            if "open" in l_eyestatus:
                l_eye_status='open'
            else:
                l_eye_status='close'
            if "open" in r_eyestatus:
                r_eye_status='open'
            else:
                r_eye_status='close'
            mouthstatus=max(zip(mouthstatus.values(),mouthstatus.keys()))[1]
    if gesture_data:
        gesture_data=gesture_data['hands'][0]
    if show_img:
        color=(255,0,0)
        fontface=cv2.FONT_HERSHEY_COMPLEX
        #face_data:landmark,attributes,face_rectangle,face_token
        
            
            # for data in (l_eye,r_eye,lip):
        #     for value in data.values():
        #         x,y=value['x'],value['y']
        #         cv2.circle(frame,center=(x,y),radius=0,color=color,thickness=8)
        if face_data:
        #     for point in landmark.values():
        #         x,y=point['x'],point['y']
        #         cv2.circle(frame,center=(x,y),radius=0,color=color,thickness=4)
           
            #draw features
            cv2.rectangle(frame,(x,y),(x+w,y+h),thickness=2,color=color)
            cv2.putText(frame,text=emotion,org=(x+w,int(y+h/2)),fontScale=1,color=color,fontFace=fontface)
            cv2.putText(frame,l_eyestatus,tuple(l_eye['left_eye_top'].values()),fontScale=0.6,color=color,fontFace=fontface)
            cv2.putText(frame,r_eyestatus,tuple(r_eye['right_eye_top'].values()),fontScale=0.6,color=color,fontFace=fontface)
            cv2.putText(frame,mouthstatus,tuple(lip['mouth_lower_lip_bottom'].values()),fontScale=0.6,color=color,fontFace=fontface)
            face_data={'l_eye':l_eye,'r_eye':r_eye,'lip':lip,\
                'l_eye_status':l_eye_status,'r_eye_status':r_eye_status,'mouthstatus':mouthstatus,\
                    'emotion':emotion,'eyegaze':attribs['eyegaze']
                    }
                
        #To be checked!!!! gesture  detection
        if gesture_data:
            y,x,w,h=list(gesture_data['hand_rectangle'].values())
            cv2.rectangle(frame,(x,y),(x+w,y+h),thickness=2,color=color)
        cv2.imshow('寄',frame)
        cv2.waitKey(0)
    data={'face_data':face_data,'gesture_data':gesture_data}



    #testing !!!
    data={"emotion":emotion}
    if not os.path.exists("./json"):
        os.mkdir('./json')
    with open('./json/result'+str(result_index)+'json', "w") as outfile:
        json.dump(data, outfile)


    #To do: call jar file and pass data as parameter



