from sklearn.svm import SVC
from sklearn.decomposition import PCA
import pickle
import numpy as np
import cv2 as cv

font = cv.FONT_HERSHEY_SIMPLEX

name_filename = "data/names.pkl"
classifier_filename = "data/classifier.pkl"
pca_filename = "data/pca.pkl"

def predict():
    file = open(name_filename,'rb')
    names = pickle.load(file)
    file.close()
    file = open(classifier_filename,'rb')
    clf = pickle.load(file)
    file.close()
    file = open(pca_filename,'rb')
    pca = pickle.load(file)
    file.close()

    #Start video capture object
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #Convert the frame
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img = cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)
        img = img.reshape((1,img.shape[0]*img.shape[1]))
        img = pca.transform(img)
        #Predict the name
        name = clf.predict(img)
        cv.putText(frame,names[name[0]],(10,400), font, 2,(255,255,255),2,cv.LINE_AA)
        # Display the frame
        cv.imshow('frame', frame)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
