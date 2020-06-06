from multiprocessing import Pool 
import pandas as pd

def reducer(fil):
    dfGrouped = fil.groupby([fil.columns[0]]).size()
    return dfGrouped


df = pd.read_csv('../dataset/datos.csv', delimiter=';')
df.head()
dfMunicipio = df.filter(items=[df.columns[1]])
p = Pool(processes=3) 
result = p.map(reducer, dfMunicipio)
print("ya va a imprimir el cosigo")
print(result.to_string())