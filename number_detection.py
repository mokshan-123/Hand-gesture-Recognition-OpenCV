import cv2
import math
import HandTrackingModule as HTM
import time

cap=cv2.VideoCapture(0)
module=HTM.handdetector()

curr_time=0
prev_time=0

finger=[0,0,0,0,0]

while True:
    success , img = cap.read()
    img=module.findhands(img)
    landmarks=module.findPosition(img,draw=False)

    if len(landmarks) !=0:
        x0,y0=landmarks[0][1],landmarks[0][2]
        x4,y4=landmarks[4][1],landmarks[4][2]
        x8,y8=landmarks[8][1],landmarks[8][2]
        x12,y12=landmarks[12][1],landmarks[12][2]
        x16,y16=landmarks[16][1],landmarks[16][2]
        x20,y20=landmarks[20][1],landmarks[20][2]

        cv2.circle(img, (x4, y4), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x0, y0), 10, (255, 0, 255), cv2.FILLED)

        d4_2=math.hypot(x4-x0,y4-y0)
        d8_6=math.hypot(x8-x0,y8-y0)
        d12_10=math.hypot(x12-x0,y12-y0)
        d16_14=math.hypot(x16-x0,y16-y0)
        d20_18=math.hypot(x20-x0,y20-y0)

        if(d4_2 < 140):
            finger[0]=0
        else:
            finger[0]=1

        if (d8_6 < 200):
            finger[1] = 0
        else:
            finger[1] = 1

        if (d12_10 < 200):
            finger[2] = 0
        else:
            finger[2] = 1

        if (d16_14 < 190 ):
            finger[3] = 0
        else:
            finger[3] = 1

        if (d20_18 < 167):
            finger[4] = 0
        else:
            finger[4] = 1

        print(finger)

        #counting fingers
        count=finger.count(1)

        cv2.putText(img, f'NUMBER: {count}', (40, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)



    curr_time=time.time()
    FPS=1/(curr_time-prev_time)
    prev_time=curr_time

    cv2.putText(img,f'FPS: {int(FPS)}',(40,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)

    cv2.imshow("image",img)
    cv2.waitKey(1)
