import webapp2



class MainPage(webapp2.RequestHandler):		

	def get(self):
		one  = 0
		two = 1
		ans = "0 <hr>1"
		for i in range(8):
			three = one+two
			ans += "<hr>" + str(three)
			one = two
			two = three
		
		self.response.write(ans);


app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
