precioDeManzana:int = int(input("Ingrese el precio de la manzana: "))
cantidadManzanas:int = int(input("Ingrese la cantidad de las manzanas: "))
#Comentarios de una linea 

#Concatenacion diferentes formas 
print("Las manzanas estan en: " + str(precioDeManzana))
print("La cantidad de manzanas es:", cantidadManzanas)
print(f"Vas a pagar: {cantidadManzanas * precioDeManzana}")
