from listaenlazada import * 
from ubicacion import * 

#Se utiliza para encontrar el lugar con mayor prioridad
def Lugares(zona: ListaEnlazada, prioridad: int) -> list: 
    lugar = zona.PRIMERO.siguiente
    mejores_ubicaciones = []
    while len(mejores_ubicaciones) <= 10:
        aux = zona.PRIMERO.dato.prioridad 
        ubicacion = abs(aux - prioridad)
        temp = None
        while lugar:
            ubicacion_actual = abs(lugar.dato.prioridad - prioridad)
            if ubicacion_actual < ubicacion and temp not in mejores_ubicaciones: 
                aux = lugar.dato.prioridad 
                ubicacion = ubicacion_actual
                temp = lugar.dato.informacion
            lugar = lugar.siguiente
            if ubicacion == 0: 
                break
        mejores_ubicaciones.append(temp)
    
    return mejores_ubicaciones


