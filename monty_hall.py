import random

portas = [1, 2, 3]

vezes_que_sorteou_porta_1 = 0
vezes_que_sorteou_porta_2 = 0
vezes_que_sorteou_porta_3 = 0

for nicolly in range(1000):
    porta_premiada = random.choice(portas)
    if porta_premiada == 1:
        vezes_que_sorteou_porta_1 += 1
    elif porta_premiada == 2:
        vezes_que_sorteou_porta_2 += 1
    elif porta_premiada == 3:
        vezes_que_sorteou_porta_3 += 1

print(f"Porta 1: {vezes_que_sorteou_porta_1}")
print(f"Porta 2: {vezes_que_sorteou_porta_2}")
print(f"Porta 3: {vezes_que_sorteou_porta_3}")