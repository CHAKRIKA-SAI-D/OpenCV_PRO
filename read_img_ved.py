import cv2
##for image reading its imread
img=cv2.imread("resources/image.png")
cv2.imshow("lenna",img)
##if we keep 0 in waitkey() then its like infinite loop
cv2.waitKey(1000)


##for vedio capture and camera access

framewidth=400
frameheight=400
##in the video capture if the digit is 0 then its for camera access (pc)
cap=cv2.VideoCapture(0)
# cap.set(3,framewidth)
# cap.set(4,frameheight)
while True:
    success,img=cap.read()
    #if you dont want to set those frameheights and frame widths then the beloww is using resize
    cv2.resize(img,(framewidth,frameheight))
    cv2.imshow("camera",img)
    ##press space bar for stopping
    if cv2.waitKey(1) & 0xFF==ord(" "):
        break
