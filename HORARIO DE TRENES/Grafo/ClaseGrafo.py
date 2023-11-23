from queue import PriorityQueue

from typing import Any, List, Tuple

from .ClaseArista import Arista
from .ClaseNodo import Nodo

class Grafo:

    __cantVertices:int
    __adyacencia:list
    __vertices:list

    def __init__(self, cantVertices:int):
        self.__cantVertices = cantVertices
        self.__vertices = dict()
        self.__adyacencia = dict()

    def insertarVertices(self, vertices:list):
        if not (isinstance(vertices, list) and len(vertices) == self.__cantVertices):
            msj = f"Error en insertarVertices: Se espera una lista con {self.__cantVertices} elementos."
            raise Exception(msj)
        else:
            for vertice in vertices:
                if vertice in self.__adyacencia:
                    msj = f"Error en insertarVertices: {vertice} ya fue registrado."
                else:
                    self.__vertices[vertice] = Nodo(vertice)
                    self.__adyacencia[vertice] = list()
    
    def insertarAristas(self, aristas:list):
        if not isinstance(aristas, list):
            msj = "Error en insertarVertices: Se espera una lista."
            raise Exception(msj)
        else:
            for arista in aristas:
                if arista[0] in self.__adyacencia and arista[1] in self.__adyacencia:
                    listaAdyacencia = self.__adyacencia[arista[0]]
                    if not arista[1] in listaAdyacencia:
                        listaAdyacencia.append(Arista(self.__vertices[arista[1]], arista[2]))
                elif not arista[0] in self.__adyacencia:
                    msj = f"Error en insertarVertices: {arista[0]} no es un vertice."
                    raise Exception(msj)
                else:
                    msj = f"Error en insertarVertices: {arista[1]} no es un vertice."
                    raise Exception(msj)

    def camino(self, valorVerticeOrigen:Any, valorVerticeDestino:Any):
        caminoRecomendado = ("No hay camino, tocará patear",0)
        if not valorVerticeOrigen in self.__adyacencia:
            print(f"Error en camino: ({valorVerticeOrigen}) no es un vertice.")
        elif not valorVerticeDestino in self.__adyacencia:
            print(f"Error en camino: ({valorVerticeDestino}) no es un vertice.")
        elif valorVerticeOrigen == valorVerticeDestino:
            camino =  ("Jejeje, ahi estas parado", 0)
        else:
            dicciDistancia = dict((key,1000000) for key in self.__adyacencia.keys())
            dicciDistancia[valorVerticeOrigen] = 0
            visitados = set()
            camino = dict()
            pendientes = PriorityQueue()
            pendientes.put((0,valorVerticeOrigen))
            while not pendientes.empty():

                costo , valorVerticePadre = pendientes.get()
                visitados.add(valorVerticePadre)
                for arista in self.__adyacencia[valorVerticePadre]:
                    if not arista.getValorVertice() in visitados:
                        if costo+arista < dicciDistancia[arista.getValorVertice()]:
                            nuevoCosto = costo + arista
                            dicciDistancia[arista.getValorVertice()] = nuevoCosto
                            camino[arista.getValorVertice()] = valorVerticePadre
                            pendientes.put((nuevoCosto,arista.getValorVertice()))

            if valorVerticeDestino in camino:    
                parada = valorVerticeDestino
                costoTraslado = dicciDistancia[parada]
                caminoCorto = [parada]
                while parada != valorVerticeOrigen:
                    parada = camino[parada]
                    caminoCorto.insert(0,parada)
                caminoRecomendado =  (caminoCorto,costoTraslado)
        return caminoRecomendado