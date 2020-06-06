from multiprocessing import Pool 
import pandas as pd

def reducer(df):
    dfGrouped = df.groupby([df.columns[0]]).size()
    return dfGrouped



df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')
df.head()

dfMunicipio = df.filter(items=[df.columns[1]])
dfDia = df.filter(items=[df.columns[4]])
dfClase = df.filter(items=[df.columns[5]])

listas = [dfMunicipio, dfDia, dfClase]

p = Pool(processes=3)
print("antes de map") 
result = p.map(reducer, listas)
print("ya va a imprimir el cosigo")
print(result.to_string()) 

