from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import f1_score
import pickle
import numpy as np
from time import time

pic_filename = "data/photo_dataset.pkl"
label_filename = "data/label_dataset.pkl"
classifier_filename = "data/classifier.pkl"
pca_filename = "data/pca.pkl"

def train():
    pic_file_handler = open(pic_filename,"rb")
    pics = pickle.load(pic_file_handler)
    pic_file_handler.close()

    label_file_handler = open(label_filename,"rb")
    labels = pickle.load(label_file_handler)
    label_file_handler.close()
    n_samples = pics.shape[0]
    n_features = pics.shape[2]
    n_classes = max(labels)+1
    pics = pics.reshape((n_samples,n_features))
    print("Total dataset size")
    print ("n_classes: %d" % n_classes)
    print ("n_samples: %d" % n_samples)
    print ("n_features: %d" % n_features)

    ###############################################################################
    # Split into a training and testing set
    x_train, x_test, y_train, y_test = train_test_split(pics, labels, test_size=0.3, random_state=42)

    ###############################################################################
    # Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
    # dataset): unsupervised feature extraction / dimensionality reduction
    n_components = 100

    print ("Extracting the top %d eigenfaces from %d faces" % (n_components, x_train.shape[0]))
    t0 = time()
    pca = PCA(n_components=n_components, whiten=True).fit(x_train)
    print ("done in %0.3fs" % (time() - t0))

    #eigenfaces = pca.components_.reshape((n_components, 240, 360))

    print ("Projecting the input data on the eigenfaces orthonormal basis")
    t0 = time()
    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)
    print ("done in %0.3fs" % (time() - t0))

    ###############################################################################
    # Train a SVM classification model

    print ("Fitting the classifier to the training set")
    t0 = time()
    param_grid = {
             'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
              }
    # for sklearn version 0.16 or prior, the class_weight parameter value is 'auto'
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(x_train_pca, y_train)
    print ("done in %0.3fs" % (time() - t0))
    print ("Best estimator found by grid search:")
    print (clf.best_estimator_)

    ###############################################################################
    # Quantitative evaluation of the model quality on the test set

    print ("Predicting the people names on the testing set")
    t0 = time()
    y_pred = clf.predict(x_test_pca)
    print ("done in %0.3fs" % (time() - t0))
    print ("f1 score is: ", f1_score(y_test, y_pred, average = None))

    clf_file_handler = open(classifier_filename,"wb")
    pickle.dump(clf, clf_file_handler)
    clf_file_handler.close()

    pca_file_handler = open(pca_filename,"wb")
    pickle.dump(pca, pca_file_handler)
    pca_file_handler.close()

    input("Press any key to continue")
