#CRUD
import bdconector
import mysql.connector
import materia

def altaMateria():
    pass

def verMateria():
    pass

def verTodasMaterias():
    try:
        conexion = bdconector.conexionBd('local')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materia")
        registros = cursor.fetchall()
        for registro in registros:
            #Materia = materia(registro[0], registro[1])
            print(f'id = {registro[0]} titulo = {registro[1]} ')
            print(materia)
        cursor.close
        conexion.close
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()


def ModificarMateria():
    pass

def borrarMateria():
    pass

