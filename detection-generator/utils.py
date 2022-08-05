import cv2
from time import time
from urllib import request,error
def send_req(url, key, secret, frame,params):
    """
    Send request to Face++ server and return detection results.

    """
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    cv2.imwrite('frame.jpg',frame)
    fr = open('frame.jpg', 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    # The server only accepts bytes!!!!!
    data.append(fr.read())
    fr.close()
    # Optional params
    for name, value in params:
        data.append('--%s'%boundary)
        data.append('Content-Disposition: form-data; name="%s"\r\n' % name)
        data.append(value)
    print("boundary:",boundary)
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
        print(content)
        return content
    except error.HTTPError as e:
        print(e.read().decode('utf-8'))
def show_res(frame,face,gesture):
    """
    This function demonstrates the landmarks and emotions using opencv.
    """
    pass