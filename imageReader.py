import cv2 as cv
import numpy as np
import pickle
pic_filename = "data/photo_dataset.pkl"
label_filename = "data/label_dataset.pkl"
name_filename = "data/names.pkl"
image_number_filename = "data/image_numbers.pkl"

def readData():
    images = []
    labels = []
    file = open(name_filename,'rb')
    names = pickle.load(file)
    file.close()
    for index, name in enumerate(names):
        x = 1
        while True:
            print("Reading images")
            img = cv.imread("pics/"+name+"/img"+str(x)+".jpg")
            if img is None:
                break
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            img = cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)
            img = img.reshape((1,img.shape[0]*img.shape[1]))
            images.append(img)
            labels.append(index)
            x += 1

    print(len(images))
    images = np.array(images)
    file = open(pic_filename,"wb")
    pickle.dump(images, file)
    file.close()
    file = open(label_filename,"wb")
    pickle.dump(labels, file)
    file.close()
    
