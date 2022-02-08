import random
X= int(input("Ingrese un valor entre 0 y 1000: "))

Array = [0, 1, 2, 3, 4]

for i in range(0,5):
    Array[i]=random.randint(0, 1000)
    print (Array[i])
    if Array[i]== X:
        print("Los valores son iguales")
    elif Array[i]<X:
        print("El arreglo es menor.")
    else:
        print("El arreglo es mayor.")
    print("")