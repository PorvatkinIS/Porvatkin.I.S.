import math

def f(a, b, c, d, diag1, diag2):
    alpha = math.acos((a**2 + c**2 - diag1**2) / (2 * a * c))
    beta = math.acos((b**2 + d**2 - diag1**2) / (2 * b * d))
    return 0.5 * diag1 * diag2 * math.sin(alpha + beta)
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
d = float(input("Введите длину четвертой стороны: "))
diag1 = float(input("Введите длину первой диагонали: "))
diag2 = float(input("Введите длину второй диагонали: "))
area = f(a, b, c, d, diag1, diag2)
print("Площадь четырехугольника:", area)
