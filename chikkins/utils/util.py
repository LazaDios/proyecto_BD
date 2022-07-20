from database.db import conexion
import datetime #para las Fechas

class Validar():
    
    @classmethod
    def all_table_cedula(self): #hacer una consulta a todos los datos de la tabla

        try:
            conectar = conexion()
            all_datos_BD = [] #guardaremos todo lo obtenido
            

            with conectar.cursor() as cursor:
                cursor.execute(" SELECT cedula, whatsapp, email   FROM customer")
                all_datos = cursor.fetchall() #Guardara todos los datos seleccionados 
                
                for row in all_datos:
                    all_datos_BD += row[0] , row[1] , row[2]
                    
                conectar.close()


            return all_datos_BD #mostrar el array o lista de los datos guardados en la BD

            

        except Exception as ex:
            raise Exception(ex)


    #consultar todas las ID de la tabla Orders
    @classmethod
    def all_table_id(self):
        try:
            conectar = conexion()
            all_datos_BD = [] #guardaremos todo lo obtenido

            with conectar.cursor() as cursor:
                cursor.execute(" SELECT id FROM orders")
                all_datos = cursor.fetchall() #Guardara todos los datos seleccionados 
                
                for row in all_datos:
                    all_datos_BD += row
                    
                conectar.close()


            return all_datos_BD #mostrar el array o lista de los datos guardados en la BD


        except Exception as ex:
            raise Exception(ex)


    #validar fecha guardada en la BD
    @classmethod
    def convertir_dato(self , date):
        return datetime.datetime.strftime( date , '%Y-%m-%d %H:%M:%S')


