# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def true_false(a1, b1, c1):
    if ((a1 + b1) > c1) and ((a1 + c1) > b1) and ((b1 + c1) > a1):
        print("Треугольник существует")
    else:
        print("Треугольник не существует")
        exit()

def type_identification(a2, b2, c2):
    if a2 == b2 == c2:
        print("Треугольник равносторонний")
    elif (a2 == b2 != c2) or (a2 == c2 != b2) or (b2 == c2 != a2):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")

a = float(input("Введите длину первой стороны треугольника а: "))
b = float(input("Введите длину первой стороны треугольника b: "))
c = float(input("Введите длину первой стороны треугольника c: ")) 
true_false(a, b, c)
type_identification(a, b, c)    