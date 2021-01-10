import re
from dominio_tsp import DominioTSP

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
            
        print( matriz)



# tsp = DominioTSP('datos/ciudades_cr_pruebas.csv', 'Cartago')
# solucion=tsp.generar()
# print(solucion)
# # tsp.validar(solucion)
# tsp.texto(solucion)
# # tsp.fcosto(solucion)
# tsp.vecino(solucion)
    
# matriz()