def f():
    sum=0
    count=0
    n=int(input())
    while n!=0:
        sum+=n
        count+=1
        n=int(input())
    if count > 0:
        sredn = sum/count
        return sredn
    else:
        return "Нет введенных чисел"
sredn = f()
print(sredn)