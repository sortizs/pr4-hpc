# Proyecto 4: High Performance Computing - HPC

### Autores
- Sebastian Ortiz Serna
- Sebastian Ramrez Lopez
- Stefania Zapata Osorio

## Ejecución de codigos. 

primero se decide cual se va a usar si es el serial o paralelo, los comandos respectivos son: 
```
$ cd serial 
```

```
$ cd openmp
```

```
$ cd mpi
```
luego se selecciona el código a ejecutar en caso de serial tomamos el acc_por_ciudad.py 

```
$ python3 acc_por_ciudad.py 
``` 
luego para ejecutar la prueba de tiempo se usa el siguiente comando 

```
$ time python3 acc_por_ciudad.py 
``` 

para los ejemplos mpi usamos para ejecutar 

```
$ mpiexec -n 4 python3 script.py
``` 

para medir el tiempo usamos

```
$ time mpiexec -n 4 python3 script.py
``` 

en el caso de los openmp usamos para ejecutar 

```
$ python3 accidentes_omp.py
``` 
y para medir el tiempo usamos 
```
$ time python3 accidentes_omp.py
``` 

En Google Drive se encuentra adjunto el documento con el detalle de los resultados obtenidos tras la ejecución de las pruebas, para abrirlo hacer clic [aquí](https://drive.google.com/drive/folders/1m4Jjiqmn6zKK2AvqdTQ76u6A12I0rJT6?usp=sharing).