import cv2
import numpy as np
##(512,512)=>implies the height
#(3) implies the channel (to add the colors)
#as we are using the np to genrate for getting normal zeros we used unit8
img=np.zeros((512,512,3),np.uint8)
print(img)
#(0,0)=>from the start like x,y in the space
#end i img.shape[0]=>width, img.shape[1]=>height
#(0,255,0)=>bgr
#2=> thickness also can use cv2.FILLED for full fill
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)

cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,400),50,(255,0,0),3)#150,400=>center and 50 is radi
cv2.putText(img,"Testing",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
#in the above 75,50 is start, 1st 1 is for scale and 2nd 1 is for thickness
cv2.imshow("Image",img)
cv2.waitKey(0)

