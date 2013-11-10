import string


def openfile():
	f = open('/static/pages/index.txt')
	data = f.read()
	print data
		
openfile()