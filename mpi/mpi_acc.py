from mpi4py import MPI
import pandas as pd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

df = pd.read_csv('../dataset/datos.csv', delimiter = ';')
df.head()

if rank == 0:
    comm.send(1, dest = 1) # ciudad
    comm.send(5, dest = 2) # clase
    comm.send(4, dest = 3) # dia
    comm.send(7, dest = 4) # gravedad
if rank == 1:
    num = comm.recv(source = 0)
    dfMunicipio = df.filter(items = [df.columns[num]])
    dfGrouped = dfMunicipio.groupby([dfMunicipio.columns[0]]).size()
    print("Finaliza: ciudad")
if rank == 2:
    num = comm.recv(source = 0)
    dfClase = df.filter(items = [df.columns[num]])
    dfGrouped = dfClase.groupby([dfClase.columns[0]]).size()
    print("Finaliza: clase")
if rank == 3:
    num = comm.recv(source = 0)
    dfDia = df.filter(items = [df.columns[num]])
    dfGrouped = dfDia.groupby([dfDia.columns[0]]).size()
    print("Finaliza: dia")
if rank == 4:
    num = comm.recv(source = 0)
    dfGrav = df.filter(items = [df.columns[num]])
    dfGrouped = dfGrav.groupby([dfGrav.columns[0]]).size()
    print("Finaliza: gravedad")
