import os
from detection.detector import process_image,process_video
import cv2
from detection.option import args


input_dir=args.inputDir
input=args.input

def img_process():

    dirs=os.listdir(input_dir+'img')
    for files in dirs:
        if files!='.DS_Store':  #in case of the DS_store file in the MAC operating system
            file_dir=str(input_dir+'img/'+files)
            frame=cv2.imread(file_dir)
            process_image(frame,copy_to_clipboard=args.clipboard,dynam_wallpaper=args.dynamwall)

def process_cam():
    process_video()

def video_process():
    dirs=os.listdir(input_dir+'video')
    for files in dirs:
        file_dir=str(input_dir+'video/'+files)
        process_video(path=file_dir)

if __name__=='__main__':
    if args.input=='img':
        img_process('no') #testing
    elif args.input=='cam':
        process_cam()
    elif args.input=='video':
        video_process()