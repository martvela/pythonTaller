contador=0
califs=[]
def promedio(valores=[]):
    media= sum(valores) / len(valores)
    return media 

while contador < 10:
    valor=int(input(f"Ingrese la calificacion del alumno {contador+1}: "))
    califs.append(valor)
    contador+=1
print(f"Las calificaciones guardadas son: {califs}")


print(f"El promedio de la clase es: {promedio(califs)}")


    
