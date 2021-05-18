import sys
koloda = [2,3,4,5,6,7,8,9,10,11] * 4
import random
random.shuffle(koloda)
print (" Поиграем в 21")
count1=0
count2=0
current1 = koloda.pop()
count1 += current1
current2 = koloda.pop()
count2 += current2
current1 = koloda.pop()
count1 += current1
current2 = koloda.pop()
count2 += current2
print('У Вас %d' %count1)
print('У Вашего аппонента %d' %count2)
while True:
    choice = input('Игрок1 Будете брать карту? y/n')
    if choice == 'y':
        current1 = koloda.pop()
        print('Вам попалась карта достоинством %d' %current1)
        count1 += current1
        print('У Игрок1 %d очков.' %count1)
        if count1 > 21:
            print('выйграл игрок2')
            sys.exit()
    elif choice == 'n':
        print('У Игрок1 %d очков.' %count1)
        break
if count1 > 21:
    print('выйграл игрок2')
    sys.exit()
while True:
    choice = input('Игрок2 Будете брать карту? y/n')
    if choice == 'y':
        current2 = koloda.pop()
        print('Вам попалась карта достоинством %d' %current2)
        count2 += current2
        print('У Игрок2 %d очков.' %count2)
        if count2 > 21:
            print('выйграл игрок1')
            sys.exit()
    elif choice == 'n':
        print('У Игрок2 %d очков.' %count2)
        break
if count1 == count2:
    print('Ничья')
if count1 > count2:
    print('Выйграл Игрок1')
if count1 < count2:
    print('Выйграл Игрок2')


