from snapper import snap
from directoryCreator import initialize, addName
from imageReader import readData
from trainer import train
from predictor import predict

options = ['Initialize names',
           'Add names',
           'Take pictures',
           'Read pictures',
           'Train',
           'Predict']
while True:        
    print("Enter the number next to the option")
    for index, option in enumerate(options):
        print(index, option)
    choice = input()
    if choice == '0':
        initialize()
    if choice == '1':
        addName()
    if choice == '2':
        snap()
    if choice == '3':
        readData()
    if choice == '4':
        train()
    if choice == '5':
        predict()
    if choice == 'exit':
        break

    
