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
      
      print("----------GOT HERE----------");
      print(json_data);

      print("--------------------");


      words = json_data.get('words') # list of strings (even if one string sent as input by client)
      source = json_data.get('source')
      target = json_data.get('target')

      print('[GET]\t Arguments: \n\t\twords: %s, \n\t\tsource: %s, \n\t\ttarget: %s' % (words, source, target))

      url = 'https://translation.googleapis.com/language/translate/v2'

      data = {
        'q': words, # string or list of strings
        'source': source,
        'target': target,
        'format': 'text', # HTML or plain text
        'key': API_KEY
      }

      r = requests.post(url=url, data=data);
      response = r.json();
      print('[GET]\t Response: \n\t\t', pprint.pformat(response))

      # time.sleep(5)      
      self.write(response)

def make_app():
  return Application([
    (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(5001)
  IOLoop.current().start()
