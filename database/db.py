#conexion a la BD
import psycopg2 #modulo para jugar con Postgres
from psycopg2 import DatabaseError #por si sucede un error

def conexion():
    try:
        return psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'admin',
            database = 'chikkins'
        )
    except DatabaseError as ex :
        raise ex