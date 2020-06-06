from multiprocessing import Pool 
import pandas as pd

def reducer(fil):
    fil.head()
    dfMunicipio = fil.filter(items=[fil.columns[1]])
    dfGrouped = dfMunicipio.groupby([dfMunicipio.columns[0]]).size()
    return dfGrouped

if __name__ == "__main__":
    df = pd.read_csv('../dataset/datos.csv', delimiter=';', encoding='ISO-8859-1')
    p = Pool() 
    result = p.map(reducer, df)
    print(result.to_string()) 

