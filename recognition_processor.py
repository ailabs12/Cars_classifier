#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:48:37 2018
TESTING!!!
@author: kdg
"""
import os
import sys
import logging
import copy
from datetime import datetime

import cv2
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import image
from keras import backend
import numpy as np
#import matplotlib.pyplot as plt

backend.clear_session()

_SAVE_DIR = 'static/result'
_MODELS_PATH = './trained_models/'
_CARS = ['Ambulance', 'Fire Truck', 'Garbage Truck', 'MCHS Car',
         'OTHERS', 'Police Car']

img_width, img_height = 128, 128

def car_classificator(image_body):
    """
    Predicts car-type for single car on the image
    Params:
        image (base64) - input image
    Returns:
        prediction (list) - list of car prediction 
    """
    # LOADING MODELs 
    modls_lst = ['MobNet2.h5', 'MobNet2_1.h5', 'MobNet2_2.h5', 'MobNet2_3.h5']
    modls = []
    for i in modls_lst:
        modls.append(load_model(_MODELS_PATH + i, compile=False))
   
    unchanged_image = cv2.imdecode(np.fromstring(image_body,
                           np.uint8), cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(unchanged_image, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (img_width, img_height))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis = 0)
    predictions = []
    for m in modls:
        pred = m.predict(x)[0]
        for i in range(len(_CARS)):
            if i == np.argmax(pred):
                print(_CARS[i], "%.2f%%" % (max(pred)*100))
                predictions.append((_CARS[i], str(max(pred))))               
    return predictions
    
    
               
                