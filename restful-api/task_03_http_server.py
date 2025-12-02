#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import sys

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="text/plain; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        path = self.path

        if path == "/" or path == "":
            self._set_headers(200, "text/plain; charset=utf-8")
            self.wfile.write(b"Hello, this is a simple API!")
            return

        if path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(payload).encode('utf-8')
            self._set_headers(200, "application/json; charset=utf-8")
            self.wfile.write(body)
            return

        if path == "/status":
            self._set_headers(200, "text/plain; charset=utf-8")
            self.wfile.write(b"OK")
            return

        if path == "/info":
            self.set_headers(200, "application/json; charset=utf-8")
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            body = json.dumps(payload).encode('utf-8')
            self.wfile.write(body)
            return

        self._set_headers(404, "text/plain; charset=utf-8")
        self.wfile.write(b"Endpoint not found")

def run():
    port = 8000
    server = HTTPServer(("", port), Handler)
    server.serve_forever()

if __name__ == "__main__":
    run()
