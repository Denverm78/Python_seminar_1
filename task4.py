print("                     Таблица умножения")
for i in range(2, 10):
    for j in range(2, 6):
        print(f"{j} х {i} = {i * j}\t", end=" ")
    print()
print()
for i in range(2, 10):
    for j in range(6, 10):
        print(f"{j} х {i} = {i * j}\t", end=" ")
    print(" ")
