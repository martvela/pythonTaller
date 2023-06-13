import os


def saludo ():
    print("Hola")
    
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

os.system("cls")

print("hey".center(40,"="))
saludo()
saludo()
saludo()

#puedo traer funciones de liberias al descargarlas o de archivos que yo haga traerme las funciones


