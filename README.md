# ytdl-streamer

##Introduction

A simple bash script that can stream your youtube video right to your player right from terminal

##Useage

Clone or download this repo. `cd` to your repo directory. 
Just execute `sudo chmod +x ./playmusic.sh` and run. It will ask you to input your search term, and will stream it directly to [mplayer](https://help.ubuntu.com/community/MPlayer)

Here is the whole process summarized for newbies:

```
machine@localhost$ git clone "https://github.com/ashutosh2k12/ytdl-streamer.git"
machine@localhost$ cd ytdl-streamer
machine@localhost$ sudo chmod +x ./playmusic.sh 
machine@localhost$ ./playmusic.sh "in the end linkin park"
```

This will automatically pick best result from youtube api for the search term
and will start playing the mp3 for you. 

### Sidenote
This program requires `ffmpeg`, [youtube-dl](https://github.com/rg3/youtube-dl) and `mplayer`. Please install one before using this script.
For Ubuntu 12.04 or 14.04 users, use [this bash script](https://gist.github.com/xdamman/e4f713c8cd1a389a5917) 
