#!/bin/sh
cd ~/Music
youtube-dl -f 249 https://www.youtube.com/watch?v=$2
ffmpeg -i *.webm -acodec libmp3lame -aq 4 $1.mp3
#etc.
