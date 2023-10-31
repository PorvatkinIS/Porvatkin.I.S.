def f() -> int:
    currentLength = maxLength = predNumber = 0
    currentNumber = int(input())
    while currentNumber != 0:
        if currentNumber == predNumber:
            currentLength += 1
        else:
            predNumber = currentNumber
            maxLength = max(currentLength, maxLength)
            currentLength = 1
        currentNumber = int(input())
    return max(currentLength, maxLength)

maxLength = f()
print(maxLength)
