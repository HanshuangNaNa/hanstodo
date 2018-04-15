#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年04月15日 星期日 21时11分11秒
# File Name: hello.py
# Description:
"""
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


