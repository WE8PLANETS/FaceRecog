import numpy as np
import cv2
img= cv2.imread("lara.jpg",1)

#if you want to add black image using numpy
img=np.zeros([512, 512, 3], np.uint8)

#if you want to add  a arrowed line in pic
img=cv2.arrowedLine(img, (0,0),(255,255), (0, 255, 0), 3)

#if you want to add rectangle in picture
img=cv2.rectangle(img, (384,0), (510,128),(0,255,),5)
#if you write -1 in the place of thickness 5 it will fill the rectangle with color

#if you want to add circle in picture
img=cv2.circle(img,(447,63),63,(0,255,0),-1)

#if you want to add text in the picture
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img, "openCV", (10,500), font, 4, (255,0,0), 10,cv2.LINE_AA)
cv2.imshow("image",img)

#wait key is used to hold the screen
cv2.waitKey(0)
cv2.destroyAllWindows()
