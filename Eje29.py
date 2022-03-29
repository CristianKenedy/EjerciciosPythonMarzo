def imprimir(dic):
    for indice in dic:
        print("Producto:",indice,"Precio:",dic[indice])

dic = {}
dic["pan"]=.12
dic["queso"] = 2
total = 0 
menu = True

while menu:
    op = int(input("Elija una opcion\n1.-Agregar Producto\n2.-Facturar\n3.-Salir\n"))
    if op == 1:
        indice = input("Ingrese el indice: ")
        valor = float(input("Ingrese el valor: "))
        dic[indice] = valor
        print(dic)
    elif op==2:               
        factura = True
        while factura:
            imprimir(dic)
            print("Elija una opcion\n1.-Agregar a Factura\n2.-Finalizar")
            opf=int(input())
            if(opf==1):
                indice = input("Ingrese el producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                if(dic.get(indice) is None):
                    print("Producto no encontrado")
                else:                    
                    total += float(dic.get(indice))*cantidad
                    print("El total es: ",str(total))
            else:
                factura = False
    elif op == 3:
        menu = False
    else:
        print("Ingrese una opcion valida")