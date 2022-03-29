lista = [80,34,80,23,70];
mayor = 0

for i in range(len(lista)):
    aux = lista[i]
    for j in range(i+1,len(lista)):
        suma = aux + lista[j]
        if(suma<=150):
            print("Peso de",aux,"+",lista[j],"=",suma)
            if(mayor < suma):
                mayor = suma
print("El peso maximo posible es: ",mayor)

