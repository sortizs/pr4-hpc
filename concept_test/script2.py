from multiprocessing import Pool 
import pandas as pd

def reducer(df):
    dfMunicipio = df.filter(items=[df.columns[1]])
    dfGrouped = dfMunicipio.groupby([dfMunicipio.columns[0]]).size()
    return dfGrouped



df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')
df.head()

p = Pool(processes=3)
print("antes de map") 
result = p.map(reducer, df)
print("ya va a imprimir el cosigo")
print(result.to_string())