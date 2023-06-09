year=int(input("Ingresa un año -->"))

if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
    print("Es año bisiesto")
else:
    print("Tu año es un año comun")
    