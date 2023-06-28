import mysql.connector
opcionBaseDeDatos = 1
def conectarbd(opcionBaseDeDatos):
    if opcionBaseDeDatos == 1 :
        #Forma local
        host="localhost"
        user="root"
        passwd=""
        port = 3306
        database="mini-siau"
    elif opcionBaseDeDatos == 2 :
        #Forma remota
        host="142.44.163.242"
        user="Alumno6"
        passwd="AlumnoPython1@." 
        port = 4000
        database='mini-siiau'
        
    conexion = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    port=port,
    database=database)
    return conexion