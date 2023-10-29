def f(s):
    count = s.count('a')
    s = s.replace('a', '')
    return count
s= input()
count = f(s)
print(count)
