try:
	from setuptools import setup
except importerror:
	from distutils.core import setup

config = {
	'description':'tsblog',
	'author':'SuthakaranS',
	'url':'www.tssutha.com',
	'download_url':'where to download it',
	'author_email':'tssutha03@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['blog'],
	'scripts':[],
	'name': 'blog'
}

setup(**config)