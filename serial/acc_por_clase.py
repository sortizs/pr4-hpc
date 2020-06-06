# MapReduce secuencial
import pandas as pd

def map(df):
    dfMapped = df.filter(items=[df.columns[5]])
    return dfMapped

def reduce(df):
    dfReduced = df.groupby([df.columns[0]]).size()
    return dfReduced

df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')

df.head()

dfClase = map(df)

dfGrouped = reduce(dfClase)

print(dfGrouped.to_string())