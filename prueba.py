import re
#from simulated_annealing import optimizar
#from dominio_tsp import DominioTSP
from dominio_ag_tsp import DominioAGTSP
from algoritmo_genetico import optimizar
from math import e
from time import time



"""
temperatura = 10000
enfriamiento = [0.8,0.9,0.95,0.99]

dominio = DominioTSP('datos/ciudades_cr.csv', 'Alajuela')

while(temperatura < 10000000):
    for tasa in enfriamiento:
        solucion,cont = optimizar(dominio,temperatura,tasa) 
        print("|  17   |",  temperatura, "|", tasa,  "|",  round(solucion,3), "|", cont, "|")

    temperatura = temperatura/0.2        
"""

    
"""    
poblacion = 100
elite = 0.1
mutacion = [0.1,0.3,0.5,0.7,0.9]
reps = 1000
test = False

dominio = DominioAGTSP('datos/ciudades_cr.csv', 'Alajuela')

#         (dominio, 100,        0.1,        0.5,    1000, False)
#optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps, testeo):

while(poblacion <= 1000):
    for p in mutacion:
        solucion = optimizar(dominio,poblacion,elite,p,reps,test) 
        #print("poblacion: ", poblacion, ", mutacion: ", p)
        #print("Solucion: ", dominio.fcosto(solucion), "\n")
        print("|  16   |",   poblacion,  "|",  p,    "|",  round(dominio.fcosto(solucion),3), "|   1000 |")
       

    poblacion = poblacion + 200        
"""


#Annealing: 1250000.0	0.99	1762.4	1856    
#Genetico: 700	0.1	1675.0	1000
    


#Simualted Annealing


"""
dominio = DominioTSP('datos/ciudades_cr.csv', 'Alajuela')
for i in range(0,5):
    start_time = time()
    solucion = optimizar(dominio,1250000.0,0.99)
    elapsed_time = time() - start_time
    print("Elapsed time: %0.10f seconds." % elapsed_time)
"""


#Genetico

dominio = DominioAGTSP('datos/ciudades_cr.csv', 'Alajuela')
for i in range(0,5):
    start_time = time()
    solucion = optimizar(dominio,700,0.1,0.1,1000,False)
    elapsed_time = time() - start_time
    print("Elapsed time: %0.10f seconds." % elapsed_time)


