gun = ['камень', 'ножница','бумага']
player = gun[int(input('0-камень, 1-ножница, 2-бумага: '))]

#рандомизация инструмента бота

random = set(gun)
bot = list(random)
random = set(bot)
bot = list(random)
botgun = bot[1]


print ('Бот выбрал ' +botgun)

#Условия победы
if player == 'камень':
    if botgun == 'ножница':
         print ('You won')
if player == 'ножница':
    if botgun =='бумага':
        print ('You won')
if player == 'бумага':
    if botgun =='камень':
         print ('You won')
#Условия поражения
if player == 'камень':
    if botgun == 'бумага':
        print ('You lose')
if player == 'ножница':
    if botgun =='камень':
        print ('You lose')
if player == 'бумага':
    if botgun =='ножница':
        print ('You lose')
#Условия ничьи
if player == botgun:
    print ('Ничья')
#Над победой до 3х очков, пока работаю
