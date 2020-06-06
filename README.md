# Proyecto 4: High Performance Computing - HPC

### Autores
- Sebastian Ortiz Serna
- Sebastian Ramrez Lopez
- Stefania Zapata Osorio

## Ejecución de codigos. 

primero se decide cual se va a usar si es el serial o secuencial, los comandos respectivos son: 
```
$ cd serial 
o
$ cd openmp
o
$ cd mpi
```
luego se selecciona el código a ejecutar en caso de serial tomamos el acc_por_ciudad.py 

```
$ py acc_por_ciudad.py 
``` 
luego para ejecutar la prueba de tiempo se usa el siguiente comando 

```
$ time python acc_por_ciudad.py 
``` 

para los ejemplos mpi usamos para ejecutar 

```
$ mpiexec -n 4 python script.py
``` 

para medir el tiempo usamos

```
$ time mpiexec -n 4 python script.py
``` 

en el caso de los openmp usamos para ejecutar 

```
$ python3 accidentes_omp.py
``` 



