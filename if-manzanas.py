precioDeManzana:int = int(input("Ingrese el precio de la manzana: "))
cantidadManzanas:int = int(input("Ingrese la cantidad de las manzanas: "))
#Comentarios de una linea 

#Concatenacion diferentes formas 
print("Las manzanas estan en: " + str(precioDeManzana))
print("La cantidad de manzanas es:", cantidadManzanas)

if cantidadManzanas > 10:
    descuento=(cantidadManzanas*precioDeManzana)*.10
    print(f"FELICIDADES tienes un descuento de {descuento}, pagaras {(cantidadManzanas*precioDeManzana)-descuento}")
    
