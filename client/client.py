from socket import *
import pickle


client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 7000))

while True:
    message = input('ВВедите массив строки/числа\n')
    message = pickle.dumps(message)
    client.sendall(message)

    message = client.recv(1024).decode('utf-8')
    message2 = client.recv(1024).decode(('utf-8'))

    print(message)
    print(message2)



