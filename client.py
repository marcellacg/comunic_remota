import Pyro4

uri = input("Insira a URI do objeto remoto: ")

remote_obj = Pyro4.Proxy(uri)

nome = input("Insira seu nome: ")
opt = input(''' SUAS OPÇÕES:
                    1. PARA GERAR SENHA ALEATÓRIA
                    2. PARA RECEBER FRASE MOTIVACIONAL
                    3. PASSO-A-PASSO DE COMO FAZER OVO COZIDO
''')

print(remote_obj.greet_person(nome))
print(remote_obj.opcao(opt))
