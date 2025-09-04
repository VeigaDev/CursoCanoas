idade = int(input("Digite sua idade: "))
classificacao_indicativa = int(input("Digite a classificação indicativa do filme: "))
if idade >= classificacao_indicativa:
    print("Você pode assistir ao filme.")
elif idade < classificacao_indicativa:
    print("Você não pode assistir ao filme.")
else:
    print("Idade ou classificação indicativa inválida.")