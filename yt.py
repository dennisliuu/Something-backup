import subprocess
import shlex
import os

code = input("The youtube code: ")
name = input("This song's name: ")
name = name.replace(" ", "\ ")
print("")

os.system("youtube-dl -F https://www.youtube.com/watch?v=%s" % str(code))
fm = input("Format code: ")
os.system("youtube-dl -f %s https://www.youtube.com/watch?v=%s" % (str(fm),str(code)))

try :
	os.system("mv *.webm %s.webm" % str(name))
except:
	os.system("mv *.mp4 %s.mp4" % str(name))

print("%s.webm now is ok!" % str(name))

yes = input("Do you want to Format?(Y/n)")

if str(yes) == "Y":
	typ = input("What type?(mp3 as default) ")
	if str(typ) == "":	
		os.system("ffmpeg -i *.webm -acodec libmp3lame -aq 4 %s.mp3" % str(name))
		os.system("rm %s.webm" % str(name))
		os.system("mv %s.mp3 ~/Music" % str(name))
		exit()

	else:
		os.system("ffmpeg -i *.webm -acodec libmp3lame -aq 4 %s.%s" % (str(name),str(typ)))	
		os.system("rm %s.webm" % str(name))
		os.system("mv %s.%s ~/Music" % (str(name),str(typ)))
		exit()
else:	
	os.system("mv %s.webm ~/Music" % str(name))
	exit()
	
