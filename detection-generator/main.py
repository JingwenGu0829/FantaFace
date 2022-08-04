import cv2
from option import args
import requests

def onlineMain(pic):
    url = 'https://www.w3schools.com/python/demopage.php'
    myobj = {'somekey': 'somevalue'}


def offlineMain(pic):
    pass

def main():
    sum=0
    if args.input=='video':
        cap = cv2.VideoCapture(args.inputDir+'demo.mp3')
    else:
        cap = cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        if ret=='False':
            break
        sum+=1
        if sum%30==0:
            pic=cv2.imread(img)
            if args.approach=='Online_request':
                onlineMain(pic)
            elif args.approach=='Offline_request':
                offlineMain(pic)

        
            
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

    
