import subprocess
import shlex
import os

a = input("Name: ")
b = input("Code: ")
print ("Target: " + a + ".mp3")

os.system("youtube-dl -F https://www.youtube.com/watch?v=%s" % str(b))
fm = input("Format: ")
os.system("youtube-dl -f %s https://www.youtube.com/watch?v=%s" % (str(fm),str(b)))
os.system("ffmpeg -i *.webm -acodec libmp3lame -aq 4 %s.mp3" % str(a))

