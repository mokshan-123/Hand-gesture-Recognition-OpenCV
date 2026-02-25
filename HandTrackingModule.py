import cv2
import mediapipe as mp
import time



class handdetector():
    def __init__(self,image_mode=False,no_hands=2,complexity=1,min_det_conf=0.5,min_track_conf=0.5):
        self.image_mode=image_mode
        self.no_hands=no_hands
        self.complexity=complexity
        self.min_det_conf=min_det_conf
        self.min_track_conf=min_track_conf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.image_mode,self.no_hands,self.complexity,self.min_det_conf,self.min_track_conf)  # this always get only RGB values
        self.mpdraw = mp.solutions.drawing_utils


    def findhands(self,camdata,draw=True):
        RGBimg = cv2.cvtColor(camdata, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(RGBimg)
        if self.result.multi_hand_landmarks:
            for hand in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(camdata, hand, self.mpHands.HAND_CONNECTIONS)
        return camdata


    def findPosition(self,camdata,handNo=0,draw=True):
        lmlist=[]
        if self.result.multi_hand_landmarks:
            myhands=self.result.multi_hand_landmarks[handNo]
            for id, landmark in enumerate(myhands.landmark):
                h,w,c=camdata.shape
                pixel_x, pixel_y=int(landmark.x*w),int(landmark.y*h)
                lmlist.append([id,pixel_x,pixel_y])

                if draw:
                    cv2.circle(camdata,(pixel_x,pixel_y),15,(255,0,225),cv2.FILLED)
        return lmlist

def main():
    prevtime = 0
    nexttime = 0

    # get the images from camera
    getcam = cv2.VideoCapture(0)
    detector=handdetector()
    while True:
        sucess, camdata = getcam.read()
        img=detector.findhands(camdata)
        lmlist=detector.findPosition(img,0)

        if len(lmlist) != 0:
            print(lmlist[4])


        if not sucess:
            break

        nexttime = time.time()
        fps = 1 / (nexttime - prevtime)
        prevtime = nexttime

        cv2.putText(camdata, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 0), 3)

        cv2.imshow("Image", camdata)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
