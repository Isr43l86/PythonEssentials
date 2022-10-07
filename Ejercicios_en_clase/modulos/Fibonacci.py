def fibFunction(num):
    fibonacciList = []
    fibonacciList.append(0)
    fibonacciList.append(1) 
    cont = 2
    while (fibonacciList[len(fibonacciList)-1] != num):
        if (fibonacciList[cont-1] + fibonacciList[cont-2] > num):
            break
        fibonacciList.append(fibonacciList[cont-1] + fibonacciList[cont-2])
        cont = cont + 1
    print(fibonacciList)
    return fibonacciList