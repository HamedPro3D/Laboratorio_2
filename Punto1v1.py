class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor)

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def añadir(self, valor):
        Minodo = Nodo(valor)
        if self.tamaño == 0:
            self.primero = Minodo
        else:
            actual = self.primero
            while(actual.siguiente != None):

                actual = actual.siguiente
            actual.siguiente = Minodo

        self.tamaño = self.tamaño + 1

        return Minodo

    def eliminar(self, valor):
        if self.tamaño == 0:
            return False
        else:
            actual = self.primero
            while((actual.siguiente.valor) != valor):
                if actual.siguiente == None:
                    return False
                else:
                    actual = actual.siguiente
            nodoeliminado = actual.siguiente
            actual.siguiente = nodoeliminado.siguiente
        self.tamaño = self.tamaño -1
        return nodoeliminado

    def sumar(self,valor):
        suma = 0
        if self.tamaño == 0:
            return 0
        else:
            actual = self.primero
            while(actual.siguiente != None):
                print(actual.valor)
                a = actual.valor
                suma = a + suma
                actual = actual.siguiente
            return "La suma es: ",suma

    def multiplicacion(self,valor):
        mult = 1
        if self.tamaño == 0:
            return 0
        else:
            actual = self.primero
            while(actual.siguiente != None):
                print(actual.valor)
                a = actual.valor
                mult = a * mult
                actual = actual.siguiente
            return "La multiplicacion es : ",mult

    def __len__(self):
        return self.tamaño

    def __str__(self):
        String = "["
        actual = self.primero
        while(actual != None):
            String = String + str(actual)
            String = String + str(",")
            actual = actual.siguiente
        String = String + "]"
        return String

    
Milista = ListaEnlazada()

Milista.añadir(1)
Milista.añadir(2)
Milista.añadir(3)
Milista.añadir(4)
Milista.añadir(None)



print(Milista.sumar(1))
print(Milista.multiplicacion(1))
#print(Milista)