#
# This is main server side code in python and webpy
# 
#
#


import web
from web import form
import markdown
from os.path import  join
import os
import datetime

#urls = (
#	'/', 'index',
#	'/login', 'login',
#	'/register','register',
#
#	'/submit', 'submit',
#	'/archive', 'archive',
#	'/about', 'about',
#	'/(.*)', 'page',
#)

urls = (
	'/', 'index',
	'/archive', 'archive',
	'/about', 'about',
	'/blog/(.*)', 'page',
	'/projects', 'projects',
	
)

app = web.application(urls, globals())
render = web.template.render('templates/',base='layout1')
md = markdown.Markdown(output_format='html5', extensions=['codehilite(linenums=True)'])

class post(object):
	"""
		post class is to store each post information
		
	"""
	def __init__(self):
		self.date = "21-12-1983"
		self.title = "This is post's title"
		self.summary = "Summary"
		self.filename = ""
# and not file.startswith("2013-08-10")	
class post_adap(object):
	"""
		This post_adp class ,read all markdown files from static/page
		folder and get post information from file name, such as 
		date, title, summary and store into list of post object
		Index page use this list of post information to render the 
		from page. 
		sample file name : yyyy-mm-dd-this-is-post-title.markdown
		where
			post.date = yyyy-mm-dd
			post.title = this is post title
	"""
	def __init__(self):
		self.postList = []
		
	def getposts(self):
		"""
			Get List of post information , sorted by date object
		"""
		for r,d, f in os.walk('static/pages/'):
			for file in f:
				if not file.startswith('.') and not file.startswith("2013-08-10"):
					pst = post()
					fname,title, dt = self.getpostprops(file)
					pst.date = dt
					pst.title = title
					pst.filename = 'blog/'+ fname
					self.postList.append(pst)
		self.postList = self.sort_post_by_date(self.postList)
		return self.postList
	
	def getpostprops(self,filename):
		"""
			Process the post file name (markdown) and extract the 
			post properties such as date, title, summary
		"""
		ls = filename.split('.')
		filename = ls[0]
		ls = filename.split('-')
		date = '-'.join(ls[0:3])
		dt = datetime.date(int(ls[0]), int(ls[1]), int(ls[2]))
		title = ' '.join(ls[3:])
		return ( filename, title,dt.__str__())
	
	def sort_post_by_date(self,postls):
		"""
		 Sort a list of post object based on their written 
		 date
		"""
		for i in range(len(postls)):
			for j in range(i + 1,len(postls)):
				if postls[i].date < postls[j].date:
					tmpst = post()
					tmpst = postls[i]
					postls[i] = postls[j]
					postls[j] = tmpst
		return postls
		

class index(object):
	"""
		Index Page, get the list post object and 
		render it in front page
	"""
	def GET(self):
		postAdap = post_adap()
		return render.index(postAdap.getposts())
		
class projects(object):
	def GET(self):
		#each URL maps to corresponding .txt file in pages
		page_file = 'static/projects.markdown'
		
		#Try to open the text file, returning a 404 upon failure
		try:
			f = open(page_file, 'r')
		except:
			return web.notfound()
		#read the entire file, converting Markdown content to HTML
		content = f. read()
		content = md.convert(content)
		
		#Render the page.html template using the converted content
		return render.projects( content)
		
		

class login(object):
	def GET(self):
		return render.login()
		
class register(object):
	def GET(self):
		return render.register()
	
class submit(object):
	def GET(self):
		return render.submit()
		

class archive(object):
	def GET(self):
		return render.archive()
		
class about(object):
	"""
		Render the About Me Page
	"""
	def GET(object):
		return render.about()
		
class page:
	def GET(self, url):
		"""
			Get the URL form page request and generate the file
			name based on folder structure.
			Use MarkDown object to convert the *.markdown file to
			html5 content using python MarkDown Package
			
		"""
		title = self.get_page_title(url)
		
		#handle index pages : path/ Maps to path/index.txt
		if url == "" or url.endswith("/"):
			url += "index"
		
		#each URL maps to corresponding .txt file in pages
		page_file = 'static/pages/%s.markdown'%(url)
		
		#Try to open the text file, returning a 404 upon failure
		try:
			f = open(page_file, 'r')
		except:
			return web.notfound()
		#read the entire file, converting Markdown content to HTML
		content = f. read()
		content = md.convert(content)
		
		#Render the page.html template using the converted content
		return render.page(title, content)
	
	def get_page_title(self, url):
		"""
			Get the page title using URL of the page
		"""
		title = url[11:] + " | tssutha.com"
		title = title.replace("-", " ")
		return title
		
		
	
		
	
web.config.debug = False
if __name__ == "__main__":
	app.run()