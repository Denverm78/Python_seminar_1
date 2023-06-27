def fir(rows):
    for i in range (0, rows):
        print(" " * (rows - i),"*" * (i * 2 + 1))

user_rows = int(input("Введите количество рядов елочки: "))
fir(user_rows)  