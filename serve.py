#!/usr/bin/env python

import sys

from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

port = sys.argv[1] if len(sys.argv) > 1 else 8000
httpd = HTTPServer(('0.0.0.0', port), Handler)

print ("Serving HTTP on port %d" % (port))
httpd.serve_forever()
