#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Benjamin'


import os
import flask
import tools
from flask import request, send_from_directory


app = flask.Flask(__name__)


@app.route('/')
def status():
    return flask.jsonify({'Status': 'Alive'})


@app.route('/merge', methods=['POST'])
def upload():
    filenames = tools.get_files(request.files)
    if filenames:
        merged = tools.merge_files(filenames)
        uploaded = tools.serve_file(merged)
        os.remove(merged)
        return uploaded

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

hostname = tools.config().get(section='server', option='address')
port = tools.config().get(section='server', option='port')

app.run(host=hostname, port=int(port), debug=True)


