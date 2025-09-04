def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if nota < 0 or nota > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
                continue
            return nota
        except ValueError:
            print("Valor inválido! Digite um número.")

nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")
nota3 = ler_nota("Digite a terceira nota: ")

media = (nota1 + nota2 + nota3) / 3

print(f'A média das notas é: {media:.2f}')
if media >= 7:
    print("***********")
    print("Aluno aprovado!")
elif 5 <= media < 7:
    print("***********")
    print("Aluno em recuperação!")
else:
    print("***********")
    print("Aluno reprovado!")