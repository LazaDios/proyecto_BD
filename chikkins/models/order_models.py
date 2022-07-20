#Acciones de Crear Pedido e iterar con la BD (MODELO DE LOS PEDIDOS)

#modulos a importar
from database.db import conexion #BD
from .entidad.Order_One import Order_One #entidad de la Orden
#import random

class Order_Model():

    """"1- Crear un pedido , solo debe ingresar:
           "quantity”: “?”,
            “payment_method”: “?”,
            “remarks”: “?”,
            “city”: "?”,
            “municipality”: ?,
            “cedula”: ?
        *****pero debe mostrar o su salida sera:****
            “quantity”: “2”,
            “payment_method”: “pago_movil”,
            “remarks”: “Una sin queso fundido”,
            “city”: “Atamo Sur”,
            “municipality”: “Arismendi”,
            “cedula”: “21444333”,
            “total”: “$12.00”,
            “payment_screenshot”: null,
            “status”: “pending”,
            “delivery_amount”: “$2.00”,
            “order_number”: “2678822”,
            “datetime”: “2022-06-28 15:00:00"""
    
    @classmethod #para poder instanciar directamente
    def add_order(sef  ,  order):
        #id =  random.randint(10, 2000) #mientras tanto...
        try:
            conectar = conexion()

            with conectar.cursor() as cursor:
                cursor.execute("INSERT INTO orders VALUES (%s, %s, %s , %s , %s , %s, %s, %s, %s, %s, %s, %s )"  , (order.id ,  order.cedula_cliente , order.quantity ,order.payment_method, order.remarks, order.city, order.municipality, order.total, order.payment_scrennshot, order.delivery_amount, order.status , order.datetime))

                #verificar cuantas filas afecto cuando hago la insercion
                fila_afectada = cursor.rowcount  #me saca cuantas filas ha sacado
                conectar.commit() #confirmar los cambios que he hecho

            conectar.close()

            return fila_afectada

        except Exception as ex:
            raise Exception(ex)


    ################################### FIN DE INSERCCION ##############################

    #1.2. Servicio para Mostrar todos los pedidos
    @classmethod 
    def get_order(self):
        try:
            conectar = conexion() #instanciar la Conexion de BD
            orders_all = [] #lista vacia donde guardaremos los datos que buscaremos de la BD

            with conectar.cursor() as cursor:
                cursor.execute( "SELECT * FROM orders")#sentencia SQL a realizar
                result_busqueda = cursor.fetchall() #todos los datos

                for row in result_busqueda: 

                    orders = Order_One(row[0] , row[1] , row[2] , row[3] ,row[4] , row[5] , row[6] , row[7] , row[8] , row[9] , row[10] , row[11])
                    orders_all.append(orders.to_JSON()) #a todos los clientes se le guardara los clientes sacado de la BD 
                
                conectar.close()

                return orders_all #con to_JSON se imprimira en formato JSON

        except Exception as ex:
            raise Exception(ex)

    ############################FIN MOSTRAR TODOS LOS PEDIDOS ##############################

    #2.Editar solo STATUS Mediante un ID
    @classmethod
    def update_pedido(sef , orders):
        try:
            conectar = conexion()

            with conectar.cursor() as cursor:
                cursor.execute("""UPDATE orders SET status = %s 
                               WHERE id = %s""", (orders.status , orders.id)) 

                #verificar cuantas filas afecto cuando hago la insercion
                fila_afectada = cursor.rowcount  #me saca cuantas filas ha sacado
                conectar.commit() #confirmar los cambios que he hecho
            
            conectar.close()
            return fila_afectada

        except Exception as ex  :
            raise Exception(ex)
    ########################### FIN EDITAR ESTATU DE UN PEDIDOS ##############################

    #3.Filtro de Busqueda mediante (id  , cedula , fecha)

    @classmethod 
    def filtro(self , orders):
        try:
            conectar = conexion() #instanciar la Conexion de BD
            orders_all = [] #lista vacia donde guardaremos los datos que buscaremos de la BD

            with conectar.cursor() as cursor:
                cursor.execute( "SELECT * FROM orders WHERE   cedula_cliente = %s and status = %s" ,  ( orders.cedula_cliente , orders.status)) #Busqueda Filtrada
                result_busqueda = cursor.fetchall() #todos los datos que coincidan con la busqueda

                for row in result_busqueda: 

                    orders = Order_One(row[0] , row[1] , row[2] , row[3] ,row[4] , row[5] , row[6] , row[7] , row[8] , row[9] , row[10] , row[11])
                    orders_all.append(orders.to_JSON()) #a todos los clientes se le guardara los clientes sacado de la BD 
                
                conectar.close()

                return orders_all #con to_JSON se imprimira en formato JSON

        except Exception as ex:
            raise Exception(ex)