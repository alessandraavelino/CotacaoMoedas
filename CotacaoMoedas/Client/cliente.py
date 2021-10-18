import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 7777))
print("+------------------------+")
print("| Conectado ao servidor. |")
print("+------------------------+")
print("Opções disponíveis: (digitar o formato .arquivo no final)")
print("1 - Dolar")
print("2 - Euro")
print("3 - Bitcoin")

arquivo = str(input("-> " ))
#Ao escolher o arquivo, deve ser definido o caminho da pasta do cliente, para que não seja
#enviada para a pasta raíz "CotacaoMoedas".
arquivo = "C:\\Users\\Alessandra\\Desktop\\CotacaoMoedas-main\\CotacaoMoedas\\Client\\" + arquivo
client.send(arquivo.encode())

with open(arquivo, "wb") as file:
    while True:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f" {arquivo} Recebido na pasta 'Client'")