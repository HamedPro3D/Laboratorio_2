from ubicacion import *

#Clase creadora de nodos
class Nodo:
    def __init__(self, dato: Ubicacion) -> None:
        self.dato = dato
        self.siguiente = None
#Lista Enlazada
class ListaEnlazada:
    def __init__(self) -> None:
        self.PRIMERO = None
        self.tamañol = 0
    #Aca se añaden los  nodos y se ubican
    def Añadir_Nodo(self, nodo: Nodo) -> None:
        if self.PRIMERO == None:
            self.PRIMERO = nodo
            return
        aux = self.PRIMERO
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = nodo
        self.tamañol += 1
    #Transforma todo los valores a string para su impresion
    def __str__(self) -> str:
        aux = self.PRIMERO
        lista = ""
        while aux:
            lista += f" {aux.dato}"
            aux = aux.siguiente
        return lista
    #Vemos si la lista esta vacia
    def vacia(self):
        return self.PRIMERO == None
    #Se recorre la lista para administrar si esta bien unida
    def recorrer(self):
        if self.vacia():
            print("La lista esta vacia")
            return
        aux = self.PRIMERO
        while aux:
            print(aux.dato)
            aux = aux.siguiente
