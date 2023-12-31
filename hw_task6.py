# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# На семинаре был ускоренный вариант, я решил сделать просто классический перебор со счетчиком для разнообразия

def check_number(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    if counter > 2:
        print("Число", number, "составное")
    else:
        print("Число", number, "простое")

while True:
    user_number = int(input("Введите число от 1 до 100000: "))
    if user_number > 0 and user_number < 100000: break

check_number(user_number)
