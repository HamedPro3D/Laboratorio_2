class Nodo:
  def __init__(self,ptr):
    self.ptr = ptr
    self.next = None
  def SumarLista(ptr):
    sum = 0
    actual = ptr
    while(actual != None):
      sum = sum + actual.ptr
      actual = actual.next
    return "La suma es: ",sum
  
  def MultiplicacionLista(ptr):
    mult = 1
    actual = ptr
    while(actual != None):
      mult = mult * actual.ptr
      actual = actual.next
    return "La multiplicacion es: ",mult
      

num1 = Nodo(1)
num2 = Nodo(2)
num3 = Nodo(3)
num4 = Nodo(4)

num1.next = num2
num2.next = num3
num3.next = num4

Nodo.SumarLista(num1)
Nodo.MultiplicacionLista(num1)
print(Nodo.SumarLista(num1))
print(Nodo.MultiplicacionLista(num1))