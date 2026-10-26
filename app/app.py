from http.server import BaseHTTPRequestHandler, HTTPServer
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello GitOps! Version: 1.11")

HTTPServer(('0.0.0.0', 8080), MyHandler).serve_forever()
