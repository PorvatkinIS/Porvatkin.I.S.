def f(x, y):
    days=1
    while x<y:
        x *=1.1
        days +=1
    return days
print(f(19,30))