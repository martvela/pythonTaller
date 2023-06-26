class person:
    name:str
    age:int
    
    def greetttings():
        print("Hola mi nombre es ")
    
    
person1 = person
person1.name='santiago'
person1.age=18

person2 = person
person2.name='juan'
person2.age=44

print(person1.name)
person1.greetttings()
print(person1.age)

