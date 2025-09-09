idade = int(input("Digite sua idade: "))
vip = input("Você é VIP? (s/n): ").lower()

if idade > 18 and vip == 's':
    print("Entrada liberada para a área VIP.")
elif idade > 18 and vip == 'n':
    print("Entrada liberada para a área comum.")
elif idade <= 18:
    print("Entrada proibida para menores de 18 anos.")