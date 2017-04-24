#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""
import os
import sys
from time import time

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

from email_preprocess import preprocess

os.chdir('/Users/shobhaMkand/Desktop/ud120-projects/naive_bayes')

sys.path.append("/Users/shobhaMkand/Desktop/ud120-projects/tools")


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred, labels_test)


def submitAccuracies():
    return {"acc_min_samples_split_2": round(acc_min_samples_split_2, 3),
            "acc_min_samples_split_50": round(acc_min_samples_split_50, 3)}
