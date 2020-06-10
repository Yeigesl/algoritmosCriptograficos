#Isabel Gómez Yareli Elizabeth 
#Zavala Estala Lisset
#Grupo 1 Criptografía
posiciones=[]
posicionesDes=[]
mensajeCifrado=""
mensajeDescifrado=""
abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
mensajeClaro=input("Ingresa el mensaje a cifrar y descifrar :")
mensajeClaro=mensajeClaro.upper()
for letra in mensajeClaro:
    if letra in abc:
        posLetra=abc.index(letra)
        posCifrado = ((posLetra*19+7) % len(abc) )
        posiciones.append(posCifrado)
        mensajeCifrado+= abc[posCifrado] 

for letra in mensajeCifrado:
    if letra in abc:
        posLetra=abc.index(letra)
        posDescifrado = (((posLetra-7)*10) % len(abc) )
        posicionesDes.append(posDescifrado)
        mensajeDescifrado+= abc[posDescifrado] 
        
print("Posiciones cifrado", posiciones)
print("Mensaje Cifrado:", mensajeCifrado)
print("Posiciones descifrado", posicionesDes)
print("Mensaje Descifrado:", mensajeDescifrado)


