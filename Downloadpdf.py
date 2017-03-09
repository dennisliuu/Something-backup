import urllib.request, os

pathname = input('Creat a floder:')
start = int(input('Start: '))
end = int(input('End: '))

os.system('mkdir %s' % pathname)

for i in range(start, end + 1):
	url = 'http://phys.thu.edu.tw/~mengwen/UniversityPhysics/Halliday-problem/100-homework-Ch%s.pdf' % i
	# Download the file from `url` and save it locally under `file_name`:
	try:
		with urllib.request.urlopen(url) as response, open('./%s/100-homework-Ch%s.pdf' % (pathname, i), 'wb') as out_file:
		    data = response.read() # a `bytes` object
		    out_file.write(data)
	except:
		print('404')
		i=i+1