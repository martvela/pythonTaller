import funciondeconexion
import mysql.connector

def interfazsql(id,tittle):
    try:
        conexion = funciondeconexion.conectarbd(1)
        cursor = conexion.cursor()
        sql=f"DELETE FROM `materia` WHERE  `tittle`='{tittle}' AND `id`={id} LIMIT 1;"
        #f"SELECT tittle, id FROM materia WHERE id = {id} AND tittle ='{tittle};"
        #f"INSERT INTO `materia` (`tittle`,`id`) VALUES ('{title}', '{id}');"
        #f"UPDATE materia SET id = {id} WHERE title = '{title}',"
        #f"DELETE FROM `materia` WHERE  `tittle`='{tittle}' AND `id`={id} LIMIT 6;"
        print(sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("fail to update record to database rollbak: {}".format(error))
        conexion.rollback()  

interfazsql('13', 'administración financiera')