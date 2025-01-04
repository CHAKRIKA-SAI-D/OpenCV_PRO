import cv2
import numpy as np
import time
import HandTrackingProject.HandTrackerModule as htm
import math
###############
wcam,hcam=640,480
ptime=0
vol=0
volBar=400
perc=0
####################
##refersences: https://github.com/AndreMiras/pycaw    {for sound module}
##pip install pycaw
###################


##################
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange() ##(-63.5, 0.0, 0.5) in my pc

minVol=volRange[0]
maxVol=volRange[1]
######################################
cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
detector=htm.HandDetector(detectionCon=0.7)
while True:
    success,img=cap.read()
    detector.findHands(img)
    lmlist=detector.findPosition(img)
    if lmlist:
        #4 is for thumb
        #8 for index
        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),20,(0,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),20,(0,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,0,0),10)
        cv2.circle(img,(cx,cy),20,(0,0,255),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        # print(length)
        ##min_dist=<35
        ##max_dist=>230
        if length<40:
            cv2.circle(img,(cx,cy),20,(255,255,255),cv2.FILLED)
        vol=np.interp(length,[50,230],[minVol,maxVol])
        volBar=np.interp(length,[50,230],[400,150]) ##the last list is the range like the values hsould be in range 400-150 itseems
        perc=np.interp(length,[50,230],[0,100])
        # print(vol)
        cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
        volume.SetMasterVolumeLevel(vol, None) ##here  0 means 100volume
        cv2.putText(img,f"FPS: {int(fps)}",(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f"%: {int(perc)}",(53,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),3)
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF==ord(" "):
        break