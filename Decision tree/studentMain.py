#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn import tree

from class_vis import output_image, prettyPicture
from classifyDT import classify
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()


# the classify() function in classifyDT is where the magic
# happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

pred = clf.predict(features_test)


# grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
