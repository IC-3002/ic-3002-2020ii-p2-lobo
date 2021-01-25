import re
from simulated_annealing import optimizar
from dominio_tsp import DominioTSP
from math import e



# print(e)
dominio = DominioTSP('datos/ciudades_cr_pruebas.csv', 'Cartago')
solucion=optimizar(dominio)
print(solucion)
# tsp.validar(solucion)
# tsp.texto(solucion)
# # tsp.fcosto(solucion)
# tsp.vecino(solucion)
    
# matriz()