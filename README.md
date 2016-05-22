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
machine@localhost$ ./playmusic.sh
Enter music name:
In the end
```

This will automatically pick best result from youtube api for the search term
and will start playing the mp3 for you. 
