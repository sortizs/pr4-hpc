# MapReduce secuencial
import pandas as pd

def map(df):
    dfMapped = df.filter(items=[df.columns[1]])
    return dfMapped

def reduce(df):
    dfReduced = df.groupby([df.columns[0]]).size()
    return dfReduced

df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')

df.head()

dfMunicipio = map(df)

dfGrouped = reduce(dfMunicipio)

print(dfGrouped.to_string())