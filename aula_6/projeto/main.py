from flask import Flask
from http import HTTPStatus
import requests
import json


app = Flask(__name__)


# READ
@app.get("/get_info")
def get_info():
    """Essa função lê o banco de dados de informações do cavalo"""
    with open("db.json", "r") as arquivo:
        arquivo = json.load(arquivo)
        return arquivo


# UPDATE
@app.post("/<string:cep>")
def save_info(cep):
    """Essa função atualiza o banco de dados"""
    info_coletada = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    with open("db.json", "w") as arquivo:
        json.dump(info_coletada.json(), arquivo, indent=4)
    return {"msg": "Endereço salvo com sucesso"}


app.run(port=5050)
