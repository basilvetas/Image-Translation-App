#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Columbia University
COMS 4995 - Machine Learning Products (Fall 2017)
Image Translation App
"""

import tornado.ioloop
import tornado.web
import requests

import time # for async tests
import pprint

from config import API_KEY


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        q = self.get_arguments('q') # list of strings (even if one string sent as input by client)
        source = self.get_argument('source')
        target = self.get_argument('target')

        print('[GET]\t Arguments: \n\t\tq: %s, \n\t\tsource: %s, \n\t\ttarget: %s' % (q, source, target))

        url = 'https://translation.googleapis.com/language/translate/v2'

        data = {
          'q': q, # string or list of strings
          'source': source,
          'target': target,
          'format': 'text', # HTML or plain text
          'key': API_KEY
        }

        r = requests.post(url=url, data=data)
        response = r.json()
        print('[GET]\t Response: \n\t\t', pprint.pformat(response))

        # time.sleep(5)
        self.write(response)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5001)
    tornado.ioloop.IOLoop.current().start()
