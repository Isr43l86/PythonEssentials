def isPrime(num):
    cont = 0
    for i in range(1,num,1):
        if (num % i == 0):
            cont += 1
            if cont >= 2:
                return False
    
    if cont > 2:
        return False
    else:
        return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
