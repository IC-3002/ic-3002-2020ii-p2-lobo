import re
#from simulated_annealing import optimizar
#from dominio_tsp import DominioTSP
from dominio_ag_tsp import DominioAGTSP
from algoritmo_genetico import optimizar
from math import e



# print(e)
"""
temperatura = 10000
enfriamiento = [0.8,0.9,0.95,0.99]

dominio = DominioTSP('datos/ciudades_cr.csv', 'Alajuela')

while(temperatura < 10000000):
    for tasa in enfriamiento:
        solucion = optimizar(dominio,temperatura,tasa) 
        print("Temperatura: ", temperatura, ", Enfriamiento: ", tasa)
        print("Solucion: ", solucion, "\n")

    temperatura = temperatura/0.2        

"""
    
    
    
poblacion = 100
elite = 0.01
mutacion = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
reps = 1000
test = False

dominio = DominioAGTSP('datos/ciudades_cr.csv', 'Alajuela')

#         (dominio, 100,        0.1,        0.5,    1000, False)
#optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps, testeo):

while(poblacion <= 1000):
    for p in mutacion:
        solucion = optimizar(dominio,poblacion,elite,p,reps,test) 
        print("poblacion: ", poblacion, ", mutacion: ", p)
        print("Solucion: ", solucion, "\n")
    poblacion = poblacion + 100        
    