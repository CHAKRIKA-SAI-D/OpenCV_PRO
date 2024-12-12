import cv2

##resize
path="resources/image.png"
img=cv2.imread(path)
cv2.imshow("Image",img)
print(img.shape) #(225, 225, 3) where 3=bgr
width,height=500,500
elong_img=cv2.resize(img,(width,height))
cv2.imshow("elongated",elong_img)
print(elong_img.shape) #(500, 500, 3)

##cropping
img_cropped=img[100:200,5:189]
cv2.imshow("Image cropped",img_cropped)
img_crop_elong=cv2.resize(img_cropped,(img.shape[1],img.shape[0]))
cv2.imshow("elong_crop",img_crop_elong)
cv2.waitKey(0) 