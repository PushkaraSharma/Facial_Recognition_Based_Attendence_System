import os
import numpy as np
import cv2
import time
def recog():

    def data_shaping():
        facepath = []
        for root,folder,files in os.walk('facedatas/'):
            for file in files:
                facepath.append(root+file)
        print(facepath)

        facedata =[]
        for face in facepath:
            facedata.append(np.load(face))

        facedata = np.asarray(facedata)
        facedata = facedata.reshape(-1,7500)
        print(facedata.shape)

        labels = os.listdir('facedatas/')
        print(labels)
        labelsname = {i : labels[i][:-4] for i in range(len(labels))}
        print(labelsname)

        outputlabels = np.zeros(len(facedata))

        slice_1 = 0
        slice_2 = 50
        try:
            for i in range(len(labels)):
                outputlabels[slice_1:slice_2]=i
                slice_1+=50
                slice_2+=50
        except BaseException:
            pass
        print(outputlabels.shape)
        return outputlabels,facedata,labelsname

    def distance(x1,x2):
        return np.sqrt(sum((x1-x2)**2))




    def knn(x,train,k,outputlabels):
        n = train.shape[0]
        dis = []
        for i in range(n):
            dis.append(distance(x,train[i]))
        dis = np.asarray(dis)
        indexes = np.argsort(dis)[:k]
        sort_label = outputlabels[indexes]
        counts = np.unique(sort_label,return_counts=True)
        d = counts[0][np.argmax(counts[1])]
        return labelsname[d]

    outputlabels,facedata,labelsname = data_shaping()


    def show():
        font = cv2.FONT_HERSHEY_COMPLEX
        dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        capture = cv2.VideoCapture(0)
        start = time.time()
        while True:
            ret, img = capture.read()
            if ret:
                grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = dataset.detectMultiScale(grey)
                for x, y, w, h in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 1)

                    face = img[y:y + h, x:x + h, :]
                    face = cv2.resize(img, (50, 50))

                    face = np.asarray(face)
                    face = face.reshape(50 * 50 * 3)
                    #face = face.reshape(1, face.shape[0])

                    text = knn(face,facedata,5,outputlabels)

                    cv2.putText(img, text, (x - 10, y - 20), font, 1, (255, 0, 0), 3)

                cv2.imshow('faces', img)
                if cv2.waitKey(1) == 27 or time.time()>start+5:
                    break

        capture.release()
        cv2.destroyAllWindows()
        return text

    text2 = show()
    return text2
#recog()