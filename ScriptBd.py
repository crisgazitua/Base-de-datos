import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv 
import pandas as pd 

# Ingresar sus datos aqui 
params = {
    "host"      : "201.238.213.114", 
    "user"      : "bd_group_18",
    "password"  : "p3pXZ8",
    "port":       "54321" 
}

conn = psycopg2.connect(**params)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

#Para llenar la tabla de la base de datos:
df = pd.read_excel('imp_exp_chile.xlsx') # excel de una sola hoja 
 
to_db = []

for a,b,c,d,e,f,g,h,i,j,k,l,m,n in zip( df.Trade_Flow, df.Country, df.Destination_Port, df.fecha, df.Origin_Port, df.HS2, df.HS4, df.Product, df.Quantity, df.Unit, df.Trade_Value, df.Payment_Type, df.Transport_Mode, df.Region):
  to_db.append((a,b,c,d,e,f,g,h,i,j,k,l,m,n))

cursor.executemany("INSERT INTO transaccion (trade_flow, pais_origen, destino, fecha, puerto_origen, hs2, hs4, producto, cantidad, unidad_de_medida, trade_value, medio_de_pago, modo_de_transporte, region) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",  # recordar incorporar nombre de las columnas, agregar aqui tantas %s como columnas tenga la tabla.  
                to_db)

# guardamos los cambios 
conn.commit()

# cerramos el cursor y la conexion 
cursor.close()
conn.close()