def imprimir(dic):
    for indice in dic:
        print("Key:",indice,"Value:",dic[indice])

def agregarEtudiante(dic,codigo,nombre):
    dic[codigo]=[]
    dic[codigo].append(nombre)
    dic[codigo].append([])

def agregarNotas(dic,codigo,nota):
    dic[codigo][1] += [nota]

def promedio(lista):
    suma = 0
    for item in lista:
        suma+= item
    return suma/len(lista)

dic ={}
imprimir(dic)
agregarEtudiante(dic,"001","kevin")
agregarNotas(dic,"001",10)
agregarNotas(dic,"001",8)
imprimir(dic)
print(promedio(dic["001"][1]))


