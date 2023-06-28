import menu 
import materiaDao
menu.menuPrincipal()
opcion = input('Ingresa una opcion: ')

if opcion==3:
    materiaDao.verTodasMaterias()
