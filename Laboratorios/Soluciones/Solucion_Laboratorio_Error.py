import re

def readint(prompt, min, max):
    isOk = False
    while isOk != True:
        try:
            value = input(prompt)
            assert(re.search("^-?[0-9]*$",value)), "Error: Error en el ingreso"
            value = int(value)
            assert(value >= min and value <= max), "Error: el valor no está en el rango permitido [{0}, {1}]".format(min, max)
            isOk = True
        except Exception as e:
            print(e)
    return value
    

result = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", result)
