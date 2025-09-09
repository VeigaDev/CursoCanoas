valor = float(input("Digite o valor em reais: "))
moeda = input("Digite a moeda para conversão (USD/EUR): ").upper()
if moeda == "USD":
    valor_convertido = valor / 5.2
    print(f"O valor em dólares é: ${valor_convertido:.2f}")
elif moeda == "EUR":
    valor_convertido = valor / 6.0
    print(f"O valor em euros é: €{valor_convertido:.2f}")