import Pyro4
from random import randint

class RemoteObject:
        
    @Pyro4.expose
    def greet_person(self, nome):
        return "Obrigada pela atenção, " + nome + "!"
    
    @Pyro4.expose
    def opcao(self, opt):
        if opt == "1":
            senha = randint(2, 2000)
            return "Aqui está sua senha: " + senha
        elif opt == "2":
            return "Se falam de você pelas costas, é sinal que você tá na frente: continue!"
        else:
            mensagem = '''
                Ponha a água e o ovo na panela, coloque no fogo,
                cozinhe por 10 minutos, desligue, espere esfriar,
                descasque e coma. Sal a gosto.'''
            return mensagem