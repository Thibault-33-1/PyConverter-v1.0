#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from convert import *

avi_state = False
avi_button_state = False

mp4_state = False
mp4_button_state = False

mpeg_state = False
mpeg_button_state = False

flv_state = False
flv_button_state = False

mp3_state = False
mp3_button_state = False

wav_state = False
wav_button_state = False

ogg_state = False
ogg_button_state = False

aif_state = False
aif_button_state = False

bmp_state = False
bmp_button_state = False

jpeg_state = False
jpeg_button_state = False

png_state = False
png_button_state = False

tga_state = False
tga_button_state = False

main_window = ""
filename = ""
filename_no_extensions = ""

def create_window():
    global main_window
    main_window = Tk()
    main_window.title('PyConverter v1.0')
    main_window.resizable(width=False, height=False)

    global filename
    global filename_no_extensions

    global avi_button_state
    global mp4_button_state
    global mpeg_state_button_state
    global flv_state_button_state

    global mp3_state_button_state
    global wav_state_button_state
    global ogg_state_button_state
    global aif_state_button_state

    global bmp_state_button_state
    global jpeg_state_button_state
    global tga_state_button_state

    # Video formats
    global avi_state
    avi_state = IntVar()
    global mp4_state
    mp4_state = IntVar()
    global mpeg_state
    mpeg_state = IntVar()
    global flv_state
    flv_state = IntVar()

    # Music formats
    global mp3_state
    mp3_state = IntVar()
    global wav_state
    wav_state = IntVar()
    global ogg_state
    ogg_state = IntVar()
    global aif_state
    aif_state = IntVar()
    global aac_state
    aac_state = IntVar()

    # Images formats
    global bmp_state
    bmp_state = IntVar()
    global jpeg_state
    jpeg_state = IntVar()
    global png_state
    png_state = IntVar()
    global tga_state
    tga_state = IntVar()

    #Create video converter LabelFrame
    label_video = LabelFrame(main_window, bd=2, text='Video converter')
    label_video.pack(fill="both", side="left")
    Label(label_video).pack()

    #Create audio converter LabelFrame
    label_audio = LabelFrame(main_window, bd=2, text='Audio converter')
    label_audio.pack(fill="both", side="left")
    Label(label_audio).pack()

    #Create images converter LabelFrame
    label_img = LabelFrame(main_window, bd=2, text='Images converter')
    label_img.pack(fill="both", expand=False)
    Label(label_img).pack()

    # Check butttons for video convertion
    avi_button = Checkbutton(label_video, text="To .avi", variable=avi_state)
    avi_button.pack(anchor=W)

    mp4_button = Checkbutton(label_video, text="To .mp4", variable=mp4_state)
    mp4_button.pack(anchor=W)

    mpeg_button = Checkbutton(label_video, text="To .mpeg", variable=mpeg_state)
    mpeg_button.pack(anchor=W)

    flv_button = Checkbutton(label_video, text="To .flv", variable=flv_state)
    flv_button.pack(anchor=W)

    # Check butttons for images convertion
    jpeg_button = Checkbutton(label_img, text="To .jpeg", variable=jpeg_state)
    jpeg_button.pack(anchor=W)

    bmp_button = Checkbutton(label_img, text="To .bmp", variable=bmp_state)
    bmp_button.pack(anchor=W)

    png_button = Checkbutton(label_img, text="To .png", variable=png_state)
    png_button.pack(anchor=W)

    tga_button = Checkbutton(label_img, text="To .tga", variable=tga_state)
    tga_button.pack(anchor=W)

    # Check butttons for Audio convertion
    mp3_button = Checkbutton(label_audio, text="To .mp3", variable=mp3_state)
    mp3_button.pack(anchor=W)

    wav_button = Checkbutton(label_audio, text="To .wav", variable=wav_state)
    wav_button.pack(anchor=W)

    ogg_button = Checkbutton(label_audio, text="To .ogg", variable =ogg_state)
    ogg_button.pack(anchor=W)

    aif_button = Checkbutton(label_audio, text="To .aif", variable=aif_state)
    aif_button.pack(anchor=W)

    aac_button = Checkbutton(label_audio, text="To .aac", variable=aac_state)
    aac_button.pack(anchor=W)

    # Convert Button
    convert_button = Button(main_window, text="Convert", width=13, command=get_checkbutton_state)
    convert_button.pack(anchor=E)

    main_window.mainloop()

def get_checkbutton_state() :
    filename_no_extensions = get_file_path()

# Convert Video
    avi_button_state = avi_state.get()
    if avi_button_state == True :
        get_only_filename()
        convert_to_avi()

    mp4_button_state = mp4_state.get()
    if mp4_button_state == True :
        get_only_filename()
        convert_to_mp4()

    mpeg_button_state = mpeg_state.get()
    if mpeg_button_state == True :
        get_only_filename()
        convert_to_mpeg()

    flv_button_state = flv_state.get()
    if flv_button_state == True :
        get_only_filename()
        convert_to_flv()

# Convert Audio
    mp3_button_state = mp3_state.get()
    if mp3_button_state == True :
        get_only_filename()
        convert_to_mp3()

    wav_button_state = wav_state.get()
    if wav_button_state == True :
        get_only_filename()
        convert_to_wav()

    ogg_button_state = ogg_state.get()
    if ogg_button_state == True :
        get_only_filename()
        convert_to_ogg()

    aif_button_state = aif_state.get()
    if aif_button_state == True :
        get_only_filename()
        convert_to_aif()

    aac_button_state = aac_state.get()
    if aac_button_state == True :
        get_only_filename()
        convert_to_aac()

# Convert Images
    bmp_button_state = bmp_state.get()
    if bmp_button_state == True :
        get_only_filename()
        convert_to_bmp()

    jpeg_button_state = jpeg_state.get()
    if jpeg_button_state == True :
        get_only_filename()
        convert_to_jpeg()

    png_button_state = png_state.get()
    if png_button_state == True :
        get_only_filename()
        convert_to_png()

    tga_button_state = tga_state.get()
    if tga_button_state == True :
        get_only_filename()
        convert_to_tga()

create_window()
