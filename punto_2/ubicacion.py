#Organizacion del output
class Ubicacion:
    def __init__(self, nombre: str, school: int, gym: int, bar: int, shop: int, parque: int):   
        self.informacion = {"nombre": nombre, "escuela": school, "gimnasio": gym, "bar": bar, "tienda": shop, "parque": parque}
        self.prioridad = 0
    #Convierte todos los datos en un string para mostrarlo
    def __str__(self) -> str:
        return self.informacion
