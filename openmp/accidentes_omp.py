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
print("ingrese el numero de cores")
n = input()
p = Pool(processes=n)
result = p.map(reducer, listas)


##for i in result: 
##    print(i.to_string())

