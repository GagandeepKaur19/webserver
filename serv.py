Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> from http.server import HTTPServer, BaseHTTPRequestHandler
>>> class Serv(BaseHTTPRequestHandler):
	def do_Get(self):
		if self.path== '/'
		
SyntaxError: invalid syntax
>>> class Serv(BaseHTTPRequestHandler):
	def do_Get(self):
		if self.path== '/':
			self.path == '/index.html'
			try:
				file_to_open = open(self.path[1:]).read()
				self.send_response(200)
			except:
				file_to_open = "file not found"
				self.send_response(404)
				self.end_headers()
				self.wfile.write(bytes(file_to_open,'utf-8'))

	
>>> httpd = HTTPServer(('localhost',8080), Serv)
>>> httpd.serve_forever()
