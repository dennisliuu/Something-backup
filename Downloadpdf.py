import urllib.request, os
import webbrowser

# -*- coding: utf8 -*-

# for i in range(1,11):
# 	webbrowser.open(urllib.request.unquote('http://web.phys.ntu.edu.tw/ap/102hangout/grad2/Home%20Work%20Solutions%20%s.pdf') % i) 


# pathname = input('Creat a floder:')
# start = int(input('Start: '))
# end = int(input('End: '))
# os.system('mkdir %s' % pathname)
for i in range(1, 10 + 1):	
	url = "http://web.phys.ntu.edu.tw/ap/102hangout/grad2/Home%20Work%20Solutions%20" + str(i) + ".pdf"
	# Download the file from `url` and save it locally under `file_name`:
	try:
		with urllib.request.urlopen(url) as response, open('Home Work Solutions %s.pdf' % i, 'wb') as out_file:
		    data = response.read() # a `bytes` object
		    out_file.write(data)
	except:
		print('404')
	