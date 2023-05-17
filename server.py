import Pyro4
from remote_object import RemoteObject

remote_obj = RemoteObject()

#Utilizar IP Wifi (testado em Ubuntu em diferentes redes, porém, resultando em time out)
daemon = Pyro4.Daemon(host='192.168.36.138', port=9090)
uri = daemon.register(remote_obj)

print("URI do objeto remoto:", uri)

daemon.requestLoop()