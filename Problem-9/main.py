import urllib
import json
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	
	def get(self):
		temp = {}
		self.response.write(template.render("./template/index.html",temp))
	
	def post(self):
		url = "http://universities.hipolabs.com/search?name=" + self.request.get('uni')+"&country=" + self.request.get('country')
		data = urllib.urlopen(url).read()
		data = json.loads(data)
		
		if(len(data)!=0):
			uni = data[0]['name']
			web = data[0]['web_pages'][0]
			temp = {"uni":uni, "web":web}
			self.response.write(template.render("./template/results.html",temp))
		else:
			temp = {}
			self.response.write(template.render("./template/error.html",temp))

app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
		
