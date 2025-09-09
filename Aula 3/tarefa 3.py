senha_magica = "abracadabra"

while True:
    senha = input("Digite a senha: ")
    if senha != senha_magica:
        print("Senha incorreta! Tente novamente.")
        continue  # Solicita novamente
    else:
        print("Acesso concedido!")
    break