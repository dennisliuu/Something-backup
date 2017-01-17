import subprocess
import shlex
import os

print("")
code = input("The youtube code: ")
name = input("This song's name: ")
print("")

os.system("youtube-dl -F https://www.youtube.com/watch?v=%s" % str(code))
fm = input("Format code: ")
os.system("youtube-dl -f %s https://www.youtube.com/watch?v=%s" % (str(fm),str(code)))

os.system("mv *.mv %s.webm" % str(name))
print("%s.webm now is ok!" % str(name))

yes = input("Do you want to Format?(y/N)")

if str(yes) == "N":
	exit()
else:
	typ = input("What type?(mp3 as default) ")
	if str(typ) == "":	
		os.system("ffmpeg -i *.webm -acodec libmp3lame -aq 4 %s.mp3" % str(name))
	else:
		os.system("ffmpeg -i *.webm -acodec libmp3lame -aq 4 %s.%s" % (str(name),str(typ)))	
	os.system("rm %s.webm" % str(name))
	exit()
