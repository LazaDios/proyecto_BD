#Diferentes URL o RUTAS que tendra mi Api
import datetime
from flask import Blueprint , jsonify , request


#entidad
from models.entidad.Customer_One import Customer_One

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

#RUTA PARA CREAR LOS CLIENTES
@main.route('/orders' , methods = ['POST'])
def add_orders():
    try:
        cedula_cliente = request.json['cedula_cliente']
        payment_method = request.json['payment_method']
        remarks = request.json['remarks']
        city = request.json['city']
        municipality = request.json['municipality']
        total = 12.00
        payment_scrennshot = "..."
        delivery_amount = 2.00
        status = "pendiente..."
        time = datetime.datetime.now()

        
        #con los datos que se pasara por POST que sera un JSON , se guardaran en un Objeto cliente
        order = Order_Model(cedula_cliente , None , payment_method , remarks , city ,municipality ,total , payment_scrennshot, delivery_amount, status , time)
        filas_afectada = Order_Model.add_order(order)  #guardamos en una Funcion el valor que dara si se guardo los datos correctamente

        if filas_afectada == 1:
            return jsonify({'Cedula' : cedula_cliente , 'Pedido' : 'Si Fue creado con Exito'}) #si se crea con exito , mostrara la cedula
        else:
            return jsonify({'Creado' :"no , hubo un error al Crear"}) , 500

    except  Exception as ex :
        return jsonify({'mal' : str(ex)}) , 500

