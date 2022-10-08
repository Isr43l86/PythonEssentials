def l100kmtompg(liters):
    return ((3.785411784*1000)/(liters*1609.344))*100

def mpgtol100km(miles):
    return ((3.785411784*1000)/(miles/100))/1609.344

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
