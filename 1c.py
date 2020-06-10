#Isabel Gómez Yareli Elizabeth 
#Zavala Estala Lisset
#Grupo 1 Criptografía

posicionesClave=[]
posicionesMensaje=[]
posicionesFinales=[]
posicionesMod=[]
posicionesMensajeCifrado=[]
poscionesCif=[]
mensaje=""
mensajeCifrado=""
mensajeClaro=""
abc="abcdefghijklmnñopqrstuvwxyz" #Definimos para mayúsculas
accion=input("Ingresa (c) cifrar o (d) descifrar: ")
if accion==("c" or "C"): #Verifica la opción seleccionada
    
    clave =input("Ingresa la clave:")
    clave=clave.lower()
    mensaje= input("Ingresa el mensaje:   ")
    mensaje=mensaje.lower()
    while len(mensaje)<len(clave):
        mensaje+="x"
    cifrado = ""
    textoCifrado = ""
    for letra in clave.lower():
        if letra in abc:
            posLetra=int(abc.index(letra))
            posicionesClave.append(posLetra)
    
    
    for letra in mensaje.lower():
        if letra in abc:
            posLetra=int(abc.index(letra))
            posicionesMensaje.append(posLetra)
            
    for i in range(len(posicionesClave)):
            posicionesFinales.append(posicionesClave[i]+posicionesMensaje[i])
            posicionesMod.append((posicionesClave[i]+posicionesMensaje[i])%len(abc))
            mensajeCifrado+=abc[posicionesMod[i]]
    print(clave ,posicionesClave)
    print(mensaje , posicionesMensaje)
    print ("Suma posiciones: ",posicionesFinales)
    print ("Posiciones Mod: ",posicionesMod)
    print("Mensaje cifrado: ", mensajeCifrado.upper())

else: #Verifica la opción seleccionada
    
    clave =input("Ingresa la clave:")
    clave=clave.lower()
    mensajeCifrado= input("Ingresa el mensaje cifrado:   ")
    mensaje=mensaje.lower()
    while len(mensajeCifrado)<len(clave):
        mensajeCifrado+="x"
    for letra in clave.lower():
        if letra in abc:
            posLetra=int(abc.index(letra))
            posicionesClave.append(posLetra)
    for letra in mensajeCifrado.lower():
        if letra in abc:
            posLetra=int(abc.index(letra))
            posicionesMensajeCifrado.append(posLetra)
    for i in range(len(posicionesMensajeCifrado)):
            posicionesFinales.append(posicionesMensajeCifrado[i]-posicionesClave[i])
            posicionesMod.append((posicionesMensajeCifrado[i]-posicionesClave[i])%len(abc))
            mensajeClaro+=abc[posicionesMod[i]]
    print(clave ,posicionesClave)
    print(mensajeCifrado , posicionesMensajeCifrado)
    print ("Suma posiciones: ",posicionesFinales)
    print ("Posiciones Mod: ",posicionesMod)
    print("Mensaje claro: ", mensajeClaro.upper())   
   