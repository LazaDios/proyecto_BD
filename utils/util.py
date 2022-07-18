from database.db import conexion
from models.entidad.Customer_One import Customer_One
#para las Fechas
import datetime

class Validar():
    
    @classmethod
    def all_table_cedula(self): #hacer una consulta a todos los datos de la tabla

        try:
            conectar = conexion()
            all_datos_BD = [] #guardaremos todo lo obtenido
            

            with conectar.cursor() as cursor:
                cursor.execute(" SELECT cedula, whatsapp, email   FROM customer")
                all_datos = cursor.fetchall() #Guardara todos las cedulas 
                
                for row in all_datos:
                    all_datos_BD += row[0] , row[1] , row[2]
                    
                conectar.close()


            return all_datos_BD #mostrar el array o lista de los datos guardados en la BD

            

        except Exception as ex:
            raise Exception(ex)

    #validar fecha guardada en la BD

    @classmethod
    def convertir_dato(self , date):
        return datetime.datetime.strftime( date , '%d / %m / %Y %H:%M:%S')

