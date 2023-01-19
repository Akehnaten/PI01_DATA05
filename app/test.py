# Librerias
import pymysql
import sqlalchemy
import pandas as pd
import numpy as np

def crear_tabla():

    # Creo la conexión
    conexion = pymysql.connect(
            host = 'aws-sa-east-1.connect.psdb.cloud',
            user = 'hdj11vgbubzez1k2mmw0',
            passwd = 'pscale_pw_xJtpCj9sIr1JRelAqFEIRExmGep2kJrFs12dxipAZrZ',
            db = 'grupo7_pg',
            ssl={"rejectUnauthorized":True}
    )

    cursor = conexion.cursor()
    # Cargo datos e importo a MySQL
    url = 'https://raw.githubusercontent.com/ronalcabrera/PG_Olist/main/Datasets/olist_sellers_dataset.csv'
    sellers = pd.read_csv(url, delimiter=',', encoding='UTF-8')

    cursor.execute("""CREATE TABLE TEST( seller_id VARCHAR(50) NOT NULL, 
                                            seller_zip_code_prefix INT NOT NULL,
                                            seller_city VARCHAR(50) NOT NULL,
                                            seller_state VARCHAR(5) NOT NULL)
                        ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;""") # Ejecute cualquier Query deseada
    lista = []
    filas_max = len(sellers.seller_id.to_list())
    for i in range (filas_max):
        lista.append(tuple(sellers.iloc[i]))

    cursor.executemany("""INSERT INTO TEST (
                                seller_id, 
                                seller_zip_code_prefix,
                                seller_city,
                                seller_state)
                                VALUES (%s, %s,%s, %s)""", lista)

    conexion.commit() # actualizo para ver los datos
    conexion.close()
    
    return sellers
