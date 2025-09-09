peso = input("Digite seu peso em kg: ")
altura = input("Digite sua altura em metros: ")
imc = float(peso) / (float(altura) ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso.')
elif 18.5 <= imc < 24.9:       
    print(f'Seu IMC é {imc:.2f}. Você está com o peso normal.')
elif 25 <= imc < 29.9:
    print(f'Seu IMC é {imc:.2f}. Você está com sobrepeso.')
elif 30 <= imc < 34.9:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau 1.')
    