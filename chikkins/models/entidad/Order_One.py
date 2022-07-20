#Modelo de La Entidad Ordenes o Pedidos (Orders en Ingles)

class Order_One():

    #constructor del Cliente
    def __init__(self , id ,cedula_cliente = None , quantity = None,  payment_method= None , remarks= None , city= None , municipality= None , total= None , payment_scrennshot = None, delivery_amount = None  , status = None , datetime = None):

        self.id = id
        self.cedula_cliente = cedula_cliente
        self.quantity = quantity
        self.payment_method = payment_method
        self.remarks = remarks
        self.city = city
        self.municipality = municipality
        self.total = total
        self.payment_scrennshot = payment_scrennshot
        self.delivery_amount = delivery_amount
        self.status = status
        self.datetime = datetime

    
    #Para poder imprimir los datos en Formarto JSON
    def to_JSON(self):

        return {
            'id' : self.id,
            'cedula_cliente' : self.cedula_cliente,
            'quantity' : self.quantity,
            'payment_method' : self.payment_method,
            'remarks' : self.remarks,
            'city' : self.city,
            'municipality' : self.municipality,
            'total' : self.total,
            'payment_scrennshot' : self.payment_scrennshot,
            'delivery_amount' : self.delivery_amount,
            'status' : self.status,
            'datetime' : self.datetime
        }
        
        