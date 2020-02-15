import cv2
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.ger(4))
while(cap.isOpened()):
    ret, frame=cap.read()
    if ret == True:
       
        cv2.imshow('frame', frame)

        k=cv2.waitKey(1)
        if k==27:
            break
        else:
            break
cap.release()
cv2.destroyAllWindows() 