import cv2
pic=cv2.VideoCapture(0) #enable camera
ret,frame=pic.read()
pic.release()
cv2.imshow('pic',frame)
cv2.imwrite('pic')

