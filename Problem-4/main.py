import webapp2

class MainPage(webapp2.RequestHandler):

	def get(self):
		for i in range(1,11):
			res = "5 x "+ str(i) + " = " + str(5*i)+"<hr>"
			self.response.write(res);


app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
