def f():
    count = 0
    pred =int(input())
    while pred != 0:
        sled = int(input())
        if sled > pred:
            count +=1
            pred=sled
    return count
