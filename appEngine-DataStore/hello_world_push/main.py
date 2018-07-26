import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Austin's Online Portal")

app = webapp2.WSGIApplication([
('/main', MainHandler),
],  debug=True)
