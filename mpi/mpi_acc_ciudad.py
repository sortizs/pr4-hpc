from mpi4py import MPI
import pandas as pd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

df = pd.read_csv('../dataset/datos.csv', delimiter = ';')
df.head()

dfMunicipio = df.filter(items = [df.columns[1]])
dfGrouped = dfMunicipio.groupby([dfMunicipio.columns[0]]).size()
