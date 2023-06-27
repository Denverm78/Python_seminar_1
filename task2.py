TENS = 10
HUNDREDS = 100

while True:    
    user_number = int(input("Введите число от 1 до 999: "))
    if user_number >= 1 and user_number <= 999: break

number = user_number / HUNDREDS
if number >= 1 and number <= 9.99:    
    user_hundred = int(user_number / HUNDREDS)
    user_ten = int ((user_number / TENS) % TENS)
    user_unit = int(user_number % TENS)
    res = user_unit * HUNDREDS + user_ten * TENS + user_hundred             
elif number < 1 and number >= 0.1:        
    first_num = int(user_number / TENS)
    second_num = int(user_number % TENS)
    res = first_num * second_num        
elif number < 0.1 and number >= 0.01:        
    res = user_number ** 2
print("Результат -", res)
exit()

        
    
