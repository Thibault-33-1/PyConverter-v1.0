#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

from Tkinter import *
from tkFileDialog import *
from PIL import Image

avi_state = False
mp4_state = False
mpeg_state = False
flv_state = False

mp3_state = False
wav_state = False
ogg_state = False
aif_state = False

bmp_state = False
jpeg_state = False
png_state = False
tga_state = False

filename = ""
filename_no_extensions = ""

path = ""
main_window = ""

def get_file_path() :
    global path
    path = open_file()

    get_filename()

def open_file() :
    file_path = askopenfilename(initialdir=sys.argv[0], title='Select File', filetypes = (('all files', '*.*'), ('avi files', '*.avi'), ('mp4 files', '*.mp4'),\
    ('jpeg files', '*.jpg'), ('bmp files', '*.bmp'), ('png files', '*.png'), ('mp3 files', '*.mp3'), ('wav files', '*.wav'), ('ogg files', '*.ogg'), \
    ('aif files', '*.aif')))

    return file_path

def get_filename() :
    inverted_path = ''
    inverted_filename = ''

    i = len(path)
    j = 0

    global filename
    filename = ""
    global filename_no_extensions
    filename_no_extensions = ""

    # Invert the path
    for letter in reversed(path) :
        inverted_path += letter

    # we split the inverted path for get only the file name inverted
    i = 0
    while i < len(inverted_path):
        if inverted_path[i] == '/':
            break
        else :
            inverted_filename += inverted_path[i]
            i += 1

    # we put back the right side of the filename
    for letter in reversed(inverted_filename) :
        filename += letter

    i = 0
    for elt in filename :
        if elt == ' ' :
            os.rename(filename, filename.replace(" ", "_"))
            sys.exit('The file have been renamed please re call convert operation.\nExiting ...\n')


def get_only_filename() :
    global filename
    global filename_no_extensions
    i = 0

    while i < len(filename):
        if filename[i] == '.':
            break
        else :
            filename_no_extensions += filename[i]
            i += 1

# Convert video
def convert_to_avi() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.avi'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_mp4() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.mp4'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_mpeg() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.mpeg'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_flv() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.flv'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

# Convert audio
def convert_to_mp3() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.mp3'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_wav() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.wav'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_ogg() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.ogg'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_aif() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.aif'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_aac() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.aac'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

# Convert images
def convert_to_bmp() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.bmp'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_jpeg() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.jpeg'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_png() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.png'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_tga() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.tga'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()
