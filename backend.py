from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data_set = {}

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        data_set.update(data)
        with open('data.json', 'w') as f:
            json.dump(data_set, f)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "message": "Data received and saved",
            "data": data
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        with open('data.json', 'r') as f:
            data_set = json.load(f)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data_set).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
