# Hacer enrutador https://www.codewars.com/kata/588a00ad70720f2cd9000005

"""
router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')
router.runRequest('/hello', 'GET') // returns 'hello world'
"""


# Hacer un decorador para POST

# ---> Decoradores para router

# El servidor mas sencillo del mundo

from http.server import SimpleHTTPRequestHandler, HTTPServer

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Imprimir la URL visitada
        print(f"URL visitada: {self.path}")
        
        # Responder al cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f"<html><body><h1>URL visitada: {self.path}</h1></body></html>", "utf8"))

    def do_POST(self):
        # Imprimir la URL visitada
        print(f"URL visitada: {self.path}")
        
        # Leer el contenido del POST
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Datos POST: {post_data.decode('utf-8')}")
        
        # Responder al cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f"<html><body><h1>URL visitada: {self.path}</h1></body></html>", "utf8"))

    # Métodos para PUT, PATCH y DELETE si son necesarios
    def do_PUT(self):
        print(f"URL visitada: {self.path}")
        self.send_response(200)
        self.end_headers()
    
    def do_PATCH(self):
        print(f"URL visitada: {self.path}")
        self.send_response(200)
        self.end_headers()
    
    def do_DELETE(self):
        print(f"URL visitada: {self.path}")
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en el puerto {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    pass#    run()