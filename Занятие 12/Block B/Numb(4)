import math

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

n = int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")