import funciondeconexion
import mysql.connector

def interfazsql(sql):
    try:
        conexion = funciondeconexion.conectarbd(1)
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()    

interfazsql("select md.schedule, md.classroom, mtr.id from materiasdisponibles as md right join maestro as mtr on md.idmaestro = mtr.id")