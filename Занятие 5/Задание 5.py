def schet():
    count = 0
    n = int(input())
    while n != 0:
        count += 1
        n = int(input())
    return count
count=schet()
print(count)