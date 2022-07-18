#Acciones de Crear Pedido e iterar con la BD (MODELO DE LOS PEDIDOS)

#modulos a importar
from database.db import conexion #BD
from .entidad.Order_One import Order_One #entidad de la Orden

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
        try:
            conectar = conexion()

            with conectar.cursor() as cursor:
                cursor.execute("INSERT INTO customer VALUES ( %s , %s  , %s , %s , %s, %s, %s, %s, %s, %s, %s )"  , (order.cedula_cliente, None, order.payment_method, order.remarks, order.city, order.municipality, order.total, order.payment_scrennshot, order.delivery_amount, order.status, order.datetime))

                #verificar cuantas filas afecto cuando hago la insercion
                fila_afectada = cursor.rowcount  #me saca cuantas filas ha sacado
                conectar.commit() #confirmar los cambios que he hecho

            conectar.close()

            return fila_afectada

        except Exception as ex:
            raise Exception(ex)


    ################################### FIN DE INSERCCION ##############################