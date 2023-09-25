from ClaseNodo import Nodo
class Arbol(): 
    __raiz : Nodo
    

    def __init__(self): 
        self.__raiz = None 
        
    def insertar(self,dato):
        if self.__raiz == None: 
            self.__raiz = Nodo(dato)
        else: 
            self.__insercion_recursiva(self.__raiz,dato)
             
    def __insercion_recursiva(self,nodo:Nodo,dato): 
        if dato>nodo.get_dato(): 
            if nodo.get_derecha!=None:
                return self.__insercion_recursiva(nodo.get_derecha(),dato)
            else: 
                nodo.set_derecha(Nodo(dato))
                return True
            
        elif dato<nodo.get_dato():
            if nodo.get_izquierda()!=None: 
                return self.__insercion_recursiva(nodo.get_izquierda(),dato)
            else: 
                nodo.set_izquierda(Nodo(dato))
                return True
        else: 
            return None 
        
    def inOrden(self): 
        if self.__raiz != None: 
            print("El arbol está vacio")
        else: 
            self.__inOrdenRecursivo(self.__raiz)
            
    def __inOrdenRecursivo(self,nodo:Nodo):
        if nodo != None: 
            self.__inOrdenRecursivo(nodo.get_izquierda())
            print(nodo.get_dato())
            self.__inOrdenRecursivo(nodo.get_derecha())
            
            
if __name__=='__main__': 
    ab=Arbol()
    
    ab.insertar(15)
    ab.insertar(9)
    ab.insertar(23)
    ab.insertar(3)
    ab.insertar(17)
    ab.insertar(28)
    ab.insertar(12)
    ab.insertar(8)
    ab.inOrden()