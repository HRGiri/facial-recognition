# facial-recognition
A text-based facial recognition software using Machine Learning in Python 3. 
## About
This project is a module based, but end to end package of Face Recognition. It covers data collection, data processing, training a classifier and predicting images.

## Libraries required
#### 1. Numpy
NumPy is a library for Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
#### 2. Scikit Learn
Scikit-learn is a machine learning library for Python that features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
#### 3. OpenCV
OpenCV (Open source computer vision) is a library of programming functions mainly aimed at real-time computer vision. The library is cross-platform and free for use under the open-source BSD license.

## Instructions
#### 1. Preparing the dataset
The directorycreator.py is a program that will take the names of people you want to identify as input and create respective directories for them along with storing the names in a pkl file. You should begin with at least 2 people. You can add more people later. The names of the directories serve as label names.

After the directories are created, fill them with 640x480 pictures of the respective people's faces. For the best results, take your time and use the snapper.py to click and store images from your webcam. Take as any pictures as you can, with different facial expressions, lighting and backgrounds for best results.

Next, use the imagereader.py to convert the images into numpy arrays.

#### 2. Training the classifier
In this part, we divide the training data into training data and testing data. Then we use a PCA(Principal Component Analysis) method for dimensionality reduction/ feature extraction. Then we use an SVM classifier to train the data.

All the above is done in trainer.py.

#### 3. Predicting faces
After we've trained our data, run the predictor.py to open up an OpenCV window that takes your webcam frames as input and displays the predicted name.
