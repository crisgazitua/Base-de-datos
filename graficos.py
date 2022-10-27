import psycopg2
import csv 
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set_style("whitegrid")
sns.set(rc={'figure.figsize':(18,12)})
sns.set_palette(sns.color_palette())


# Ingresar sus datos aqui 
params = {
    "host"      : "201.238.213.114", 
    "user"      : "bd_group_18",
    "password"  : "p3pXZ8",
    "port":       "54321" 
}

conn = psycopg2.connect(**params)
cursor = conn.cursor()

cursor.execute("""
Select trade_value, hs2 From transaccion
Group by trade_value, hs2
""")

df = pd.DataFrame(
    cursor.fetchall(),
    columns=['trade_value', 'hs2']
)

sns.violinplot(data=df, x="trade_value", y="hs2")


# cerramos el cursor y la conexion 
cursor.close()
conn.close()