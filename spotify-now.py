#!/usr/bin/env python
"""
spotify-now.py

Get info on the current spotify song
https://github.com/getmicah/spotify-now

Created by Micah Cowell
https://micahcowell.com
"""
import sys, os, subprocess

def getInfo(a):
    status = subprocess.check_output("pidof spotify | wc -l", shell=True)
    if "1" in str(status):
        meta = subprocess.check_output("dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'", shell=True)
        print(meta)
    else:
        print('Spotify doesn\'t seem to be running')

# allow only one argument
if len(sys.argv) == 2:
    getInfo(sys.argv[1])
else:
    print('error')
