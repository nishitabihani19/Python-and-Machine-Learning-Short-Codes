import face_recognition
import cv2
vedio_capture=cv2.VideoCapture(0)
myimage=face_recognition.load_image_file("my.jpg")
myencode=face_recognition.face_encodings(myimage[0])
known_face_names=["Nishita"]
known_face_encode=[myencode]
while 1:
    
    ret,frame=vedio_capture.read()
    cv2.imshow("myimage",frame)
    rgb_frame=frame[:,:,::-1]
    face_locations=face_recognition.face_locations()
    face_encode=face_recognition.face_encodings(rgb_frame,face_encode)
    for(top,right,bottom,left),face_encode in zip(face_locations,face_encode):
        match=face_recorgnition.compare_faces(known_face_encode,face_encode)
        name="unknown"
        if true in match:
            first_match=match.index(True)
            name=known_face_names[first_match]
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.puttext(frame,name,(left+6,bottom+2),font,1.0,(0,0,255),1)

    cv2.imshow("vedio",frame)
    
