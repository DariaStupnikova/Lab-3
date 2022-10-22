'''Беру очевидно антидот аптечку еду арбалет и ингалятор'''

backpack = [['' for _ in range(2)] for _ in range(4)]
backpack[0][0] = 'и'
backpack[0][1] = 'д'
backpack[1][0] = 'a'
backpack[1][1] = 'a'
backpack[2][0] = 'к'
backpack[2][1] = 'к'
backpack[3][0] = 'н'
backpack[3][1] = 'o'
print(*backpack, end='\n')
summ = 20*2 + 15*2 + 25 + 10
minu = 25 + 15 + 20 + 15 + 20
print('Общая сумма очков:', summ - minu)

#не, ну технически тз я выполнила...)) (прога с дп будет позже)