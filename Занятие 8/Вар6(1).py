def NOD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def NOK(a, b):
    return abs(a * b) // NOD(a, b)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
NOD_ab = NOD(a, b)
NOK_ab = NOK(a, b)
print("НОД:", NOD_ab)
print("НОК:", NOK_ab)
