# -*- coding: utf-8 -*-

'''
Created on 11/02/2015

@author: ecrespo
@version: 1.0
@description: script para modificar la BBDD con errores de los consumos de NGCS

'''

import datetime
from datetime import timedelta
import mysql.connector as dbapi
from mysql.connector import errorcode

print('Conectando a la BdD...')
usuario = 'user'
contras = 'password'

try: 
    cnx = dbapi.connect(user = usuario, password = contras, 
                    host = '192.168.1.1', database = 'aprendiendoarduino')
    cursor = cnx.cursor()
    query = ("SELECT * FROM temp\
             WHERE cuenta < 6\
			 ORDER BY date ASC")
    cursor.execute(query)
    
    rows = cursor.fetchall()
    
    #print(rows)
    #print("Número de filas de la consulta: ",len(rows))

    print(rows[0])
    print(rows[0][3])
    fecha_fallo = datetime.datetime.strptime(rows[0][3],'%Y-%m-%d %H:%M')
    print(fecha_fallo)
    fecha_corregida = fecha_fallo + timedelta(minutes=1)
    print(fecha_corregida)
    
    query2 = ("SELECT * FROM temp WHERE\
              date_format(date, '%Y-%m-%d %H:%i') = '{0}'"
              .format(fecha_corregida.strftime('%Y-%m-%d %H:%M')))
    print(query2)

    cursor.execute(query2)
    rows2 = cursor.fetchall()
    print(rows2)
    
        
    cursor.close()
except dbapi.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print(err)
else:
    cnx.close()
