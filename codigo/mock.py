import requests

# GET

url = "https://stoic.tekloon.net"
endpoint = "/stoic-quote"
respuesta = requests.get(url + endpoint)
datos = respuesta.json()["data"]
print(datos)
print("---")
print(f"{datos["author"]} dijo:\n{datos["quote"]}")

# GET con API KEY
print("\n---\n")

api_key = "a7ade0cd9e5c493ca8cf74a5b3fc0790"
url = "http://data.fixer.io/api"
endpoint = "/2022-07-05"  # año-mes-dia
params = {
    "access_key": api_key,
    "base": "EUR",
    "symbols":"JPY, USD, CAD"  # Esto esta raro...
}
respuesta = requests.get(url + endpoint, params=params)
tasas = respuesta.json()["rates"]
print(tasas)

# POST
print("\n---\n")

url = "https://jsonplaceholder.typicode.com"
endpoint = "/posts"
body = {
    "title": 'The incredible test',
    "body": 'This is a testy test!',
    "userId": 666,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
respuesta = requests.post(url + endpoint, json=body, headers=headers)

# PUT

print("\n---\n")

url = "https://jsonplaceholder.typicode.com"
endpoint = "/posts"
element = "/1"
body = {
    "id": 1,
    "title": 'The incredible test',
    "body": 'This is a testy test!',
    "userId": 1,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
respuesta = requests.put(url + endpoint + element, json=body, headers=headers)

# PATCH

print("\n---\n")

url = "https://jsonplaceholder.typicode.com"
endpoint = "/posts"
element = "/1"
body = {
    "title": 'The incredible test returned!',
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
respuesta = requests.patch(url + endpoint + element, json=body, headers=headers)

# DELETE

print("\n---\n")

url = "https://jsonplaceholder.typicode.com"
endpoint = "/posts"
element = "/1"
respuesta = requests.delete(url + endpoint + element)

# Ejercicio ---> reqres.in

url = "https://reqres.in/api"
endpoint = "/users"
_id = "/4"

## Consumir los nombres y apellidos de algunos usuarios

## Consumir los emails de los usuarios de la segunda pagina

## Consumir el avatar del usuario con id 4

## Crear un usuario nuevo

## Cambiar ese usuario con PUT

## Cambiar ese usuario con PATCH

## Eliminar el usuario con id 2

## Eliminar nuestro usuario

