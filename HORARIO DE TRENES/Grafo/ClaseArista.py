from .ClaseNodo import Nodo

class Arista:

    __nodoDestino:Nodo
    __peso:int

    def __init__(self, destino:Nodo, peso:int):
        self.__nodoDestino = destino
        self.__peso = peso
    
    def __eq__(self, otro):
        if isinstance(otro, Arista):
            return self.__nodoDestino == otro.__nodoDestino
    
    def __add__(self, otro):    
        if isinstance(otro, Arista):
            return self.__peso + otro.__peso
        elif isinstance(otro, (int,float)):
            return self.__peso + otro
    
    def __radd__(self, otro):
        return self.__add__(otro)
    
    def __gt__(self, otro):
        if isinstance(otro, Arista):
            return self.__peso > otro.__peso
        elif isinstance(otro, (int,float)):
            return self.__peso > otro
    
    def getValorVertice(self):
        return self.__nodoDestino.getDato()
    
    def getPeso(self):
        return self.__peso