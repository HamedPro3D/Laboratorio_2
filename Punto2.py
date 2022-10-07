from asyncore import write
import csv
print("Solo escribir s para sí, n para no")
escuela = input("¿Quiere un vecindario con escuela? ")
gimnasio = input("¿Quiere un vecindario con gimansio? ")
bar = input("¿Quiere un vecindario con bar? ")
tienda = input("¿Quiere un vecindario con tienda? ") 
parque = input("¿Quiere un vecindario con parque? ")
acc = list()
with open("data.csv") as f:
    lector = csv.reader(f)
    for row in lector:
        #Se puede reducir todos los ifs
        if(row[1] == "1"):
            row[1] = "Si"
        if(row[1] == "0"):
            row[1] = "No"
            comp = True    
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
        acc.append(row)
        print("Vecindario: {0}, Escuela: {1}, Gimnasio: {2}, Bar: {3}, Tienda: {4}, Parque: {5} ".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    

with open("lista.csv","w") as file:
    escritor = csv.writer(file)
    for row in acc:
        if(row[1] == "No"):
            if(escuela == "n"):
                a = 'Sin escuela'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[1]))
        if(row[1] == "Si"):
            if(escuela == "s"):
                a = 'Con escuela'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[1]))
        if(row[2] == "No"):
            if(gimnasio=="n"):
                a = 'Sin gimnasio'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[2]))
        if(row[2] == "Si"):
            if(gimnasio == "s"):
                a = 'Con gimnasio'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[2]))
        if(row[3] == "Si"):
            if(bar=="s"):
                a = 'Con bar'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[3]))
        if(row[3] == "No"):
            if(bar=="n"):
                a = 'Sin bar'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[3]))
        if(row[4] == "Si"):
            if(tienda=="s"):
                a = 'Con tienda'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[4]))
        if(row[4] == "No"):
            if(tienda=="n"):
                a = 'Sin tienda'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[4]))
        if(row[5] == "Si"):
            if(parque=="s"):
                a = 'Con parque'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[5]))
        if(row[5] == "No"):
            if(parque=="n"):
                a = 'Sin parque'
                escritor.writerow((a,))
                escritor.writerow((row[0],row[5]))
    
        

