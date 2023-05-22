import webapp2
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):

	def get(self):
		temp = {}
		self.response.write(template.render("./template/index.html",temp))
	
	
	def post(self):
		lat = self.request.get('latitude')
		lon = self.request.get('longitude')
		
		url = "https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&current_weather=true"
		data = urllib.urlopen(url).read()
		data = json.loads(data)
		
		
		if(data['error']):
			self.response.write("<h1>ERROR</h1>")
		else:
			self.response.write(data)
		
app = webapp2.WSGIApplication([('/',MainPage)], debug=True)
