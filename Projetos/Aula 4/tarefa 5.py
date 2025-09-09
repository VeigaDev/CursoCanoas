senha = input('Digite sua senha: ')
if len(senha) < 6:
    print('Senha fraca. Tente uma senha maior.')
elif len(senha) == 6 or len(senha) <= 10:
    print('Senha moderada. Adicione caracteres especiais para mais segurança.')
else:
    print('Senha forte. Excelente!')