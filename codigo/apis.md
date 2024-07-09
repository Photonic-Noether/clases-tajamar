# Introducción a HTTP: APIs y programando internet

Una API (Interfaz de Programación de Aplicaciones, por sus siglas en inglés) es un conjunto de reglas y protocolos que permite a diferentes aplicaciones **comunicarse entre sí**. Las APIs definen los métodos y datos que pueden ser intercambiados, facilitando la integración de servicios y la automatización de procesos.

Utilizar (o *consumir*) una API **es agnóstico de lenguaje**, ya que se estan intercambiando datos en un *standart conocido, llamado JSON*.

Existen varias **arquitecturas de APIs**, inicialmente se utilizaba SOAP, pero fue un desastre.

La mayoría de APIs hoy en dia son **APIs REST** (Representational State Transfer) es un estilo arquitectónico para diseñar servicios web. REST se basa en un conjunto de principios y restricciones que utilizan los métodos HTTP para interactuar con los recursos del servidor, y sigue una serie de convenciones y patrones que se consideran buenas prácticas. Las APIs REST **bien diseñadas** son cómodas de utilizar y representan la segunda forma de intercambiar datos y comportamiento de un software (la primera siendo importar módulos y paquetes).

RESTful es un término que se usa para describir una API que cumple con los principios de la arquitectura REST. Cuando una API se describe como RESTful, significa que sigue las normas y restricciones establecidas por REST para la interacción entre el cliente y el servidor.

## REST y sus principios

Los principios REST son:

1. Cliente-Servidor: La arquitectura REST separa las responsabilidades entre el cliente (que solicita recursos) y el servidor (que los proporciona)
2. Stateless (Sin estado): Cada solicitud del cliente al servidor debe contener toda la información necesaria para entender y procesar la solicitud. El servidor no guarda estado de cliente entre las solicitudes, aunque puede (y suele) tener una base de datos asociada
3. Cacheable: Las respuestas deben ser marcadas como cacheables o no, para mejorar la eficiencia y el rendimiento del sistema
4. Uniform Interface (Interfaz Uniforme): La interacción entre el cliente y el servidor se debe hacer a través de una interfaz uniforme, facilitando la comprensión y la utilización de los recursos. Aqui el standart es JSON, pero algunos sistemas legacy utilizarán XML
5. Layered System (Sistema por Capas): La arquitectura REST puede estar compuesta por capas que no afecten la funcionalidad del sistema. Una de las más conocidas es MVC, pero hay más
6. Code on Demand (Código bajo demanda): Opcionalmente, los servidores pueden enviar código ejecutable al cliente para extender su funcionalidad

Además, las APIs RESTful suelen tener las características adicionales:

* Recursos Identificados por URIs: Los recursos (datos o servicios) se identifican mediante URLs. Cada recurso tiene una URI (Identificador Uniforme de Recursos) única. Ejemplo: `https://api.ejemplo.com/usuarios/1414`
* Uso de Métodos HTTP: Las acciones sobre los recursos se realizan utilizando los métodos HTTP estándar. Ejemplo `GET /usuarios/1414`
* Uso de HATEOAS (Hypermedia as the Engine of Application State): Las respuestas del servidor pueden contener hipervínculos que indican las posibles acciones que el cliente puede realizar a continuación. Esto permite que el cliente navegue por la API sin conocer de antemano la estructura completa de la API
* Uso de OpanAPI/Swagger: El standart de documentación OpenAPI se utiliza para documentar **endpoints** e, incluso, para mandar peticiones en un entorno controlado. Esta documentación suele ser bastante adecuada y automáticamente generada. `https://libretranslate.com/docs/`

## Verbos, acciones o métodos HTTP

### GET: Recuperar información de un recurso

```
GET /usuarios/123 HTTP/1.1
Host: api.ejemplo.com
Accept: application/json
```

```json
{
    "id": 123,
    "nombre": "John Doe",
    "email": "john.doe@ejemplo.com"
}
```

### POST: Crear un nuevo recurso

```json
POST /usuarios HTTP/1.1
Host: api.ejemplo.com
Accept: application/json

{
    "nombre": "Jane Doe",
    "email": "jane.doe@ejemplo.com"
}
```

```
HTTP/1.1 201 Created
Location: /usuarios/124
```

Las peticiones POST también pueden devolver un JSON, por ejemplo, si lo que se esta haciendo es una query. SIn embargo, tanto GET como POST pueden utilizar **query parameters (parametros query)**

### PUT: Actualizar un recurso existente

```json
PUT /usuarios/123 HTTP/1.1
Host: api.ejemplo.com
Accept: application/json

{
    "nombre": "John Smith",
    "email": "john.smith@ejemplo.com"
}
```

```
HTTP/1.1 200 OK
```

### PATCH: Actualizar parcialmente un recurso existente

```json
PATCH /usuarios/123 HTTP/1.1
Host: api.ejemplo.com
Accept: application/json

{
    "email": "smith.john@nuevo.com"
}
```

```
HTTP/1.1 200 OK
```

### DELETE: Eliminar un recurso

```
DELETE /usuarios/123 HTTP/1.1
Host: api.ejemplo.com

```

```
HTTP/1.1 204 No Content
```

## Ejemplo de HATEOAS

```
GET /usuarios/123 HTTP/1.1
Host: api.ejemplo.com
Accept: application/json
```

```json
{
    "id": 123,
    "nombre": "John Smith",
    "email": "smith.john@ejemplo.com",
    "links": [
        {
            "rel": "self",
            "href": "/usuarios/123"
        },
        {
            "rel": "datos",
            "href": "/usuarios/123/datos"
        },
        {
            "rel": "update",
            "href": "/usuarios/123",
            "method": "PUT"
        },
        {
            "rel": "delete",
            "href": "/usuarios/123",
            "method": "DELETE"
        }
    ]
}
```

## Parámetros de query

Los parámetros query se utilizan para pasar datos a través de la URL en una solicitud GET. Estos parámetros son útiles para filtrar, ordenar o limitar los resultados de una solicitud.

Se tiene el host `https://api.example.com` y se quiere consultar el endpoint `/productos`, además, que sean productos de electrónica y que se ordenen por orden ascendente, y mostrar solo los 10 primeros.

`https://api.example.com/products?category=electronics&sort=price_asc&limit=10`

* **category** filtra por categoria, en este caso electrónica
* **sort** ordena de acuerdo a un valor del recurso
* **limit** limita la busqueda a un numero determinado (esto se llama paginar)

## Códigos de respuesta

Cada petición obtiene una respuesta del servidor, a menos que la conexión no llegue o sea un servidor especial (en ese caso, se tendrá un timeout). No todas las respuestas tienen un payload, pero todas las respuestas tienen un **código de status** que indica como fue la conexión.

* 1xx información – la petición ha llegado con exito, continuando...
* 2xx exito – la peticiñon llegó con exito, fue aceptada y procesada
* 3xx redireccion – se necesitan realizar acciones extra para esta petición
* 4xx error en cliente – la petición contiene algo que no permite que sea procesada
* 5xx error en servidor – el servidor ha fallado en proporcionar una respuesta a una petición aparentemente válida

Y por supuesto, se estudian estos códigos con gatos: [https://http.cat/](https://http.cat/)

## Otras arquitecturas de API

Además de REST, existen varios otros protocolos y estilos para diseñar APIs:

* SOAP (Simple Object Access Protocol):
    * Descripción: Es un protocolo basado en XML para intercambiar información estructurada en la implementación de servicios web.
    * Características: Especifica reglas estrictas para la mensajería y puede ser utilizado con varios protocolos de red, como HTTP, SMTP y más.
    * Ejemplo: Servicios web de algunas empresas financieras que requieren alta seguridad y transacciones complejas.

* GraphQL:
    * Descripción: Es un lenguaje de consulta para APIs que permite a los clientes solicitar exactamente los datos que necesitan.
    * Características: Los clientes pueden especificar la forma exacta de la respuesta, lo que puede reducir el uso de ancho de banda y mejorar la eficiencia.
    * Ejemplo: APIs de Facebook, GitHub y Shopify.

* gRPC (gRPC Remote Procedure Call):
    * Descripción: Es un marco de trabajo de RPC desarrollado por Google que utiliza Protocol Buffers (protobuf) como su lenguaje de definición de interfaz.
    * Características: Ofrece comunicación eficiente y escalable entre servicios en diferentes lenguajes de programación.
    * Ejemplo: Servicios internos de Google y otros microservicios modernos.

## Métodos auth

Las APIs utilizan diferentes métodos de autenticación para garantizar que solo los usuarios autorizados puedan acceder a los recursos. Estos métodos permiten identificar a un usuario, de forma que pueda acceder a sus recursos.

### API Key Authentication

Se utiliza una clave API (API Key) para autenticar las solicitudes. La clave se incluye en la solicitud HTTP, generalmente en los encabezados o como un parámetro de consulta.

```python
import requests

url = "https://api.ejemplo.com/endpoint"
headers = {
    "Authorization": "Bearer API_KEY"
}

response = requests.get(url, headers=headers)
```

Y en vez de mandarlo en headers se puede mandar como parametro de consulta (param)

### Basic Authentication

Se envían las credenciales (nombre de usuario y contraseña) en el encabezado de la solicitud HTTP, codificadas en base64.

```python
import requests
from requests.auth import HTTPBasicAuth

url = "https://api.ejemplo.com/endpoint"
auth = HTTPBasicAuth(<usuario: str>, <contraseña: str>)

response = requests.get(url, auth=auth)
```

### Bearer Token Authentication

Se envía un token de acceso en el encabezado de autorización de la solicitud HTTP.

```python
import requests

url = "https://api.ejemplo.com/endpoint"
headers = {
    "Authorization": "Bearer TOKEN"
}

response = requests.get(url, headers=headers)
```

### JWT (JSON Web Token)

JWT se utiliza para compartir información de manera segura entre dos partes. Los tokens JWT son autodescriptivos y pueden contener información adicional en sus "claims".

```python
import jwt
import datetime
import requests

secret_key = <SECRET_KEY: str>
payload = {
    "user_id": "123",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}
token = jwt.encode(payload, secret_key, algorithm="HS256")

url = "https://api.ejemplo.com/endpoint"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)
```

### Oauth 2.0

OAuth 2.0 es un protocolo de autorización que permite a las aplicaciones obtener acceso limitado a los recursos del usuario en un servidor.

```python
import requests

url = "https://auth.ejemplo.com/oauth/token"
data = {
    "grant_type": "client_credentials",
    "client_id": <CLIENT_ID: str>,
    "client_secret": <CLIENT_SECRET: str>
}
response = requests.post(url, data=data)
token = response.json()["token"]

url = "https://api.ejemplo.com/endpoint"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)
```

### TLS (Auth mutuo)

Utiliza certificados digitales para autenticar tanto al cliente como al servidor.

```python
import requests

url = "https://api.ejemplo.com/endpoint"
cert = (<path_cert_pem: str>, <path_key_pem: str>)

response = requests.get(url, cert=cert)
```

## Autenticación VS autorización

Autenticar a un usuario **no significa que ese usuario tenga todos los accesos**. A veces, tenemos un error 403, indicando que el usuario se ha autenticado correctamente, *pero no tiene permisos para acceder a ese recurso*.

## Cliente REST VS Servidor

Un cliente REST es aquel que **consume** una API RESTful, mientas que un **servidor** es quien expone las APIs a los clientes.
