from funcionamiento import *
#Clase que almacena los nodos
class Nodo(): 
  def __init__(self, dato): 
    self.dato = dato
    self.siguiente = None

#Creacion de la lista
class ListaEnlazada(): 
    def __init__(self): 
        self.PRIMERO = None 
        self.ULTIMO = None
    #Verificando que la lista no este vacia
    def vacia(self):
        return self.PRIMERO == None
    #Añadiendo un nodo
    def Añadir_Nodo(self, dato): 
      #Añade un nodo al principio de la lista.
      aux = Nodo(dato)
      if(self.PRIMERO == None):
        self.ULTIMO = aux
      aux.siguiente = self.PRIMERO
      self.PRIMERO = aux
    #Sirve para borrar un nodo
    def Eliminar(self, target):
        aux = self.PRIMERO 
        temp = None 
        while(aux.dato != target and aux != None):
            temp = aux 
            aux = aux.siguiente 
        if(aux == self.PRIMERO): 
            self.PRIMERO = aux.siguiente 
            aux.siguiente = None 
            aux = self.PRIMERO 
        else:
            if(aux == self.ULTIMO):
                self.ULTIMO = temp 
                aux = self.ULTIMO 
                aux.siguiente = None
            try:
                if(aux.dato == target):
                    temp.siguiente = aux.siguiente 
                    aux.siguiente = None 
                    aux = temp.siguiente 
            except:
                print("No se encontro el dato")
    #Elimina una lista
    def EliminarL(self):
      aux = self.PRIMERO
      while (aux != None):
        self.Eliminar(aux.dato)
        aux = self.PRIMERO
    #Recorre y printea la lista
    def recorrer(self):
        if self.vacia():
            print("La lista esta vacia")
            return
        aux = self.PRIMERO
        while aux:
            print(aux.dato, "->")
            aux = aux.siguiente
    #Invierte el orden de la lista
    def Invertir(self):
        aux = self.PRIMERO
        TEMP = self.ULTIMO
        p1 = None
        while (TEMP != self.PRIMERO):
            if(aux == TEMP):
                aux.siguiente = p1
                TEMP = p1
                p1 = None
                aux = self.PRIMERO
            else:
                p1 = aux
                aux = aux.siguiente
        aux = self.PRIMERO
        TEMP = self.ULTIMO
        aux.siguiente = None
        self.PRIMERO = TEMP
        self.ULTIMO = aux
    #Despues de invertirse, se ordena para el usuario
    def Ordenar(self):
      aux = self.PRIMERO
      temp = self.PRIMERO
      p1 = 0
      while(aux != None):
        temp = aux
        temp = temp.siguiente
        while(temp != None):
          if(aux.dato > temp.dato):
            p1 = aux.dato
            aux.dato = temp.dato
            temp.dato = p1
          temp = temp.siguiente
        aux = aux.siguiente
     #Lo utilizo para despues de juntadas las listas y sumadas este las agrupa en el primer conjunto
    def Orden1(self, lista2):
      conjuntos = Conjuntos()
      p1 = True
      p2 = True
      aux = True
      temp = False
      t = 0
      for i in range(len(conjuntos)-1):
        if aux:
          for j in range(len(str(conjuntos[i]))):
            if p1:
              t = conjuntos[i]
              if t < 0:
                temp = True
                t *= -1
              p1 = False
            if len(str(t)) > 1:
              if temp and t % 10 != 0:
                node = Ultimo(t)
                node *= -1
              else:
                node = Ultimo(t)
              self.Añadir_Nodo(node)
              t = Eliminar(t)
            else:
              if temp:
                self.Añadir_Nodo(t*(-1))
              else:
                self.Añadir_Nodo(t)
              aux = False
              temp = False
              break
        for k in range(len(str(conjuntos[i+1]))):
          if p2:  
            t = conjuntos[i+1]
            if t < 0:
              temp = True
              t *= -1
            p2 = False
          if len(str(t)) > 1:
            if temp and t % 10 != 0:
              node = Ultimo(t)
              node *= -1
            else:
              node = Ultimo(t)
            lista2.Añadir_Nodo(node)
            t = Eliminar(t)
          else:
            if temp:
              lista2.Añadir_Nodo(t*(-1))
            else:
              lista2.Añadir_Nodo(t)
            p2 = True
            temp = False
            break
        self.Invertir()
        lista2.Invertir()
        self.Sumar(lista2)
        lista2.EliminarL()
        print("Lista: ")
        self.recorrer()
        resultado = self.UnirLista()
        print("El resultado es: ",resultado)
    #Lo utilizo para despues de juntadas las listas y sumadas este las agrupa en el segundo conjunto
    def Orden2(self):
      conjuntos = Conjuntos()
      lista = ListaEnlazada()  
      p1 = True
      sw = True
      temp = False
      aux = 0
      for i in range(len(conjuntos)-1):
        if(sw):
          for j in range(len(str(conjuntos[i]))):
            if(p1):
              aux = conjuntos[i]
              if aux < 0:
                temp = True
                aux *= -1
              p1 = False
            if len(str(aux)) > 1:
              if temp and aux % 10 != 0:
                node = Ultimo(aux)
                node *= -1
              else:
                node = Ultimo(aux)
              self.Añadir_Nodo(node)
              lista.Añadir_Nodo(node)
              aux = Eliminar(aux)
            else:
              if temp:
                self.Añadir_Nodo(aux*(-1))
                lista.Añadir_Nodo(aux*(-1))
              else:
                self.Añadir_Nodo(aux)
                lista.Añadir_Nodo(aux)
              sw = False
              temp = False
              break   
      l2 = conjuntos[1]
      if l2 < 0:
        l2 *= -1 
      self.Multiplicar(lista, l2)
      print("Lista")
      self.recorrer()
      print("Resultado")
      x = self.UnirLista()
      print(x)
    #Aca es donde se multiplica par hacer la segunda opcion
    def Multiplicar(self, q, n):
      sw = True
      if n == 0:
        self.EliminarL()
        self.Añadir_Nodo(0)
        sw = False  
      if sw:
        q.Invertir()
        for i in range(n-1):
          self.Invertir()
          self.Sumar(q)
    #Suma las listas
    def Sumar(self,lista2):
      aux = self.PRIMERO
      p1 = lista2.PRIMERO
      p2 = self.Contador()
      p3 = lista2.Contador()
      p4 = p2 - p3
      for i in range(p4):
        lista2.Añadir_Nodo(0)
      sw = 0 
      temp = 0
      while(aux != None):
        if(aux.dato <= p1.dato and aux.dato < 0 and 
           self.ULTIMO.dato*(-1) < lista2.ULTIMO.dato):
             if aux.dato < 0 or p1.dato < 0:
              temp = aux.dato
              aux.dato = p1.dato
              p1.dato = temp
        if(aux.dato > p1.dato and p1.dato *(-1) > aux.dato and 
           aux.dato > 0 and self.ULTIMO != aux):
             if p1.dato < 0:
               aux.dato += 10 
               aux.siguiente.dato -= 1
        if(p1.dato > aux.dato and aux.dato*(-1) < p1.dato and 
           p1.dato > 0 and self.ULTIMO != aux):
            if aux.dato < 0:
              aux.dato -= 10 
              aux.siguiente.dato += 1
        aux.dato = aux.dato + p1.dato
        if(aux.dato > 9):
          sw = Ultimo(aux.dato)
          aux.dato = Ultimo(aux.dato)
          if(aux.siguiente == None):
            self.Añadir_Nodo(0)
            lista2.Añadir_Nodo(0)
            aux.siguiente.dato += sw
          else:
            aux.siguiente.dato += sw
        if(aux.dato < -9):
          sw = Ultimo(aux.dato)
          aux.dato = Ultimo(aux.dato)
          if(aux.siguiente == None):
            self.Añadir_Nodo(0)
            lista2.Añadir_Nodo(0)
            aux.siguiente.dato += sw
          else:
            aux.siguiente.dato += sw
        aux = aux.siguiente; p1 = p1.siguiente
      self.Invertir()
      if(self.PRIMERO.dato == 0):
        self.Eliminar(0)
    #Se utiliza para poder saber el tamaño de la lista 
    def Contador(self):
      aux = self.PRIMERO
      sw = 0
      while(aux != None):
        sw += 1
        aux = aux.siguiente
      return sw
    #Une las listas creadas en los conjuntos
    def UnirLista(self):
      aux = self.PRIMERO
      temp = ""
      while(aux != None):
        if(aux.dato < 0 and aux != self.PRIMERO):
          aux.dato *= -1
        temp = temp + str(aux.dato)
        aux = aux.siguiente
      return temp

       
    
