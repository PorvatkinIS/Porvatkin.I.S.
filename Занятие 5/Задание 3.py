import math
def f(N):
    stepen=1
    while stepen * 2 <= N:
        stepen *= 2
    return stepen, 2**int(math.log2(stepen))
stepen, pokazatel=f(24)
print(stepen, pokazatel)