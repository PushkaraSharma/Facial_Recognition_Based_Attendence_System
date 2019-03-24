import cv2
import numpy as np
import os

def detect_face(name):
    facedata = []
    dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)

    while True:
        ret,img = capture.read()
        if ret :
            grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = dataset.detectMultiScale(grey)
            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),1)

                face = img[y:y+h,x:x+h,:]
                face = cv2.resize(img,(50,50))

                if len(facedata)<50:
                    facedata.append(face)
                    print(len(facedata))


            cv2.imshow('faces',img)

            if cv2.waitKey(1)==27 or len(facedata)>=50:
                break

    facedata = np.asarray(facedata)
    facedata = facedata.reshape(50,50*50*3)
    np.save(os.path.join('facedatas',name+'.npy'),facedata)

    capture.release()
    cv2.destroyAllWindows()

#detect_face('pankaj')