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
      source = json_data.get('source')
      target = json_data.get('target')

      print('[GET]\t Arguments: \n\t\twords: %s, \n\t\tsource: %s, \n\t\ttarget: %s' % (words, source, target))

      url = 'https://translation.googleapis.com/language/translate/v2'

      data1 = {
        'q': words, # string or list of strings
        'source': 'en',
        'target': source,
        'format': 'text', # HTML or plain text
        'key': API_KEY
      }

      r1 = requests.post(url=url, data=data1);
      response1 = r1.json();
      print('[GET]\t Response: \n\t\t', pprint.pformat(response1))

      data2 = {
        'q': words, # string or list of strings
        'source': 'en',
        'target': target,
        'format': 'text', # HTML or plain text
        'key': API_KEY
      }

      r2 = requests.post(url=url, data=data2);
      response2 = r2.json();
      print('[GET]\t Response: \n\t\t', pprint.pformat(response2))

      # time.sleep(5) 
      
      self.write(dict([('source', response1), ('target', response2)]))

def make_app():
  return Application([
    (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(5001)
  IOLoop.current().start()
