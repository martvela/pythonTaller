import menu 
import materiaDao

menu.menuPrincipal()
opcion = int(input('Ingresa una opcion: '))

if opcion == 1:
    id = input("ingresa el id--> ")
    tittle = input("Ingresa el nombre de la materia --> ")
    materiaDao.altaMateria(id,tittle)
elif opcion == 2:
    id = input("ingresa el id--> ")
    materiaDao.verMateria(id)
elif opcion == 3:
    materiaDao.verTodasMaterias()
elif opcion == 4:
    id = input("ingresa el id--> ")
    tittle = input("Ingresa el nombre de la materia --> ")
    materiaDao.ModificarMateria(id,tittle)
elif opcion == 5:
    id = input("ingresa el id--> ")
    tittle = input("Ingresa el nombre de la materia --> ")
    materiaDao.borrarMateria(id,tittle)
    
