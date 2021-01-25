from dominio import Dominio
import random as rd
import collections
from datos import crear_datos
import re
import random
import csv

class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """
        # self.ciudades, self.i_ciudades = crear_datos(ciudades_rutacsv)
        # self.n_ciudades = len(self.ciudades)
        # self.nombre_ciudad_inicio = ciudad_inicio
        # self.i_ciudad_inicio = self.i_ciudades[ciudad_inicio]

        # # Pendiente: implementar este constructor
        # pass


        matr=[]
        with open(ciudades_rutacsv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                matr.append(row)

        self.matriz=matr
        self.ciudades_rutacsv=ciudades_rutacsv
        self.ciudad_inicio=ciudad_inicio


        

    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.
        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """
        # repetidos = [x for x, y in collections.Counter(sol).items() if y > 1]

        # Pendiente: implementar este método
        # pass
        isValid=True
        matriza=self.matriz
        numCiudades=len(matriza)-1

        fila=matriza[0]
        ciudadSalida=fila.index(self.ciudad_inicio)-1

        a=1
        for i in sol:
            # contener numeros menores a n
            if i >=numCiudades:
                isValid= False
            # no tener repetidos
            if i in sol[a:]:
                isValid= False
                # print(sol[a:])
            a=a+1

        
        # tamaño n-1
        if (len(sol))!=(numCiudades-1):
            # print("aqui")
            isValid= False
        # contener la cuidad de inicio
        elif ciudadSalida in sol:
            isValid= False

        # print(isValid)
        return isValid


    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """
        # formato_legible = self.nombre_ciudad_inicio + " -> "
        # for ciudad in sol:
        #     nombre_actual = self.ciudades[ciudad]['km/min']
        #     formato_legible += nombre_actual + " -> "
        # formato_legible += self.nombre_ciudad_inicio
        # return formato_legible

        # Pendiente: implementar este método
        # pass


        matriza=self.matriz
        ruta=""
        ruta=ruta+(self.ciudad_inicio)+" -> "
        var1=matriza[0].copy()

        for i in sol:
            ruta=ruta + (var1.pop(i+1))+" -> "
            var1=matriza[0].copy()

        ruta=ruta+(self.ciudad_inicio)

        # print(ruta)
        return ruta


    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """
        # sol =  list(range(0,self.n_ciudades))
        # del sol[self.i_ciudad_inicio]
        # rd.shuffle(sol)        
        # return sol

        # # Pendiente: implementar este método
        # pass
        matriza=self.matriz
        fila=matriza[0]
        noTomar=fila.index(self.ciudad_inicio)-1

        solucion=random.sample(range(len(fila)-1), len(fila)-1)
        solucion.remove(noTomar)

        # remueve el valor de km/min
        # print(fila)
        # print(solucion)

        return solucion



    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.
    
        Entradas:
        sol (list)
        Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """
        # primera_visitada = self.ciudades[sol[0]]["km/min"]
        # costo_ruta = float(self.ciudades[self.i_ciudad_inicio][primera_visitada])

        # Pendiente: implementar este método
        # pass
        matriza=self.matriz
        costo=0
        primeraCiudad=self.ciudad_inicio

        ciudadSalida=matriza[0].index(primeraCiudad)

        primeraCiudad=ciudadSalida

        for i in sol:
            costo=costo+float(matriza[ciudadSalida][i+1])
            ciudadSalida=i+1

        costo=costo+float(matriza[ciudadSalida][primeraCiudad])
        # print(costo)
        return costo



    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con
        la solución que la origina, aunque no son exactamente iguales. El
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """


        vecino=sol.copy()
        # limiteCambios=(len(vecino)//2)-1
        # while limiteCambios>0:
        while vecino==sol:
            num1=random.randint(0, len(vecino)-1)
            num2=random.randint(0, len(vecino)-1)
            numeroSaca=0

            if num1!=num2:
                numeroSaca=vecino[num1]
                vecino[num1]=vecino[num2]
                vecino[num2]=numeroSaca

        return vecino

        # temp = sol.copy()
        # cambio_invalido = True
        # cambios = 3
        # while cambio_invalido or cambios == 0:
        #     # i,j = rd.randint(0,self.n_ciudades-2),rd.randint(0,self.n_ciudades-2)
        #     i,j = rd.randint(0,len(self.matriz)-2),rd.randint(0,len(self.matriz)-2)
        #     temp[i],temp[j] = temp[j],temp[i]
        #     cambio_invalido = True
        #     if temp != sol:
        #         cambio_invalido = False
        #     cambios -=1
        # return temp


    