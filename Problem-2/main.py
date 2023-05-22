import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		for i in range(5):
			self.response.write(" Name: Parth R <br>")
		        self.response.write(" Rollno: 33359 <br>")
		        self.response.write(" Department: IT <hr>")

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
