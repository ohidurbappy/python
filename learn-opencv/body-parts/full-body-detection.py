import numpy as np
import cv2

full_body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #(img, human, 1.02, 2, 0 | 1, Size(40,70), Size(80, 300)
    bodies=full_body_cascade.detectMultiScale(gray,1.02, 2, 0 | 1, Size(40,70), Size(80, 300))
    

    for (x,y,w,h) in bodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
