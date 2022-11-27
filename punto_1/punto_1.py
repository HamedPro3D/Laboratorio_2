from listaenlazada import ListaEnlazada

lista1 = ListaEnlazada()
print("Escriba 'Sumar' para sumar listas")
print("Escriba 'Multiplicar' para sumar listas")
op = input("Escoja: ")

if (op == "sumar" or op == "Sumar"):
  print("Sumar listas: ")
  lista1.Orden1(ListaEnlazada())
else:
  if (op == "Multiplicar" or "multiplicar"):
    print("Multiplicar listas: ")
    lista1.Orden2()