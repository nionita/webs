# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:18:00 2018

@author: nicu
"""

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers