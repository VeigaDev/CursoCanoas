estado = input("Digite o seu estado: ").strip().upper()
valor_compra = float(input("Digite o valor da compra: R$ "))
frete = 25.00
if estado == 'SP' and valor_compra > 200:
    frete = 0.00
    print(f'O valor total da compra é R$ {valor_compra:.2f} e o frete é grátis!')
elif estado == 'RJ':
    frete = 15.00
    print(f'O valor total da compra é R$ {valor_compra + frete:.2f} e o frete é R$ {frete:.2f}.')
else:
    print(f'O valor total da compra é R$ {valor_compra + frete:.2f} e o frete é R$ {frete:.2f}.')