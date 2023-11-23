from typing import Any

class Nodo:

    __dato:Any

    def __init__(self, dato:Any):
        self.__dato = dato

    def __eq__(self, otro):
        if isinstance(otro, self):
            return self.__dato == otro.__dato
    
    def getDato(self):
        return self.__dato