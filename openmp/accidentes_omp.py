from multiprocessing import Pool 
import pandas as pd
import sys 

def reducer(df):
    dfGrouped = df.groupby([df.columns[0]]).size()
    return dfGrouped



df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')
df.head()

dfMunicipio = df.filter(items=[df.columns[1]])
dfDia = df.filter(items=[df.columns[4]])
dfClase = df.filter(items=[df.columns[5]])
dfGravedad = df.filter(items=[df.columns[7]])

listas = [dfMunicipio, dfDia, dfClase, dfGravedad]

p = Pool(processes=4)
result = p.map(reducer, listas)


##for i in result: 
##    print(i.to_string())

