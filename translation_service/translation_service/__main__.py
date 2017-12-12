#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Columbia University
COMS 4995 - Machine Learning Products (Fall 2017)
Image Translation App
"""

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.web import RequestHandler
import requests
import json
import time # for async tests
import pprint

from config import API_KEY


class MainHandler(RequestHandler):    
    def set_default_headers(self):
      super(MainHandler, self).set_default_headers()
      self.set_header('Access-Control-Allow-Origin', 'http://localhost:8080')
      self.set_header('Access-Control-Allow-Credentials', 'true') 
      self.set_header('Content-Type', 'application/json')

    def post(self):      
      print(self.request.body);
      json_data = json.loads(self.request.body);
      words = json_data.get('words') # list of strings (even if one string sent as input by client)
      lang1 = json_data.get('lang1')
      lang2 = json_data.get('lang2')

      print('[GET]\t Arguments: \n\t\twords: %s, \n\t\tsource: %s, \n\t\ttarget: %s' % (words, lang1, lang2))

      url = 'https://translation.googleapis.com/language/translate/v2'

      if not(lang1 == 'en'):
        data1 = {
          'q': words, # string or list of strings
          'source': 'en',
          'target': lang1,
          'format': 'text', # HTML or plain text
          'key': API_KEY
        }
        r1 = requests.post(url=url, data=data1).json();
        response1 = [val['translatedText'] for val in r1['data']['translations']];
        print('[GET]\t Response: \n\t\t', pprint.pformat(response1))
      else:
        response1 = words;

      if not(lang2 == 'en'):
        data2 = {
          'q': words, # string or list of strings
          'source': 'en',
          'target': lang2,
          'format': 'text', # HTML or plain text
          'key': API_KEY
        }
        r2 = requests.post(url=url, data=data2).json();
        response2 = [val['translatedText'] for val in r2['data']['translations']];
        print('[GET]\t Response: \n\t\t', pprint.pformat(response2))
      else:
        response2 = words;

      # time.sleep(5) 

      print('Words: \n\t\t', pprint.pformat(words))
      
      self.write(dict([('lang1', response1), ('lang2', response2)]))

def make_app():
  return Application([
    (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(5001)
  IOLoop.current().start()
