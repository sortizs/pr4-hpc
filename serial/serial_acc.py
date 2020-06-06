# MapReduce secuencial
import pandas as pd

def map(df, num):
    dfMapped = df.filter(items=[df.columns[num]])
    return dfMapped

def reduce(df):
    dfReduced = df.groupby([df.columns[0]]).size()
    return dfReduced

df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')

df.head()

dfMunicipio = map(df, 1)
dfgMun = reduce(dfMunicipio)
print(dfgMun.to_string())

dfDia = map(df, 4)
dfgDia = reduce(dfDia)
print(dfgDia.to_string())

dfClase = map(df, 5)
dfgClase = reduce(dfClase)
print(dfgClase.to_string())

dfGravedad = map(df, 7)
dfgClase = reduce(dfGravedad)
print(dfgClase.to_string())
