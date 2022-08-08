from django.shortcuts import render
import cv2
import threading



def start(request):
    if  request.POST.get('url')=='test':
        print("OK")
    return render(request,'start.html')

"""""
class VideoCamera():
    def __init__(self) -> None:
        self.video=cv2.VideoCapture(0)
        (self.grabbed,self.frame)=self.video.read()
        threading.Thread(target=self.update,args=()).start()
    def __del__(self):
        self.video.release()
    def get_frame(self):
        image=self.frame
        _,jpeg=cv2.imcode('.jpg',image)
        return jpeg.tobytes()
    def update(self):
        while True:
            (self.grabbed,self.frame)=self.video.read()

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'frame\r\n'
              b'Content-Type:image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')
"""""