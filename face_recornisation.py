import cv2
face_cascade=cv2.CascadeClassifier('C:\\Users\\nishi\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('C:\\Users\\nishi\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\data\\haarcascade_eye.xml')
capture=cv2.VideoCapture(0)
while(1):
    ret,img=capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,7)
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),3)
    cv2.imshow('mycapture',img)
    k=cv2.waitKey(1)
    if k==27:
            break
capture.release()
cv2.destroyAllWindows()
