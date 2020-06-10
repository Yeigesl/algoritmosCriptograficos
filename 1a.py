#Isabel Gómez Yareli Elizabeth 
#Zavala Estala Lisset
#Grupo 1 Criptografía
accion=input("Ingresa (c) cifrar o (d) descifrar: ")
if accion=="c": #Verifica la opción seleccionada
    mensajeClaro=input ("Ingresa el mensaje claro:  ") #ingresar texto claro
    
    if mensajeClaro==mensajeClaro.upper () : #Verifica mayúsulcas
     
          abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #Definimos para mayúsculas
     
    else:
     
          abc="abcdefghijklmnñopqrstuvwxyz" #Definimos para minúsculas
     
    k=int (3) #Valor para cifrar 
     
    mensajeCifrado = ""
    for letra in mensajeClaro:                 #Recorremos el mensajeClaro
      if letra in abc:                         #Verificamos si esta en el abecedario
        pos_letra = abc.index(letra)           #Obtenemos la posición de la letra en mensajeClaro
        nueva_pos = (pos_letra + k) % len(abc) #Obtenemos la posición de la letra en mensajeCifrado
        mensajeCifrado+= abc[nueva_pos]        #Se genera el mensajeCifrado
      else:
        mensajeCifrado+= letra                 #Se añade la letra en caso de no estar en abc 

    print("Mensaje cifrado:", mensajeCifrado)  #Impresión de mensajeCifrado

else:
    
    mensajeCifrado=input ("Ingresa el mensaje cifrado:  ") #ingresar texto cifrado
    
    if mensajeCifrado==mensajeCifrado.upper () : #Verifica mayúsulcas
     
          abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #Definimos para mayúsculas
     
    else:
     
          abc="abcdefghijklmnñopqrstuvwxyz" #Definimos para minúsculas
     
    k=int (3) #Valor para cifrar 
     
    mensajeClaro = ""
    for letra in mensajeCifrado:                 #Recorremos el mensajeCifrado
      if letra in abc:                         #Verificamos si esta en el abecedario
        pos_letra = abc.index(letra)           #Obtenemos la posición de la letra en mensajeCifrado
        nueva_pos = (pos_letra - k) % len(abc) #Obtenemos la posición de la letra en mensajeClaro
        mensajeClaro+= abc[nueva_pos]        #Se genera el mensajeClaro
      else:
        mensajeClaro+= letra                 #Se añade la letra en caso de no estar en abc 

    print("Mensaje claro:", mensajeClaro)  #Impresión de mensajeClaro
    

        
