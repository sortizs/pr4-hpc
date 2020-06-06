

## proyecto 4 hpc archivo PCAM

Curso tópicos en telemática 2020-1 

## Integrantes: 

Sebastian Ortiz Serna, Sebastian Ramirez Lopez, Stefania Zapata Osorio. 


## Introducción

En el presente proyecto se dedica a ser un caso de estudio en el cual se intenta dar solución a cuáles son los municipios mas afectados con accidentes de coches.  Esto se logra usando dataets del área metropolitana tomados de la página [datos abiertos](https://datosabiertos.metropol.gov.co/search/type/dataset)
de este tomando el dataset [Accidentalidad Valle de Aburra](https://datosabiertos.metropol.gov.co/dataset/accidentalidad-valle-de-aburrá) , el cual muestra los municipios, fechas, barrios, etc. En los que se presentan accidentes en toda el área.  Lo que hace el proyecto es generar un análisis de los datos para saber cual es el municipio más afectado. 

## Análisis 

En este proyecto se usan dos versiones para completar el problema, una de forma secuencial y la otra paralela, para este desarrollo se decidió usar Python, este permite usar mpi. 

**El análisis secuencial**

El código secuencial esta ubicado en la carpeta [serial](https://github.com/sortizs/pr4-hpc/tree/master/serial), en este tenemos el archivo acc_por_ciudad.py en este se obtiene el numero de accidentes por ciudad o municipio.  

El código paralelizado  es ubicado en la carpeta [paralelo](https://github.com/sortizs/pr4-hpc/tree/master/paralelo).  


tiempos 

conclusiones


## Metodología de desarrollo PCAM

Primero comencemos con el codigo de mpi, en este usamos las siguientes tareas. 

**Partición**.

**Tarea 1:** Extraer de datos del dataset.

**Tarea 2:** Enviar mensajes desde el proceso root.

**Tarea 3:** Seleccionar los registros por ciudad y enviarlos al método reducer (Proceso 1).

**Tarea 4:** Seleccionar los registros por clase y enviarlos al método reducer (Proceso 2).

**Tarea 5:** Seleccionar los registros por día y enviarlos al método reducer (Proceso 3).

**Tarea 6:** Seleccionar los registros por gravedad y enviarlos al método reducer (Proceso 4).

**Tarea 7:** Procesar los datos recibidos por cada proceso.

**Tarea 8:** Mostrar los resultados.

**Comunicación.**

<img align="center" width="600" height="300" src="https://github.com/sortizs/pr4-hpc/blob/master/images/diagrama-mpi.jpg?raw=true">

![alt text](https://github.com/sortizs/pr4-hpc/blob/master/images/diagrama-mpi.jpg?raw=true)

**Aglomeración.**

**Recolección:** Tarea 1.

**Procesamiento:** Tareas 2-7.

**Visualización:** Tarea 8.

**Mapeo.**

![alt text](https://github.com/sortizs/pr4-hpc/blob/master/images/mapeo-mpi.jpg?raw=true)



Luego seguimos con el OpenMP.

![alt text](https://github.com/sortizs/pr4-hpc/blob/master/images/diagrama-omp.jpeg?raw=true)
