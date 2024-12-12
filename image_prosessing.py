import cv2
import numpy as np
path="resources/image.png"
#normal_img
img=cv2.imread(path)
cv2.imshow("normal image",img)

#kernal creation
kernel=np.ones((5,5),np.uint8)
#print(kernal)
#grey scale image
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# grey1=cv2.cvtColor(img,0)
cv2.imshow("Grey image",grey)
# img2=cv2.imread(path,0)
# cv2.imshow("Grey image one ",img2)

#blurr image
#note: only odd numbers are allowed
blur_img=cv2.GaussianBlur(img,(7,7),0)
blur_img_grey=cv2.GaussianBlur(grey,(7,7),0)
cv2.imshow("blur image",blur_img)
cv2.imshow("blur grey image",blur_img_grey)

#canny image
canny_img=cv2.Canny(blur_img_grey,100,200)
canny_grey=cv2.Canny(blur_img_grey,100,200)
cv2.imshow("Canny image",canny_img)
cv2.imshow("Canny image grey",canny_grey)
#Dilation
dialation=cv2.dilate(canny_img,kernel,iterations=1)
dialation_grey=cv2.dilate(canny_img,kernel,iterations=1)
cv2.imshow("Dialated",dialation)
cv2.imshow("Dialated grey",dialation_grey)
#Erodation
eroded=cv2.erode(dialation,kernel,iterations=1)
eroded_grey=cv2.erode(dialation,kernel,iterations=1)
cv2.imshow("'Eroded",eroded)
cv2.imshow("'Eroded grey",eroded_grey)
cv2.waitKey(0)