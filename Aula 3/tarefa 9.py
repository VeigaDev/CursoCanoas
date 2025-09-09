input_year = input('Digite um ano para verificar se é bissexto: ')
year = int(input_year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é bissexto!')
else:
    print(f'O ano {year} não é bissexto!')