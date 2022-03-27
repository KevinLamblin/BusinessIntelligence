import mysql
from mysql.connector import Error

"""
Script de connection à la base mySQL

:return La connection
"""
def connection():
    try:
        # Essaye la connection à la base en local avec les logs
        connection = mysql.connector.connect(host='localhost',
                                             database='esirem',
                                             user='root',
                                             password='kQUfotv9rlFeDSJWutMF')

    except Error as e:
        # Affiche un message d'erreur en cas d'échec de connection
        print("Error while connecting to MySQL", e)

    return connection
