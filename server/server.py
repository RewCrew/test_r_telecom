from socket import *
import pickle


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 7000))
server.listen(2)
user, adr = server.accept()

while True:
    data = user.recv(1024)
    data = pickle.loads(data)
    data = eval(data)
    lst = [i for i in data if type(i) is int or type(i) is float]
    middle = (sum(lst)/len(lst)).__round__(2)

    lst_up = sorted(lst)
    lst_up.append(middle)
    lst_down = sorted(lst, reverse=True)
    lst_down.append(middle)

    message1 = f'Список по возрастанию = {lst_up} и среднее арифмитическое = {lst_up[-1]}'.encode('utf-8')
    user.sendall(message1)
    message2 = f'Список по убыванию = {lst_down} и среднее арифмитическое = {lst_down[-1]}'.encode('utf-8')
    user.sendall(message2)
user.close()
