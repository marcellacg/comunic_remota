import Pyro4
from remote_object import RemoteObject

remote_obj = RemoteObject()

'''Utilizar IP Wifi (testado em Ubuntu em diferentes redes (firewall desligado), porém, 
resultando em [Errno 110] Connection timed out. Até certo ponto eles se enxergam; o server envia
a função, mas na resposta do cliente o servidor não faz o retorno com a resposta esperada.
Em terminais diferentes a comunicação ocorre.)'''

daemon = Pyro4.Daemon(host='192.168.36.138', port=9090)
uri = daemon.register(remote_obj)

print("URI do objeto remoto:", uri)

daemon.requestLoop()