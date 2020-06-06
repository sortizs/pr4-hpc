# MapReduce secuencial
import pandas as pd

# Leemos el archivo desde un dataset al dataframe
df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')

# Indicamos que el archivo contiene el nombre de las columnas
df.head()

# Filtramos por el nombre del municipio
dfMunicipio = df.filter(items=[df.columns[1]])

# Agrupamos por nombre de municipio y contamos los registros de cada grupo
dfGrouped = dfMunicipio.groupby([dfMunicipio.columns[0]]).size()

# print dfGrouped.to_string()