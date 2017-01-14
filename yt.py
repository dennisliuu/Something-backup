import subprocess
import shlex
import os

a = input("This song name: ")
b = input("The youtube code: ")


os.system("youtube-dl -F https://www.youtube.com/watch?v=%s" % str(b))
fm = input("Format code: ")                                                                  os.system("youtube-dl -f %s https://www.youtube.com/watch?v=%s" % (str(fm),str(b)))
print("webm now is ok!")
yes = input("Do you want to Format?(y/N)")

if str(yes) == "y" :
	typ = input("What type? ")
	os.system("ffmpeg -i *.webm -acodec libmp3lame -aq 4 %s.%s" % (str(a),str(typ)))
	os.system("rm *.webm")
else:
	exit()
