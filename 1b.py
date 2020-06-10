#Isabel Gómez Yareli Elizabeth 
#Zavala Estala Lisset
#Grupo 1 Criptografía
accion=input("Ingresa (c) cifrar o (d) descifrar: ")
if accion==("c" or "C"): #Verifica la opción seleccionada
    claro="abcdefghijklmnñopqrstuvwxyz" #Definimos el claro
    clave =input("Ingresa la clave:") #Pedimos la clave para crifar 
    clave=clave.lower()
    cifrado = ""   #Para guardar el cifrado
    textoCifrado = "" #Texto cifrado
    for letra in clave    :     #Recorremos la clave
        if letra not in cifrado: #Verificamos que la letra no este repetida
            cifrado+=letra.lower()  #Se añade la letra en caso de no estar en cifrado
    for letra in claro:     #Recorremos claro
        if letra not in cifrado: #Verificamos que letra no estan en cifrado 
            cifrado+=letra
        
    print("Claro:  ", claro)  #Impresión de mensaje claro

    print("Cifrado:", cifrado)  #Impresión de mensaje cifrado
    
    textoLlano=input("Ingresa el texto llano: ") #Pedimos texto llano 
    for letra in textoLlano.lower(): #Recorremos el texto llano
        if letra in claro: #Verificamos que la letra este en claro
            pos_claro=claro.index(letra) #Indicamos posicion de claro
            pos_cifrado=pos_claro #igualamos la posicion anterior con la de cifrado 
            textoCifrado+=cifrado[pos_cifrado] #Añadimos las letras a texto cifrado 
    print("Texto llano: ", textoLlano.lower()) #Imprimimos texto llano
    print("Texto cifrado: ", textoCifrado.upper()) #Imprimimos texto cifrado en mayúculas
else:
    clave =input("Ingresa la clave:") #Pedimos la clave para descrifar 
    clave=clave.lower()
    claro="abcdefghijklmnñopqrstuvwxyz" #Definimos el claro
    cifrado = ""   #Para guardar el cifrado
    textoLlano = "" #Texto cifrado
    for letra in clave    :     #Recorremos la clave
        if letra not in cifrado: #Verificamos que la letra no este repetida
            cifrado+=letra  #Se añade la letra en caso de no estar en cifrado
    for letra in claro:     #Recorremos claro
        if letra not in cifrado: #Verificamos que letra no estan en cifrado 
            cifrado+=letra
        
    print("Cifrado:", cifrado)  #Impresión de mensaje cifrado

    print("Claro:  ", claro)  #Impresión de mensaje claro
    
    textoCifrado=input("Ingresa el texto cifrado: ") #Pedimos texto cifrado
    for letra in textoCifrado.lower(): #Recorremos el texto cifrado
        if letra in cifrado: #Verificamos que la letra este en cifrado
            pos_cifrado=cifrado.index(letra) #Indicamos posicion de cifrado
            pos_claro=pos_cifrado #igualamos la posicion anterior con la de claro 
            textoLlano+=claro[pos_claro] #Añadimos las letras a texto llano
    print("Texto cifrado: ", textoCifrado.upper()) #Imprimimos texto cifrado en mayúculas
    print("Texto llano: ", textoLlano) #Imprimimos texto llano
    
