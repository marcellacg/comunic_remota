import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # Este método é chamado quando uma conexão é estabelecida com o cliente.
        pass

    def on_disconnect(self, conn):
        # Este método é chamado quando uma conexão é encerrada com o cliente.
        pass

    def exposed_sum(self, a, b):
        # Este é um método exposto que pode ser chamado pelo cliente.
        return (a + b) // 2

# Inicie o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MyService, port=18861)
    server.start()