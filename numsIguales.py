#Tres numeros y su igualdad
num5=int(input("Ingrese el primer numero:"))
num6=int(input("Ingrese el segundo numero:"))
num7=int(input("Ingrese el tercer numero:"))

if num5 == num6 and num7 == num6 and num5 == num7:
    print("Ingresaste numeros iguales")
elif num5!=num6 and num5==num7:
    print("Hay dos numeros iguales")
elif num6!=num7 and num6==num7:
    print("Hay dos numeros iguales")
elif num7!=num5 and num6==num5:
     print("Hay dos numeros iguales")
elif num5!=num6 and num6==num7:
    print("Hay dos numeros iguales")
else:
    print("Ingresaste numeros diferentes")
