import mysql.connector

#forma local
host="localhost"
user="root"
passwd=""
port=3306
database="mini-siau"
try:
    conexion= mysql.connector.connect(host=host,
                                      user=user,
                                      passwd=passwd,
                                      port=port,
                                      database=database)
    cursor = conexion.cursor()
    cursor.execute("SELECT name from maestro where name like 'd%' ")
    regsitros = cursor.fetchall()
    for registro in regsitros:
        print(f'name: {registro[0]}')
    print("Conexion correcta")
except mysql.connector.Error as err:
    print("Ocurrio un error al conectar: ", err )
finally:
    conexion.close()