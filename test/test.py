#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Benjamin'

import os
import requests

full_path = os.path.realpath(__file__)
base_path = os.path.dirname(full_path)

file1 = os.path.join(base_path, 'testA.pdf')
file2 = os.path.join(base_path, 'testB.pdf')

files = {'testA': open(file1, 'rb').read(),
         'testB': open(file2, 'rb').read()}

resp = requests.post(url='http://127.0.0.1:6000/merge', files=files)

print resp.content
