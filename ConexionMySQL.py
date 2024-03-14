# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:52:40 2024

@author: jcgarciam
"""
import pandas as pd
import mysql.connector

config = {
        'user':'root',
        'password':'J4vierc4m23*',
        'host':'localhost',
        'database':'tienda1'
    }
conn = mysql.connector.connect(**config)

#%%
cursor = conn.cursor()
consulta = 'select * from cliente'
cursor.execute(consulta)

resultados = cursor.fetchall()
#%%
"""
for fila in resultados:
    print(fila)
    
cursor.close()
conn.close()
"""
#%%
columnas = [i[0] for i in cursor.description]
cursor.close()
conn.close()


df = pd.DataFrame(resultados, columns = columnas)

