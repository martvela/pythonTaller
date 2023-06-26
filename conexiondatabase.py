import funciondeconexion
import mysql.connector

def interfazsql(sql):
    try:
        conexion = funciondeconexion.conectarbd
        cursor = conexion.cursor()
        cursor.execute("sql")
        for i in cursor:
            print(i)
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        conexion.close()    

interfazsql("select name from maestro")