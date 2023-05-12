import numpy as np
import cv2 as cv
import os
trial, count = 10, 0

def Extract_Frames(interval:int):
    'Extract frames in x interval '
    for video in os.listdir('./data/row/video'):
        # if trial>count:
        if video.endswith('mp4') or video.endswith('avi'):
            print('video'+video)    
            cap = cv.VideoCapture('./data/row/video/'+video)
            c=1
            success,image = cap.read()
            while success:
                if c% interval==0:
                # resize image into input shape
                    # to be implement
                    cv.imwrite(f'./data/row/img/emotion'+ str(c) + '-' + video[:-4] + '.png', image)
                    success,image = cap.read()
                    print('Read a new frame: ', success)

                c= c+1

            cap.release()
            # count = count+1  
