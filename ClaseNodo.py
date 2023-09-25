class Nodo(): 
    __dato : object 
    __izquierda : object 
    __derecha : object 
    
    
    def __init__(self,dato): 
        self.__dato = dato 
        self.__izquierda = None 
        self.__derecha = None 
        
    
    def get_dato(self): 
        return self.__dato
    
    def get_izquierda(self): 
        return self.__izquierda
    
    def get_derecha(self): 
        return self.__derecha 
    
    def set_izquierda(self,izquierda):
        self.__izquierda = izquierda 
        
    def set_derecha(self,derecha): 
        self.__derecha = derecha 
         
    def es_hoja(self): 
        return self.__izquierda == None and self.__derecha == None 
    
    