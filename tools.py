#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Benjamin'


import time, os
import requests
from PyPDF2 import PdfFileMerger, PdfFileReader
from configparser import ConfigParser
from werkzeug.utils import secure_filename


def getpath(filename, folder=''):

    full_path = os.path.realpath(__file__)
    base_path = os.path.dirname(full_path)
    raw_path = os.path.join(base_path, folder, filename)
    return raw_path


def config():

    cnf = ConfigParser()
    cnf.read(filenames=getpath('config.ini'))
    return cnf


def allowed_file(filename):

    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    authorized = config().get(section='server', option='extensions')
    return ext == authorized


def get_files(uploaded_files):

    filename_list = []
    for file in uploaded_files:
        if not allowed_file(file):
            break
        filename = secure_filename(file)
        with open(getpath(filename, config().get(section='server', option='upload_folder'), ), 'wb') as pdf:
            pdf.write(uploaded_files[file].read())
        filename_list.append(filename)
    return filename_list


def merge_files(local_pdfs):

    name = 'merge_{0}_output.pdf'.format(str(time.clock())[2:])
    merged_export = PdfFileMerger()
    for pdfile in local_pdfs:
        filepath = getpath(pdfile, config().get(section='server', option='upload_folder'))
        file_bin = PdfFileReader(file(filepath, 'rb'))
        if file_bin.getIsEncrypted():
            file_bin.decrypt('')

        merged_export.append(fileobj=file_bin)
        os.remove(filepath)
    full_ouput = getpath(name, config().get(section='server', option='upload_folder'))
    with open(full_ouput, 'wb') as output:
        merged_export.write(output)

    return full_ouput


def serve_file(filepath):

    response = requests.post(url='https://gpldr.in/', files={'file': open(filepath, 'rb')},
                             data={'once': 'true', 'duration': '1w'})
    return response.content
