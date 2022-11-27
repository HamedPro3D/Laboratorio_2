#Metodo encargado de tomar todos los conjuntos de numeros
def Conjuntos(): 
  sw = True
  print("desde 1 digito")
  temp = int(input("¿Cuantos numeros utilizara?"))
  while temp < 1:
    temp = int(input("Cantidad de numeros utilizados: "))
  conjunto = [] 
  aux = 0
  print("El numero debe ser de 1 a 100 cifras")
  num = int(input("Cantidad de numeros utilizados: "))
  if num >= 101:
    print("El numero no puede pasar de 100 digitos")
  while num < 1 or num > 100:
    num = int(input("Cantidad de numeros utilizados: "))
  for i in range(0, temp):
    sw = True
    print("El numero debe tener ",num," digitos")
    aux = int(input("¿Cual es el numero?"))
    if temp == 1:
      print("El resultado es",aux," ya que solo es 1 digito")
    if(aux<0):
      t = str(aux).split("-")
      aux = t[1]
      sw = False
    while(len(str(aux)) != num):
      print("El debe tener",num," cifras")
      aux = int(input("Digite un num correcto"))
    if sw:
      conjunto.append(aux)
    else:
      conjunto.append(int(aux) * -1)
  print(conjunto)
  return conjunto
#Elimina el ultimo numero y lo apunta a Nulo
def Eliminar(aux): 
    p1 = []
    temp = ""
    for i in str(aux):
        p1.append(i)
    for j in range(0, (len(p1) - 1)):
        temp = temp + p1[j]
    temp = int(temp)
    return temp
#Da el ultimo numero de la lista que no es Nulo
def Ultimo(aux): 
  p1 = []
  temp = ""
  for i in str(aux):
    p1.append(i)
  temp = temp + p1[(len(p1) - 1)]
  temp = int(temp)
  return temp