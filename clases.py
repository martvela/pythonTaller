class Person:
    def __init__(self, name, age):  #constructor es esta funcion (doble guion bajo __init__)
        self.name = name #la variable nombre es propio de este self y asi con los demas
        self.age = age
    
    def saludo (self):
        print(f"Hola mi nombre es {self.name} y mi edad es {self.age}")

p1= Person("santiago", 18)  #se define de esta forma el objeto 
p2= Person("juan", 44)

p1.saludo()
p2.saludo()

