from flask import Flask

from routes import Rutas

#rutas a importar


app=Flask(__name__)
app.secret_key = 'cr7elmejor'

#Por si no encontramos la ruta seleccionada
def pagina_no_encontrada(error):
    return '<h1>PAGINA NO ENCONTRADA...</h1>', 404


#Arranque de App
if __name__ == '__main__':
    
    #Acceder a dichas rutas con "BLUEPRINTS"
    app.register_blueprint(Rutas.main)

    #manejo de error
    app.register_error_handler(404 , pagina_no_encontrada)

    app.run(debug=True) #debug=True para que autoguarde cada cambio..