import socket
import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL'] ['bid']
cotacao_euro = cotacoes['EURBRL'] ['bid']
cotacao_bitcoins = cotacoes['BTCBRL'] ['bid']

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Conectado!!\n')


while True:
    print("------COTAÇÃO DE MOEDAS--------")
    print("1 - Cotação do Dólar")
    print("2 - Cotação do Euro")
    print("3 - Cotação do Bitcoins")
    print("0 - Não desejo mais utilizar os serviços")

    opt = int(input("Digite a opção desejada: "))

    if(opt == 0):
        print("Fechando conexão!")
        break
    elif (opt == 1):
        print(cotacao_dolar)

    elif (opt == 2):
        print(cotacao_euro)

    elif (opt == 3):
        print(cotacao_bitcoins)
    else:
        print("Informação não localizada.")

