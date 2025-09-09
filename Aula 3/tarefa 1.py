pontuacao = int(input('Digite a pontuação: '))
if pontuacao < 0:
    print("Pontuação inválida! Digite um valor positivo.")
elif pontuacao <= 100:
    print("Você é um iniciante!")
elif pontuacao <= 500:
    print("Você é um aventureiro experiente!")
elif pontuacao <= 1000:
    print("Você é um mestre da aventura!")
else:
    print("Você é uma lenda viva!")

