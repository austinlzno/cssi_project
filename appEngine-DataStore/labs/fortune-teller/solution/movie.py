from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty(required =True)
    media_type = ndb.StringProperty(required=True, default = 'Movie')
    runtime = ndb.IntegerProperty(required=False)
    rating = ndb.FloatProperty(required=False)

    # def __init__(self, mov_title, runtime, user_rating):
    #     self.title = mov_title
    #     self.runtime = runtime
    #     self.rating = user_rating

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email=ndb.StringProperty(required=True)
    recently_viewed= ndb.StringProperty(required=True)

    # def __init__(self, username, password, email, recently_viewed):
    #     self.user_username = username
    #     self.user_password = runtime
    #     self.user_email = user_rating
    #     self.recently_viewed= recently_viewed
