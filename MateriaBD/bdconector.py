import mysql.connector
selectorBaseDeDatos = 'local'

def conexion(selectorBaseDeDatos):
    if selectorBaseDeDatos == 'local':
        #Base de datos local
        host="localhost"
        user="root"
        passwd=""
        port = 3306
        database="mini-siau"
    elif selectorBaseDeDatos == 'remoto':
        #Base de datos remota 
        host=""
        user="root"
        passwd=""
        port = 3306
        database="mini-siau"
    conexion = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    port=port,
    database=database)
    return conexion