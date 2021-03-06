# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:10:46 2018

@author: nicu
"""

import os
#from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'never-be-the-same-again'

    # For SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Setup for mail error logger:
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Add admins email adresses here:
    ADMINS = ['admin@localhost']

    # Babel
    LANGUAGES=['en', 'de']

    # Other
    POSTS_PER_PAGE=5