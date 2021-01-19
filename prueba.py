import re
from simulated_annealing import optimizar
from dominio_tsp import DominioTSP
from math import e


def matriz():

        regex = r"(.*?),|(.*?)\n"
        matriz=[]

        fic=open("datos/ciudades_cr_pruebas.csv", "r")
        lines=fic.readline()
        fic.close

        matches = re.finditer(regex, lines, re.MULTILINE)

        for match in matches:
            palabra=match.group()
            palabra=palabra[:-1]
            matriz.append(palabra)
            
        print(matriz)


# print(e)
dominio = DominioTSP('datos/ciudades_cr.csv', 'Cartago')
solucion=optimizar(dominio)
print(solucion)
# tsp.validar(solucion)
# tsp.texto(solucion)
# # tsp.fcosto(solucion)
# tsp.vecino(solucion)
    
# matriz()