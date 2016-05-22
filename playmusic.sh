#!/bin/bash

echo Enter music name ":"

read x

cd ~
#$(python search.py -b -q "$x")

youtube-dl -f worst -o - $(python search.py -b -q "$x") | ffmpeg -i - -ab 192k -vn -acodec libmp3lame -f mp3 - |  mplayer -
