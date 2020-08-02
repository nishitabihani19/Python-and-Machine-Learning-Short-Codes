from tkinter import *
import re,psutil,cv2,webbrowser,requests,json,math,wikipedia
import cv2
root=Tk()
root.grid()
root.geometry("500x500")
head1=Label(root,text="press Space to click",fg='black').place(x=10,y=100)
head2=Label(root,text="Escape to Terminate",fg='black').place(x=10,y=140)
def camera():
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()

    cv2.destroyAllWindows()
butn=Button(root,text="Switch Camera",command=camera).place(x=100,y=200)

root.mainloop()
