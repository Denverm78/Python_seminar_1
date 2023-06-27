# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
# print(num)
count = 10
print("Компьютер загадал число от 0 до 1000.")
print("Попробуй угадать за 10 попыток.")

for i in range (1, 11):
    user_number = int(input(f'Попытка №{i}:'))
    if user_number < 0 or user_number > 1000:
        print("Ты ввел недопустимое число. Будь внимательнее. Запусти игру еще раз.")
        exit()
    elif user_number == num:
        print("Молодец! Угадал! Возьми с полки пирожок!")
        exit()
    elif user_number > num:
        print("Не угадал. Число компьютера меньше.")
    elif user_number < num:
        print("Не угадал. Число компьютера больше.")
print("Число компьютера было", num)
print("Не переживай, в следующий раз получится!")
        

