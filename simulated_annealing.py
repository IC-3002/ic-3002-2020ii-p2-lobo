from math import e
import random

def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.99):
    """Algoritmo de optimización estocástica simulated annealing.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    temperatura (float/int)
        Temperatura inicial del algoritmo, se recomienda un número alto

    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteración, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    sol=dominio.generar()
    costo=dominio.fcosto(sol)
    cont=0
    while temperatura > 0.01:
        # print("Primera solución: "+' '.join(map(str,sol)))
        # print("Costo Primero: "+str(costo))
        sol1=dominio.vecino(sol)
        costo1=dominio.fcosto(sol1)
        # print("Primera solución vecino: "+' '.join(map(str,sol1)))
        # print("Costo Primero vecino: "+str(costo1))
        p=(e**(-(abs(costo1-costo)/temperatura)))
        pazar=random.uniform(0, 1)
        # print("p: "+str(p))
        # print("pazar: "+str(pazar))
        if costo1 < costo or pazar <= p:
            sol=sol1
            costo=costo1      
        temperatura = temperatura * tasa_enfriamiento
        cont=cont+1
        # print(str(temperatura))   
    #print("iteraciones: ", cont)
    return sol