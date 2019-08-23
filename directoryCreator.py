'''This is where you initialize the names of the people you want the program
to identify, or edit and add names'''
import os
import pickle
filename = "data/names.pkl"
image_number_filename = "data/image_numbers.pkl"
def initialize():
    names = []
    while True:
        print("Type the name of the person you want us to identify and hit Enter!\n" +
              "When you're done, press 'q' or 'Q'.")
        name = input()
        if name == 'q' or name == 'Q':
            break
        names.append(name)
        print(name + "entered to database!")
    #Make directories for the every individual
    for name in names:
        dirname = "pics/" + name
        try:
            os.makedirs(dirname)
        except FileExistsError:
            print("Directory already exists")
    #Save the names list for further use
    try:
        os.mkdir('data')
    except FileExistsError:
        print("Directory already exists")
    file_handler = open(filename,"wb")
    pickle.dump(names, file_handler)
    file_handler.close()
    file_handler = open(image_number_filename,"wb")
    numbers = [0 for x in range(len(names))]
    pickle.dump(numbers, file_handler)
    file_handler.close()

def addName():
    file_handler = open(filename,"rb")
    names = pickle.load(file_handler)
    file_handler.close()
    file_handler = open(image_number_filename,"rb")
    numbers = pickle.load(file_handler)
    file_handler.close()
    while True:
        print("Type the name of the person you want us to identify and hit Enter!\n" +
              "When you're done, press 'q' or 'Q'.")
        name = input()
        if name == 'q' or name == 'Q':
            break
        names.append(name)
        numbers.append(0)
        dirname = "pics/" + name
        try:
            os.makedirs(dirname)
        except FileExistsError:
            print("Directory already exists")
        print(name + "entered to database!")
    file_handler = open(filename,"wb")
    pickle.dump(names, file_handler)
    file_handler.close()
    file_handler = open(image_number_filename,"wb")
    pickle.dump(numbers, file_handler)
    file_handler.close()

