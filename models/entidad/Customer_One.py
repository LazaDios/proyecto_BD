#Modelo de La Entidad Cliente (Customer en Ingles)


class Customer_One():

    #constructor del Cliente
    def __init__(self , cedula , name = None , whatsapp = None , email = None ):

        self.cedula = cedula
        self.name = name
        self.whatsapp = whatsapp
        self.email = email
    
    #Para poder imprimir los datos en Formarto JSON
    def to_JSON(self):

        return {
            'cedula' : self.cedula,
            'name' : self.name,
            'whatsapp' : self.whatsapp,
            'email' : self.email
        }
        
        