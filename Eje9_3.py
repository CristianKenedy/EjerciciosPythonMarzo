hora = 17
minutos = 59
segundo = 59
print("La hora es: ",hora,":",minutos,":",segundo)

if(hora<=23 and minutos<=59 and segundo<=59):
    segundo+=1
    if(segundo==60):
        minutos+=1
        segundo=0
    if(minutos==60):
        minutos=0
        hora+=1
    if(hora==24):
        hora=0
    print("La hora un segundo despues es: ",hora,":",minutos,":",segundo)
else: 
    print("Ingrese una hora valida")
