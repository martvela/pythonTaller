#CRUD
import bdconector
import mysql.connector
import materia

def altaMateria(id, tittle):
    try:
        conexion = bdconector.conexion('local')
        cursor = conexion.cursor()
        sql= f"INSERT INTO `materia` (`tittle`,`id`) VALUES ('{tittle}', '{id}');"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

def verMateria(id):
    try:
        conexion = bdconector.conexion('local')
        cursor = conexion.cursor()
        cursor.execute(f'SELECT * FROM materia where id = {id}')
        registros = cursor.fetchall()
        for registro in registros:
            print(f'id = {registro[1]} titulo = {registro[0]}')
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

def verTodasMaterias():
    try:
        conexion = bdconector.conexion('local')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materia")
        registros = cursor.fetchall()
        for registro in registros:
            #Materia = materia(registro[0], registro[1])
            print(f'id = {registro[0]} titulo = {registro[1]} ')
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()
        
def ModificarMateria(id,tittle):
    try:
        conexion = bdconector.conexion('local')
        cursor = conexion.cursor()
        sql= f"UPDATE materia SET id = {id} WHERE tittle = '{tittle}';"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

def borrarMateria(id, tittle):
    try:
        conexion = bdconector.conexion('local')
        cursor = conexion.cursor()
        sql= f"DELETE FROM `materia` WHERE  `tittle`='{tittle}' AND `id`={id};"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

