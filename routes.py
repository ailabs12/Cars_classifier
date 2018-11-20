#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:05:57 2018

@author: kdg
"""

import base64
import io
import uuid
from datetime import datetime, timedelta
from copy import deepcopy
from PIL import Image
from flask import Flask, make_response, request, json


import app.recognition_processor as rp

app = Flask(__name__)

@app.route('/car_classifier', methods=['POST'])
def classify_cars():
    if (not is_valid_request(request)):
            return json.jsonify(get_json_response(msg='Invalid request'))

    img_b64, _ = get_request_data(request)
    img_body = get_image_body(img_b64)

    if (img_body is None):
        return json.jsonify(get_json_response(msg='Image not found'))

    #start_time = datetime.now()
    prediction_result = rp.car_classificator(img_body) 
    #delta = datetime.now() - start_time

    if (prediction_result == []):
        return json.jsonify(get_json_response())
    # print(delta.total_seconds() * 1000.0)
    print(prediction_result)
    return json.jsonify(get_json_response(prediction_result))

def is_valid_request(request):
    return 'image' in request.json

def get_request_data(request):
    r = request.json
    image = r['image'] if 'image' in r else ''
    min_accuracy = r['minAccuracy'] if 'minAccuracy' in r else 60
    return image, min_accuracy

def get_image_body(img_b64):
    if 'data:image' in img_b64:
        img_encoded = img_b64.split(',')[1]
        return base64.decodebytes(img_encoded.encode('utf-8'))
    else:
        return None

def get_json_response(result=None, msg=None):
    json = {
        'success': False
    }

    if msg is not None:
        json['message'] = msg
        return json

    json['data'] = []

    if result is None:
        return json

    for item in result:
        json['data'].append(item)

    json['success'] = True
    return json

if __name__ == '__main__':
    app.run(port='8080', debug=True)