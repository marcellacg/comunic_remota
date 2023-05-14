import Pyro4
from remote_object import RemoteObject

remote_obj = RemoteObject()

daemon = Pyro4.Daemon()
uri = daemon.register(remote_obj)

print("URI do objeto remoto:", uri)

daemon.requestLoop()
