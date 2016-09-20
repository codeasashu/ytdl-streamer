#!/bin/bash

X="$1"
if [[ -z "$X" ]]; then
	echo Enter song ": " 
	read X
fi	

youtube-dl -f worst -o - $(python search.py -b -q "$X") |  mplayer -novideo -
