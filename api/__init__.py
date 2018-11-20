#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:04:11 2018
REST API
@author: kdg
"""
from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import cars_recognizing

def create_app(config_class=Config):
    app = Flask(__name__)

    # ...

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')