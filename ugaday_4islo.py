# Игра угадай число

import random #Импортируем модуль random что бы вызвать функцию randint()
guessTaken = 0 #Переменная guessTaken хранит кол-во попыток игрока угадать число
print('Привет, как тебя Зовут?:')
myName =input()
number = random.randint(1,20) #Функция randint генерирует случайное число от и до и сохраняет значение в переменной
print('Что ж, ' + myName + ' я загадываю число от 1 до 20.')
for guessTaken in range(6):
    print('Попробуй угадать')
    guess=input()
    guess=int(guess)

    if guess < number:
        print('Твоё число слишком маленькое')

    if guess > number:
        print('Твоё число слишком большое')
    if guess == number:
        break
if guess == number:
    guessTaken = str(guessTaken+1)
    print('Отлично,' +myName+ '! Ты справился за '+ guessTaken + ' попыток(ки)!')
if guess != number:
    number= str(number)
    print('Увы. Я Загадал число' + number + '.')

