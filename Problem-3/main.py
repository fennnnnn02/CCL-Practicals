import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		i=10
		while(i!=0):
			i -= 1
			self.response.write("33359<br>")
			self.response.write("Information Technology<hr>")

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
