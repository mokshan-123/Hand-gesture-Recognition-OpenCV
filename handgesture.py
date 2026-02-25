import cv2
import mediapipe as mp
import time

#get the images from camera
getcam=cv2.VideoCapture(0)

prevtime=0
nexttime=0

mpHands=mp.solutions.hands
hands=mpHands.Hands() #this always get only RGB values
mpdraw=mp.solutions.drawing_utils

#get video data
while True:
    sucess,camdata=getcam.read()

    if not sucess:
        break

    RGBimg=cv2.cvtColor(camdata,cv2.COLOR_BGR2RGB)

    result=hands.process(RGBimg)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            #get the id of the land mark and the coordinates
            for id, landmark in enumerate(hand.landmark):
                h,w,c=camdata.shape
                pixel_x, pixel_y=int(landmark.x*w),int(landmark.y*h)
                print(id, "-->", pixel_x,pixel_y)

                if id==4:
                    cv2.circle(camdata,(pixel_x,pixel_y),25,(255,0,0),cv2.FILLED)
                if id==8:
                    cv2.circle(camdata,(pixel_x,pixel_y),25,(0,255,0),cv2.FILLED)
            mpdraw.draw_landmarks(camdata,hand,mpHands.HAND_CONNECTIONS)

    nexttime=time.time()
    fps=1/(nexttime-prevtime)
    prevtime=nexttime

    cv2.putText(camdata,str(int(fps)),(10,70),cv2.FONT_ITALIC,3,(255,0,0),3)

    cv2.imshow("Image",camdata)
    cv2.waitKey(1)
