#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Benjamin'

import os
import requests

full_path = os.path.realpath(__file__)
base_path = os.path.dirname(full_path)
filename = 'test.pdf'
raw_path = os.path.join(base_path, filename)

files = {'file[]': open(raw_path, 'rb')}
resp = requests.post(url='http://127.0.0.1:6000/merge', files=files)

print resp.content
