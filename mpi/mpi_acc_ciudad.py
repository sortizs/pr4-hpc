from mpi4py import MPI
import pandas as pd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

df = pd.read_csv('../dataset/datos.csv', delimiter = ';', encoding = 'ISO-8859-1')
df.head()

def reduce(num):
    dfR = df.filter(items = [df.columns[num]])
    dfGrouped = dfR.groupby([dfR.columns[0]]).size()
    return dfGrouped
    
if rank == 0:
    comm.send(1, dest = 1) # ciudad

if rank > 0:
    num = comm.recv(source = 0)
    dfR = reduce(num)
    print(dfR.to_string())