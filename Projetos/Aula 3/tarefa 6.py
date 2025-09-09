import random

random_number = random(1, 10)
while True:
    guess = int(input("Adivinhe o número entre 1 e 10: "))
    if guess < random_number:
        print("Muito baixo! Tente novamente.")
    elif guess > random_number:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você adivinhou o número!")
        break