# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
import requests
from requests.auth import HTTPBasicAuth
from api_recipes import*

import os
import sys
import base64
import ssl
import socketserver
import click

port = 5000



CERT_FILE = os.path.expanduser("~/.ssh/cert.pem")
KEY_FILE = os.path.expanduser("~/.ssh/key.pem")
SSL_CMD = "openssl req -newkey rsa:2048 -new -nodes -x509 " \
          "-days 3650 -keyout {0} -out {1}".format(KEY_FILE, CERT_FILE)

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
    KEY = 'aGVsbG9mcmVzaDp0cnlpbmd0b2dldGFqb2I='
    username = ''
    password = ''

    def __init__(self, request, client_address, server):
        key = '{}:{}'.format(self.username, self.password).encode('ascii')
        self.key = base64.b64encode(key)
        self.valid_header = b'Basic ' + self.key
        super().__init__(request, client_address, server)
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
            self.wfile.write("<html><body><h1>RecipesApi - I'm definitely hired, right? :P</h1></body></html>".encode())


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
def serve_http(ip="", port=80, https=False, start_dir=None, handler_class=RestHTTPRequestHandler):
    """setting up server"""
    print("now starting serve_http")
    httpd = socketserver.TCPServer((ip, port), handler_class)

    if https:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=KEY_FILE,
                                       certfile=CERT_FILE, server_side=True)

    if start_dir:
        print("Changing dir to {cd}".format(cd=start_dir))
        os.chdir(start_dir)

    socket_addr = httpd.socket.getsockname()
    print('Serving "{}" directory on {}://{}:{}'.format(
        os.getcwd(), 'https' if https else 'http', socket_addr[0], socket_addr[1])
    )
    httpd.serve_forever()


@click.command()
@click.argument('username')
@click.argument('password')
@click.argument('ip', default='0.0.0.0')
@click.argument('port', default=port)
@click.option('--https', help='use https', is_flag=True)
@click.option('--dir', help='use different directory')
def main(dir, ip, port, username, password, https):
    """
    Start http server with basic authentication current directory.
    """
    print ("starting main")
    if https and not (os.path.exists(CERT_FILE) and os.path.exists(KEY_FILE)):
        print(file=sys.stderr)
        print("Missing {} or {}".format(CERT_FILE, KEY_FILE), file=sys.stderr)
        print("Run `{}`".format(SSL_CMD), file=sys.stderr)
        print(file=sys.stderr)
        sys.exit(1)

    RestHTTPRequestHandler.username = username
    RestHTTPRequestHandler.password = password
    print("Before serve_http")
    serve_http(ip=ip, port=port, https=https,
               start_dir=dir, handler_class=RestHTTPRequestHandler)


if __name__ == "__main__":
    main()
