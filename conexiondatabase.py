import funciondeconexion
import mysql.connector

def interfazsql(id,tittle):
    try:
        conexion = funciondeconexion.conectarbd(1)
        cursor = conexion.cursor()
        sql=f"SELECT tittle, id FROM materia WHERE id = {id} AND tittle ='{tittle};"
        #f"SELECT tittle, id FROM materia WHERE id = {id} AND tittle ='{tittle};"
        #f"INSERT INTO `materia` (`tittle`,`id`) VALUES ('{title}', '{id}');"
        #f"UPDATE materia SET id = {id} WHERE title = '{title}',"
        #f"DELETE FROM `materia` WHERE  `tittle`='{tittle}' AND `id`={id} LIMIT 6;"
        print(sql)
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            #Materia = materia(registro[0], registro[1])
            print(f'id = {registro[0]} titulo = {registro[1]} ')
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print("fail to update record to database rollbak: {}".format(error))
        conexion.rollback()  

interfazsql('333', 'economía')