# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
import requests
from requests.auth import HTTPBasicAuth
from api_recipes import*

import argparse
import base64
import os
import ssl
import sys


port = 5000
###----------------------------------------- AUTHENTICATION -----------------------------------------####
USERS = [
{"username": "recipesapi", "password":"manchesterunited"},
{"username": "fungai", "password":"gotitinone"},
{"username": "fungaithetankengine", "password":"ithinkicanithinkican"},
]

def validating(self):
    ''' Present frontpage with user authentication. '''
    auth_header = self.headers.get('Authorization', '').encode('ascii')
    validated = False

    for x in USERS:
        usernamex = x["username"]
        print (usernamex)
        passwordx = x["password"]
        print (passwordx)
        key = '{}:{}'.format(usernamex,passwordx).encode('ascii')
        self.key = base64.b64encode(key)
        self.valid_header = b'Basic ' + self.key
        if auth_header == self.valid_header:
            header=self.headers.get('Authorization')
            validated = True
            return True
    print(validated)

def authentication(self):
    auth_header = self.headers.get('Authorization', '').encode('ascii')
    if auth_header is None:
        self.do_AUTHHEAD()
        header=self.headers.get('Authorization')
        self.wfile.write(b'no auth header received')
        return False
    elif validating(self)==True:
        header=self.headers.get('Authorization')
        return True
    else:
        self.do_AUTHHEAD()
        header=self.headers.get('Authorization')
        self.wfile.write(auth_header)
        self.wfile.write(b'not authenticated')
        return False
###----------------------------------------- Request Handler -----------------------------------------####
class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    ''' Main class to present webpages and authentication. '''
    KEY = ''

    #URL Mapping for VERB requests
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        print ("send header")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        print ("send header")
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        url = self.path
        recipe_id = url.split('/')[-1]

        if self.path == '/recipes':
            list_recipes(self)
        elif self.path == ('/recipe/%s' % recipe_id):
            recipe_get(self, recipe_id)
        else:
            self._set_headers()
            self.wfile.write("<html><body><h1>Hello Fresh - I'm definitely hired, right? :P</h1></body></html>".encode())

    def do_POST(self):
        url = self.path
        recipe_id = url.split('/')[-1]
        id_search = url.split('/')[-2]
        if self.path == '/recipes':
            if authentication(self):
                add_recipe(self)
        elif self.path == ('/recipe/%s/rating' % id_search):
            rate_recipe(self, id_search)
        elif self.path == ('/search/'):
            search_get(self)

    def do_PUT(self):
        url = self.path
        recipe_id = url.split('/')[-1]
        if self.path == ('/recipe/%s' % recipe_id):
            if authentication(self):
                update_recipe(self, recipe_id)

    def do_PATCH(self):
        url = self.path
        recipe_id = url.split('/')[-1]
        if self.path == ('/recipe/%s' % recipe_id):
            if authentication(self):
                update_recipe(self, recipe_id)

    def do_DELETE(self):
        url = self.path
        recipe_id = url.split('/')[-1]
        if self.path == ('/recipe/%s' % recipe_id):
            if authentication(self):
                recipe_delete(self, recipe_id)


###----------------------------------------- START SERVER -----------------------------------------####
httpd = HTTPServer(('0.0.0.0', port), RestHTTPRequestHandler)
print ('Started httpserver on port ', port)
while True:
 httpd.handle_request()
