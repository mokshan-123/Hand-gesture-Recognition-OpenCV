import cv2
import numpy as np
import time
import HandTrackingModule as HTG
import math
from pycaw.pycaw import AudioUtilities
cap=cv2.VideoCapture(0)

module=HTG.handdetector(min_det_conf=0.7)

################################################
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
#print(f"Audio output: {device.FriendlyName}")
#print(f"- Muted: {bool(volume.GetMute())}")
#print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
range=volume.GetVolumeRange()
min_vol=range[0]
max_vol=range[1]
###############################################


realtime=0
prevtime=0

landmarks=[]

vol=0
volbar=400
vol_perc=0
while True:
    success, img=cap.read()
    img=module.findhands(img,draw=True)

    landmarks=module.findPosition(img,draw=False)

    #to adjust the volume we need 4 and 8 landmark values
    if len(landmarks) !=0:
        #print(landmarks[4],landmarks[8])

        x1, y1 = landmarks[4][1], landmarks[4][2]
        x2, y2 = landmarks[8][1], landmarks[8][2]
        #get the mid point
        xm,ym=(x1+x2)//2,(y1+y2)//2

        #mark the 4 and 8 land marks
        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (xm, ym), 10, (255, 0, 255), cv2.FILLED)

        #draw a line between 2 circles
        cv2.line(img,(x1,y1),(x2,y2),(240,0,210),2)

        #get length
        length=math.hypot(x2-x1,y2-y1)
        #print(length)

        #Hand range is 15 to 160
        #We have to convert it to the volume range and get the volume according to the length
        vol=np.interp(length,[15,160],[min_vol,max_vol])
        volbar=np.interp(length,[15,160],[400,150])
        #print(length,vol)

        volume.SetMasterVolumeLevel(vol, None)
        vol_perc=np.interp(length,[15,160],[0,100])
        #print(vol_perc)

        #cv2.putText(img,f'Volume: {int(vol_perc)}',(10,100),1,cv2.FONT_HERSHEY_COMPLEX_SMALL,(255,0,0),2)

        if (length < 15) :
            cv2.circle(img, (xm, ym), 10, (0, 255, 0), cv2.FILLED)
        if(length >160):
            cv2.circle(img, (xm, ym), 10, (0, 0, 255), cv2.FILLED)

    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'VOL: {int(vol_perc)}', (40, 450), cv2.FONT_ITALIC, 1, (255, 0, 255), 2)

    #frames per second
    realtime=time.time()
    fps=1/(realtime-prevtime)
    prevtime=realtime

    #print fps on the display
    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_ITALIC,1,(255,0,255),2)


    cv2.imshow("Image",img)
    cv2.waitKey(1)
