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
	
)

app = web.application(urls, globals())
render = web.template.render('templates/',base='layout1')
md = markdown.Markdown(output_format='html5')

class post(object):
	def __init__(self):
		self.date = "21-12-1983"
		self.title = "This is post's title"
		self.summery = "Summery"
		self.filename = ""
	
class post_adap(object):
	def __init__(self):
		self.postList = []
		
	def getposts(self):
		for r,d, f in os.walk('static/pages/'):
			for file in f:
				if not file.startswith('.'):
					pst = post()
					fname,title, dt = self.getpostprops(file)
					pst.date = dt
					pst.title = title
					pst.filename = 'blog/'+ fname
					self.postList.append(pst)
		return self.postList
	
	def getpostprops(self,filename):
		ls = filename.split('.')
		filename = ls[0]
		ls = filename.split('-')
		date = '-'.join(ls[0:3])
		dt = datetime.date(int(ls[0]), int(ls[1]), int(ls[2]))
		title = ' '.join(ls[3:])
		return ( filename, title,dt.__str__())
		
		
	
		


class index(object):
	def GET(self):
		postAdap = post_adap()
		return render.index(postAdap.getposts())

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
	def GET(object):
		return render.about()
		
class page:
	def GET(self, url):
		#handle index pages : path/ Maps to path/index.txt
		if url == "" or url.endswith("/"):
			url += "index"
		
		#each URL maps to corresponding .txt file in pages
		page_file = 'static/pages/%s.markdown'%(url)
		print page_file
		
		#Try to open the text file, returning a 404 upon failure
		try:
			f = open(page_file, 'r')
		except:
			return web.notfound()
		print "2nd "
		#read the entire file, converting Markdown content to HTML
		content = f. read()
		content = md.convert(content)
		
		#Render the page.html template using the converted content
		return render.page(content)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

web.config.debug = True
if __name__ == "__main__":
	app.run()