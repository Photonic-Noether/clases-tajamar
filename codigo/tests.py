import requests

# Esto deberia de ir en fixture
full_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def query(palabra):
    response = requests.get(full_url + palabra)
    return response


# Tests
def test_status_code():
    palabra = "dog"
    response = query(palabra)
    assert response.status_code == 200

def test_palabra():
    palabra = "dog"
    response = query(palabra)
    data = response.json()
    assert data[0]['word'] == palabra
    