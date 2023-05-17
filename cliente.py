import rpyc

# Conecte-se ao servidor
conn = rpyc.connect("192.168.36.142", 18861)

# Divida a soma entre cliente e servidor
def divide_sum(a, b):
    server_result = conn.root.sum(a, b)
    client_result = (a + b) - server_result
    return server_result, client_result

# Chamada de exemplo
server_result, client_result = divide_sum(4, 6)
print("Resultado no servidor:", server_result)  # Saída: 5
print("Resultado no cliente:", client_result)  # Saída: 5

# Encerre a conexão
conn.close()