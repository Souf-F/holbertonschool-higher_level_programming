#!/usr/bin/python3
"""
Simple API server using http.server module.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIRequestHandler(BaseHTTPRequestHandler):
    """Handler for HTTP requests."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def log_message(self, format, *args):
        """Suppress default logging."""
        pass


def run_server(port=8000):
    """Start the HTTP server."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIRequestHandler)
    print(f"Server running on http://localhost:{port}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
