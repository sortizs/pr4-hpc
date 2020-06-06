from mpi4py import MPI
import pandas as pd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#se lee el archivo
df = pd.read_csv('../dataset/datos.csv', delimiter = ';')
df.head()

#se filtran los datos por ciudad
dfMunicipio = df.filter(items = [df.columns[7]])

#se agrupan los datos
dfGrouped = dfMunicipio.groupby([dfMunicipio.columns[0]]).size()
