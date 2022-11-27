# Fazer requisições
import requests

# Para criar uma página Web
from flask import Flask

import pprint

print('Digite o seu CEP: ')
cep_client = input(str())

# Retirando espaços no começo e no fim da string
cep_client = cep_client.strip()

if len(cep_client) == 9:
    cep_client = cep_client.replace('-', "")

response = requests.get(f'https://viacep.com.br/ws/{cep_client}/json')
response = response.json()

app = Flask(__name__)

# $ set FLASK_APP=main.py
# $ run flask

@app.get('/')
def return_cep():
    return response