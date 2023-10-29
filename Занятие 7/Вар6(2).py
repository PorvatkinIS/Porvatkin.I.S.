def f(s):
    return sum(elem for elem in s if elem > 5)
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_bolsh_5 = f(s)
print("Сумма элементов, которые больше 5:", sum_bolsh_5)
