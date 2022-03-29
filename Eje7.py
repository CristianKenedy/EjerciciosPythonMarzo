from random import randint
# randint(x,y)  numero aleatorio entero "x" y "y"
#random()       numero aleatorio entre o y 1
#randrange(x,y,p) numero aleatorio entero entre "x" y "y" y con un paso de "p"
#uniform(x,y)   numero aleatorio de tipo float entre "x" y "y"
zonaUsuario = int(input("¿En que zona desea disparar?: "))
zonaPortero = randint(1,6)

print("La zona cubierta por el portero es:",zonaPortero)

if(zonaUsuario == zonaPortero):
    print("No ha sido gol")
else:
    print("Goooool")