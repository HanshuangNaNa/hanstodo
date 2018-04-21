#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年04月19日 星期四 22时05分08秒
# File Name: demo.py
# Description:
"""
import logging
import os
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

if __name__ == '__main__':
    print(__file__)
    print('dirname{}'.format(os.path.abspath(os.path.dirname(__file__))))
    print(os.path.dirname(__file__))
