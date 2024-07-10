# El enrutador mas basico del mundo
class Router:
    def __init__(self):
        self.urls = dict()  # Diccionario vacio con las urls (tupla(url, metodo) y funcion)
        
    def guardar(self, url: str, method: str, func):  # Necesitais tres args (no os digo que es cada uno)
        self.urls[(url, method)] = func  # Crea ruta y la junta a una funcion
        
    def ejecutar(self, url: str, method: str):
        try:
            return self.urls[(url, method)]()  # Hago un closure con la tupla (url, metodo) y con eso simplemente ejecuto la funcion
        except KeyError:
            return 'Error 404: Not Found'  # Si no encuentro, devuelvo 404

# Creo el router
router = Router()
# Defino las rutas del router
router.guardar('/hello', 'GET', lambda: 'hello world')
router.guardar('/login', 'POST', lambda: 'Please log-in.')
# Ejecuto cada vista
resultado = router.ejecutar('/hello', 'GET')
print(resultado)
resultado = router.ejecutar('/login', 'POST')
print(resultado)


# Las rutas SUELEN estar como decoradores (Pero NO en Django!!)

def get(ruta: str):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Esto es un GET request desde {ruta}")  # Aqui tendria mi lambda y mi logica de programacion
            ...  # Aqui va mi logica
            return func(*args, **kwargs)
        return wrapper
    return decorador

def post(ruta: str):
    def decorador(func):
        def wrapper(*args, **kwargs):
            ...  # Aqui va logica
            return func(*args, **kwargs)
        return wrapper
    return decorador

def put(ruta: str):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Esto es un PUT request desde {ruta}")
            ...  # Aqui va mi logica
            return func(*args, **kwargs)
        return wrapper
    return decorador

def patch(ruta: str):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Esto es un PATCH request desde {ruta}")
            ...  # Aqui va mi logica
            return func(*args, **kwargs)
        return wrapper
    return decorador

def delete(ruta: str):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Esto es un DELETE request desde {ruta}")
            ...  # Aqui va mi logica
            return func(*args, **kwargs)
        return wrapper
    return decorador

@get("/hola")
def hola_mundo():
    return 200, "<p>Hola mundo!</p>"

@post("/login")
def crear_usuario(data):
    return 201, f"Usuario creado con datos {data}!"

@put("<ruta>")
def cambiar_usuario(data):
    return 200, f"Usuario modificado con datos {data}!"

@patch("<ruta>")
def cambiar_parte_usuario(data):
    return 200, f"Usuario modificado con datos {data}!"

@delete("<ruta>")
def eliminar_usuario():
    return 204, f"Usuario eliminado!"

print(hola_mundo())  # Esto es un get
print(crear_usuario({10: "Pepe"}))  # Esto es un post
# Y se puede jugar con el resto sin problemas!



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
    run()