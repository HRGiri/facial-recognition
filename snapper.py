import numpy as np
import cv2 as cv
import pickle
name_filename = "data/names.pkl"
image_number_filename = "data/image_numbers.pkl"
def snap():
    file = open(image_number_filename,'rb')
    numbers = pickle.load(file)
    file.close()
    file = open(name_filename,'rb')
    names = pickle.load(file)
    file.close()
    print("Whose photo do you want to capture?\nEnter the number next to the name")
    for number, name in enumerate(names):
        print(str(number) + "\t" + name)
    num = int(input())

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    print("Press 'c' to capture\n" +
          "Press 'a' to capture another's photos\n"
          "Press 'q' to quit")
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Display the frame
        cv.imshow('frame', frame)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('a'):
            print("Whose photo do you want to capture?\nEnter the number next to the name")
            for number, name in enumerate(names):
                print(str(number) + "\t" + name)
            num = int(input())
        elif key == ord('c'):
            numbers[num] += 1
            filename = "pics/" + names[num] + "/img"  + str(numbers[num]) + ".jpg"
            cv.imwrite(filename, frame)
            print("Image " + str(numbers[num]) + " of " +
                  names[num] + " stored successfully")

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    file = open(image_number_filename,'wb')
    pickle.dump(numbers,file)
    file.close()
