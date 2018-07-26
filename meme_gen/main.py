# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from google.appengine.api import urlfetch
import json
import urllib
import random
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

class MemeTemp(webapp2.RequestHandler):
    def get(self):
        memes_dictionary_2 = {'memes': [{'id': 'mc', 'name': 'austinaustin'}, {'id': 'mc2', 'name': 'mcryan'}]}
        self.response.write('MEME MEME MEME')
        template = template_env.get_template('templates/home.html')
        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                json_dict = json.loads(result.content)
                random_meme = (json_dict['data']['memes'])
                meme_names={}
                count =0

                for meme in random_meme:
                    meme_names[count]=meme['name']
                    count+= 1
                self.response.write(template.render({'meme_names': meme_names}))


        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

        # self.response.write(template.render(memes_dictionary_2))


class MemeTempResult(webapp2.RequestHandler):
    def post(self):
        meme_type = self.request.get('meme-type')
        self.response.write('My post handler - your meme was {meme_type}'.format(meme_type = meme_type)),


class MemePrint(webapp2.RequestHandler):
    def post(self):
        value2= self.request.get('user-second-ln')
        value = self.request.get('user-first-ln')
        meme_print = self.request.get('meme-type')
        meme_dictionary = {'f_line': value, 'z_line': value2}
        template = template_env.get_template('templates/meme_result.html')

        self.response.headers['Content-Type'] = 'text/html'

        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                json_dict = json.loads(result.content)
                random_meme =(json_dict['data']['memes'])[int(meme_print)]['id']

            else:
                self.response.status_code = result.status_code


        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
            'template_id': random_meme,
            'username': 'austin1234',
            'password': 'austin1234',
            'text0': value,
            'text1': value2,}
        result = urlfetch.fetch(
            url=caption_url,
            payload=urllib.urlencode(caption_dict),
            method=urlfetch.POST)

        new_meme_dict = json.loads(result.content)['data']['url']
        self.response.write('<img src = "{pic}"/>'.format(pic=new_meme_dict))



class Recipes(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/home.html')
        recipe = {'ingredients': ['ginger', 'garlic', 'salt', 'pepper','pineapple'],
                  'cuisine': 'nixonian'}
        self.response.write(template.render(recipe))


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        random_text = ['piggy eats bacon', 'he cries cheese']
        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                json_dict = json.loads(result.content)
                random_meme = random.choice(json_dict['data']['memes'])['id']

            else:
                self.response.status_code = result.status_code


        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
            'template_id': random_meme,
            'username': 'austin1234',
            'password': 'austin1234',
            'text0': random.choice(random_text),
            'text1': random.choice(random_text),}
        result = urlfetch.fetch(
            url=caption_url,
            payload=urllib.urlencode(caption_dict),
            method=urlfetch.POST)

        new_meme_dict = json.loads(result.content)
        picture_url = new_meme_dict['data']['url']
        self.response.write('<img src = "{pic}"/>'.format(pic=picture_url))
        self.response.write(result.content)
# class ProfilePage(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers['Content-type'] = 'text/plain'
#         self.response.write('This is your profile page!')
#
# class WelcomePage(webapp2.RequestHandler):
#     def get(self):
#         name = self.request.get('name')
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('Welcome {name} to your welcome page!'.format(name =name))
#
# class SecretPage(webapp2.RequestHandler):
#     def get(self):
#         password = self.request.get('password')
#         self.response.headers['Content-type'] = 'text/plain'
#         self.response.write('Welcome to the super super secret web page. Your Password: {password} has been confirmed.'.format(password=password))
#
# class FizzBuzz(webapp2.RequestHandler):
#     def get(self):
#         number = self.request.get('number')
#         number = int(number)
#         txt = ""
#         if number % 3 == 0 and number %5 != 0:
#             txt= 'fizz'
#         if number % 5 == 0 and number %3 != 0:
#             txt = 'buzz'
#         if number % 3 == 0 and number %5 == 0:
#             txt = 'FizzBuzz'
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('Result: {txt}'.format(txt= txt))

app = webapp2.WSGIApplication([
('/main.*', MainPage),
('/meme_temp', MemeTemp),
('/recipes', Recipes),
# ('/meme_result', MemeTempResult),
('/meme_meme', MemePrint),
# ('/profile.*', ProfilePage),
# ('/welcome.*',WelcomePage),
# ('/secret.*', SecretPage),
# ('/fizzbuzz.*', FizzBuzz)
], debug = True)
