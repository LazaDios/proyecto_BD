#Diferentes URL o RUTAS que tendra mi Api
import datetime
from flask import Blueprint , jsonify , request
from database.db import conexion #BD
#entidad
from models.entidad.Customer_One import Customer_One
from models.entidad.Order_One import Order_One

#models
from models.customer_models import Customer_Model
from models.order_models import Order_Model

#utils , para Validar
from utils.util import Validar

main = Blueprint('customer_blueprint' , __name__)

########################## CLIENTES ############################

#RUTA PARA CREAR LOS CLIENTES
@main.route('/customers' , methods = ['POST'])
def add_customer():
    try:
        cedula = request.json['cedula']
        name = request.json['name']
        whatsapp = request.json['whatsapp']
        email = request.json['email']

        #validar que no se duplique cedula, gmail y whastapp.
        cedulas_all = Validar.all_table_cedula()
        
        for row in cedulas_all:
            if cedula == row or  whatsapp == row or email == row:
                return jsonify({"elerta" : "No puedes repetir Cedula , Whatapp ni Gmail , por Favor verifique los datos ingresados"}), 500
                exit
        

        #con los datos que se pasara por POST que sera un JSON , se guardaran en un Objeto cliente
        customer = Customer_One(cedula , name , whatsapp , email)
        filas_afectada = Customer_Model.add_customer(customer) #guardamos en una Funcion el valor que dara si se guardo los datos correctamente

        if filas_afectada == 1:
            return jsonify({'Cedula' : customer.cedula , 'Creado' : 'Si Fue creado con Exito'}) #si se crea con exito , mostrara la cedula
        else:
            return jsonify({'Creado' :"no , hubo un error al Crear"}) , 500

    except  Exception as ex :
        return jsonify({'mal' : str(ex)}) , 500


#RUTA PARA EDITAR UN CLIENTE POR LA CEDULA (cedula no se edita)
@main.route('/customers/<cedula>' , methods = ['PUT'])
def update_customer(cedula):
    try:

        name = request.json['name']
        whatsapp = request.json['whatsapp']
        email = request.json['email']
        
        customer = Customer_One(cedula , name , whatsapp , email)
        filas_afectada = Customer_Model.update_customer(customer) #guardamos en una Funcion el valor que dara si se guardo los datos correctamente

        if filas_afectada == 1:
            return jsonify({'Cedula' : customer.cedula , 'Editada' : 'Si Fue Editada con Exito'}) #si se crea con exito , mostrara la cedula
        else:
            return jsonify({'Editada' :"no , hubo un error al Editar"}) , 500
            

    except Exception as ex:
        return jsonify( {'Mensaje' : str(ex)} ) , 500



#RUTA PARA MOSTRAR TODOS LOS CLIENTES
@main.route('/customers' , methods = ['GET'])
def get_customer():
    try:
        customer_all = Customer_Model.get_customer()
        return jsonify(customer_all) #retornar todos los Clientes

    except Exception as ex:
        return jsonify( {'Mensaje' : str(ex)} ) , 500 



########################## PEDIDOS U ORDEN ############################

#RUTA PARA CREAR LOS PEDIDOS
@main.route('/orders' , methods = ['POST'])
def add_orders():
    try:
    
        #Datos ingresados por POST , segun el enunciado...
        cedula_cliente = request.json['cedula_cliente']
        quantity = request.json['quantity']
        payment_method = request.json['payment_method']
        remarks = request.json['remarks']
        city = request.json['city']
        municipality = request.json['municipality']

        #DATOS GENERADOS , LA FECHA CON EL FORMATO: A-M-D H-M-S
        fecha = datetime.datetime.now() #guardar toda la fecha
        time = Validar.convertir_dato(fecha) #colocar un formato valido

        #RUTA DEL CAPTURE DE PANTALLA QUEDA VACIA POR LOS MOMENTOS
        payment_scrennshot = "null"

        #VERIFICAR SI SE PAGARA DELIVERY
        delivery_amount = 2
        if str(municipality.upper()) == "MANEIRO":
            delivery_amount = 0
        
        #TOTAL A PAGAR , CADA BURGUER VALE 5$ CON DELIVERY $2
        total = (int(quantity) * 5) + delivery_amount
        
        #El STATUS TIENE 4 ESTADOS (PENDIENTE [POR DEFECTO CUANDO SE CREA EL PEDIDO] , EN PROGRESO , DESPACHADO , COMPLETADO )
        status = "pendiente"
        
        #ID PARA LAS TABLAS AUTO_INCREMENT
        id_tablas = Validar.all_table_id()
        id = 0
        if id_tablas == []:
            id = 1

        if id_tablas != []:
            for i in id_tablas:
                id = i + 1
        
        #con los datos que se pasara por POST que sera un JSON , se guardaran en un Objeto cliente
        order =  Order_One( id , cedula_cliente, int(quantity) ,payment_method , remarks , city ,municipality ,total , payment_scrennshot, delivery_amount, status , str(time))  
        filas_afectada = Order_Model.add_order(order)  #guardamos en una Funcion el valor que dara si se guardo los datos correctamente

        if filas_afectada == 1:
            return jsonify({'Cedula' : order.cedula_cliente , 'Pedido' : 'Si Fue creado con Exito'}) #si se crea con exito , mostrara la cedula
        else:
            return jsonify({'Creado' :"no , hubo un error al Crear"}) , 500

    except  Exception as ex :
        return jsonify({'mal' : str(ex)}) , 500



#RUTA PARA MOSTRAR LOS PEDIDOS
@main.route('/orders' , methods = ['GET'])
def get_orders():

    try:
        orders = Order_Model.get_order()
        return jsonify(orders) #retornar todos los Clientes
        
    except  Exception as ex :
        return jsonify({'mal' : str(ex)}) , 500


#RUTA PARA EDITAR SOLO EL ESTADO DEL PEDIDO MEDIANTE UN <ID>/STATUS (POST)
@main.route('/orders/<id>/status'  ,  methods = ['PATCH'])
def update_status(id):
    try:
        status = request.json['status']

        order = Order_One( id , '' , 0 , '' , '' , '' , '' , 0, '', 0, status.lower() , '') #los otros datos no importan porque no seran modificados
        filas_afectadas = Order_Model.update_pedido(order)

        print(filas_afectadas)
        if filas_afectadas == 1 :
            return jsonify( { 'MODIFICADO EL STATUS PARA EL PEDIDO CON EL ID': order.id} )
        else:
            return jsonify({'message' :"status del pedido no fue actualizado"}) , 404

    except  Exception as ex :
        return jsonify({'mal' : str(ex)}) , 500


#RUTA PARA BUSCAR POR EL DATE < STATUS < CEDULA (GET)
@main.route('/orders/<status>/<cedula_cliente>'  , methods = ['GET'])
def filtro_bsuqueda(status , cedula_cliente):
        try:
            conectar = conexion() #instanciar la Conexion de BD
            orders_all = [] #lista vacia donde guardaremos los datos que buscaremos de la BD

            with conectar.cursor() as cursor:
                cursor.execute( "SELECT * FROM orders WHERE   cedula_cliente = %s and status = %s" ,  ( cedula_cliente , status.lower())) #Busqueda Filtrada
                result_busqueda = cursor.fetchall() #todos los datos que coincidan con la busqueda

                if result_busqueda != []: #si la busqueda coincide con los datos en la tabla se imprimira dichos datos
                
                    for row in result_busqueda: 

                        orders = Order_One(row[0] , row[1] , row[2] , row[3] ,row[4] , row[5] , row[6] , row[7] , row[8] , row[9] , row[10] , row[11])
                        orders_all.append(orders.to_JSON()) #a todos los clientes se le guardara los clientes sacado de la BD 
                    
                    conectar.close()

                    return jsonify(orders_all)#con to_JSON se imprimira en formato JSON
                else: #si la busqueda por la URL no coincide se imprimira todos los datos de la tabla , tal como lo dice el enunciado
                    orders = Order_Model.get_order()
                    return jsonify(orders) #retornar todos los Clientes
                    

        except Exception as ex:
            raise Exception(ex)