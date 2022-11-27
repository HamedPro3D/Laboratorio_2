from clasificador import *
from listaenlazada import *
from asyncore import *

#Toma los archivos del csv para leerlos
def archivo() -> ListaEnlazada: 
    ubicacion = "./punto_2/data.csv"
    lista = ListaEnlazada()
    with open(ubicacion, "r") as archivo:
        next(archivo)
        for i in archivo:   
            datos = i.rstrip().split(",")
            lugar = Ubicacion(datos[0], int(datos[1]), int(datos[2]), int(datos[3]), int(datos[4]), int(datos[5]))
            lista.Añadir_Nodo(Nodo(lugar))
    
    return lista
# Prioridad de cada barrio segun lo que se escogio
def Prioridades(ubicaciones: ListaEnlazada, lugares: list) -> tuple: 
    prioridades = [30, 25, 20, 15, 10]
    mejores = sum(prioridades[:len(lugares)])
    aux = ubicaciones.PRIMERO 
    while aux: 
        i = 0
        for lugar in lugares: 
            if aux.dato.informacion.get(lugar) == 1: 
                aux.dato.prioridad += prioridades[i]
            i += 1
        aux = aux.siguiente
    
    return (ubicaciones, mejores)

lista = ListaEnlazada()

print("¿Que necesidades tienes?")
print("Escoja de 1 en 1 o separe su eleccion por una ','")
lugares = input("Gimnasio, Bar, Tienda, Parque, Escuela: ").split(",")
lugar = archivo()
lugar_prioridad = Prioridades(lugar, lugares)
lugar_seleccionados = Lugares(lugar_prioridad[0], lugar_prioridad[1])
p = 0
for p in range (10):
  lista = lugar_seleccionados[p]
escritor = str(lugar_seleccionados)
print(lugar_seleccionados)
arch = open("lista.txt","a")
arch.write(escritor)
