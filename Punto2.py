import csv
print("Solo escribir s para sí, n para no")
escuela = input("¿Quiere un vecindario con escuela? ")
gimnasio = input("¿Quiere un vecindario con gimansio? ")
bar = input("¿Quiere un vecindario con bar? ")
tienda = input("¿Quiere un vecindario con tienda? ") 
parque = input("¿Quiere un vecindario con parque? ")
with open("data.csv") as f:
    lector = csv.reader(f)
    for row in lector:
        #Se puede reducir todos los ifs
        if(row[1] == "1"):
            row[1] = "Si"
        if(row[1] == "0"):
            row[1] = "No"    
        if(row[2] == "1"):
            row[2] = "Si"
        if(row[2] == "0"):
            row[2] = "No"
        if(row[3] == "1"):
            row[3] = "Si"
        if(row[3] == "0"):
            row[3] = "No"
        if(row[4] == "1"):
            row[4] = "Si"
        if(row[4] == "0"):
            row[4] = "No"
        if(row[5] == "1"):
            row[5] = "Si"
        if(row[5] == "0"):
            row[5] = "No"
        print("Vecindario: {0}, Escuela: {1}, Gimnasio: {2}, Bar: {3}, Tienda: {4}, Parque: {5} ".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    with open("lista.csv","w",newline="") as file:
        escritor = csv.writer(file)
        if(escuela == "n"):
            escritor.writerow((row[0],escuela,gimnasio,bar,tienda,parque))

