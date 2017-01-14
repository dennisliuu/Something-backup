import subprocess
import shlex
a = input("Name: ")
b = input("Code:  ")
print ("Target: " + a + ".mp3")
subprocess.call(shlex.split('./yt.sh %s %s' % (str(a),str(b))))

