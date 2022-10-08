f = open("devices.txt","a")
while True:  
    newItem = input("Ingrese un nuevo dispositivo -> ")
    if newItem == "exit":
        print("Todo listo!!")
        break
    f.write(newItem + "\n")

f.close()

