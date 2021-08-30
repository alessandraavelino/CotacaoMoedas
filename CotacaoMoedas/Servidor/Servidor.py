import socket
import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL'] ['bid']
cotacao_euro = cotacoes['EURBRL'] ['bid']
cotacao_bitcoins= cotacoes['BTCBRL'] ['bid']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7777))

print('Esperando conexão! \n')

server.listen(10)

connection, address = server.accept()

namefile = connection.recv(1024).decode()


print("O cliente não deseja mais utilizar os serviços... Encerrando conexão!")