#Acciones que tendra mi Entidad CLiente , acciones que tendra con la BD 

#modulos a importar
from database.db import conexion  #metodo para el manejo de la BD
from .entidad.Customer_One import Customer_One #entidad/customer_one/Customer_One() --> importar ese modulo

class Customer_Model():

    #1. Servicio para crear un cliente.
    @classmethod #para poder instanciar directamente
    def add_customer(sef  ,  customer):
        try:
            conectar = conexion()

            with conectar.cursor() as cursor:
                cursor.execute("INSERT INTO customer VALUES ( %s , %s  , %s , %s )"  , (customer.cedula ,customer.name , customer.whatsapp , customer.email ))

                #verificar cuantas filas afecto cuando hago la insercion
                fila_afectada = cursor.rowcount  #me saca cuantas filas ha sacado
                conectar.commit() #confirmar los cambios que he hecho

            conectar.close()

            return fila_afectada

        except Exception as ex:
            raise Exception(ex)

    ############################ FIN CREAR CLIENTE  ##############################



    #2. Servicio para editar un cliente.
    @classmethod
    def update_customer(self , customer):
        try:
            conectar =  conexion()

            with conectar.cursor() as cursor:
                cursor.execute("""UPDATE customer SET name = %s ,  whatsapp= %s  , email= %s 
                                    WHERE cedula = %s"""  , (customer.name , customer.whatsapp , customer.email , customer.cedula ))

                fila_afectada = cursor.rowcount  #me saca cuantas filas ha sacado
                conectar.commit() #confirmar los cambios que he hecho

            conectar.close()

            return fila_afectada

        except Exception as ex  :
            raise Exception(ex)

 ############################ FIN EDITAR CLIENTE  ##############################



    #3. Servicio para Mostrar todos los Clientes
    @classmethod 
    def get_customer(self):
        
        #manejo de Errores
        try:
            conectar = conexion() #instanciar la Conexion de BD
            customer_all = [] #lista vacia donde guardaremos los datos que buscaremos de la BD

            with conectar.cursor() as cursor:
                cursor.execute( "SELECT cedula , name , whatsapp , email FROM customer" )#sentencia SQL a realizar
                result_busqueda = cursor.fetchall() #todos los datos

                for row in result_busqueda: 
                        customer = Customer_One(row[0] , row[1] , row[2] , row[3])
                        customer_all.append(customer.to_JSON()) #a todos los clientes se le guardara los clientes sacado de la BD 
                conectar.close()

                return customer_all #con to_JSON se imprimira en formato JSON

        except Exception as ex:
            raise Exception(ex)

    ############################FIN MOSTRAR TODOS LOS CLIENTES ##############################