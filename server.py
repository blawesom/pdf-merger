#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Benjamin'


import flask
import json
import tools
from flask import request, send_from_directory


app = flask.Flask(__name__)


@app.route('/')
def status():
    return json.dumps({'Status': 'Alive'})


@app.route('/merge', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("file[]")
    filenames = tools.get_files(uploaded_files)
    if filenames:
        merged = tools.merge_files(filenames)
        uploaded = tools.serve_file(merged)
        return uploaded
    return "No files accepted"


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)


hostname = tools.config().get(section='server', option='address')
port = tools.config().get(section='server', option='port')

app.run(host=hostname, port=int(port), debug=True)


