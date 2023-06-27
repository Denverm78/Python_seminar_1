COND_1 = 4
COND_2 = 100
COND_3 = 400


def check_year(year):
    if year % COND_1 == 0 and year % COND_2 != 0 or year % COND_3 == 0:
        print(year, "год - високосный") 
    else: 
        print(year,"год - невисокосный")
        
use_year = int(input("Введите год для проверки: "))
check_year(use_year)