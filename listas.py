def suma(num1, num2):
    total
    total =num1 + num2
    return total
    
#Listas 
mylist=[1,45,6,7,4,5,67,43]
print(mylist)
print(mylist[5])
#len cuantos valores tiene 
print(len(mylist))
#agregar un valor a la lista poniendolo hasta el final
mylist.append(5)
print(mylist)

#visualizar posicion exacta de la ista 
for count ,element in enumerate (mylist):
    print(f"contador{count} element {element}")

#copia de las listas y podemos sumar listas }

#podemos ordenar nuestras lista 
mylist.sort ()
print(mylist)
#podemos buscar en la lista 
if 7 in mylist:
    print("si esta el 7")
    print(mylist.index(7))
