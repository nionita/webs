# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:19:41 2018

@author: nicu
"""

from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}