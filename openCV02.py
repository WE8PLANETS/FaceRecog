import cv2
capture = cv2.VideoCapture(0)
#if you want to read video from file write input file name
#or you can read it from camera two device index 0, -1
#for two camera you can use 1 
#to capture frame continuously we use while loop
while (True):
    ret, frame = capture.read()#return true if frame available and store in frame and ret store true or false
    #if you want gray video capture use cv2.Color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('GRAY', gray)
    k=cv2.waitKey(1)
    if k==27:#if user press esc key video capturing quit
        break
capture.release()
cv2.destroyAllWindows() 