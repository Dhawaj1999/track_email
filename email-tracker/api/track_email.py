from http.server import BaseHTTPRequestHandler
import urllib.parse

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query string to get the email parameter
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        email = params.get('email', [''])[0]

        # Log the email for testing purposes
        print(f"Email opened by: {email}")

        # Send the response headers with CORS support
        self.send_response(200)
        self.send_header("Content-Type", "image/gif")
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow all domains (or specify a domain)
        self.end_headers()

        # Send a 1x1 transparent GIF
        self.wfile.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B')