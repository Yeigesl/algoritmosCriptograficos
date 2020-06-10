mensaje1=""
mensaje2=""
mensaje3=""
mensaje4=""
mensaje5=""
mensaje6=""
mensaje7=""
mensaje8=""
abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
mensajeCifrado1=""
mensajeClaro=input("Ingresa el mensaje a cifrar y descifrar:")
mensajeClaro=mensajeClaro.upper()
mensajeClaro=mensajeClaro.replace(' ','')
while len(mensajeClaro)<32:
    mensajeClaro+="X"
mensaje1= mensajeClaro[0:4]
mensaje2= mensajeClaro[4:8]
mensaje3= mensajeClaro[8:12]
mensaje4= mensajeClaro[12:16]
mensaje5= mensajeClaro[16:20]
mensaje6= mensajeClaro[20:24]
mensaje7= mensajeClaro[24:28]
mensaje8= mensajeClaro[28:32]
def sustitucion(mensaje):
    sus=""
    for letra in mensaje:
        if letra in abc:
            posLetra=abc.index(letra)
            m1 = ((posLetra+1) % len(abc) )
            sus+= abc[m1]
    return sus
def permutacion(sustito):
    permutada=sustito[3]+sustito[1]+sustito[0]+sustito[2]
    return permutada
    
def sustitucionInv(mensaje):
    sus=""
    for letra in mensaje:
        if letra in abc:
            posLetra=abc.index(letra)
            m1 = ((posLetra-1) % len(abc) )
            sus+= abc[m1]
    return sus

def permutacionInv(sustito):
    permutada=sustito[2]+sustito[1]+sustito[3]+sustito[0]
    return permutada
    
def main():
    print("       mensajeCifrado1")
    print("                     RONDA         1")
    s1m1=sustitucion(mensaje1)
    p1m1=permutacion(s1m1)
    s1m3=sustitucion(mensaje3)
    p1m3=permutacion(s1m3)
    s1m5=sustitucion(mensaje5)
    p1m5=permutacion(s1m5)
    s1m7=sustitucion(mensaje7)
    p1m7=permutacion(s1m7)
    print(mensaje1,mensaje2,"  ",mensaje3,mensaje4,"  ",mensaje5,mensaje6,"  ",mensaje7,mensaje8 )     
    print(s1m1,mensaje2,"  ",s1m3,mensaje4,"  ",s1m5,mensaje6,"  ",s1m7,mensaje8)
    print(p1m1,mensaje2,"  ",p1m3,mensaje4,"  ",p1m5,mensaje6,"  ",p1m7,mensaje8)
    
    print("                     RONDA         2")
    s1m2=sustitucion(mensaje2)
    p1m2=permutacion(s1m2)
    s1m4=sustitucion(mensaje4)
    p1m4=permutacion(s1m4)
    s1m6=sustitucion(mensaje6)
    p1m6=permutacion(s1m6)
    s1m8=sustitucion(mensaje8)
    p1m8=permutacion(s1m8)
    print(mensaje2,p1m1,"  ",mensaje4,p1m3,"  ",mensaje6,p1m5,"  ",mensaje8,p1m7 )     
    print(s1m2,p1m1,"  ",s1m4,p1m3,"  ",s1m6,p1m5,"  ",s1m8,p1m7)
    print(p1m2,p1m1,"  ",p1m4,p1m3,"  ",p1m6,p1m5,"  ",p1m8,p1m7)
    
    print("                     RONDA         3")
    s2m1=sustitucion(p1m1)
    p2m1=permutacion(s2m1)
    s2m3=sustitucion(p1m3)
    p2m3=permutacion(s2m3)
    s2m5=sustitucion(p1m5)
    p2m5=permutacion(s2m5)
    s2m7=sustitucion(p1m7)
    p2m7=permutacion(s2m7)
    print(p1m1,p1m2,"  ",p1m3,p1m4,"  ",p1m5,p1m6,"  ",p1m7,p1m8 )     
    print(s2m1,p1m2,"  ",s2m3,p1m4,"  ",s2m5,p1m6,"  ",s2m7,p1m8)
    print(p2m1,p1m2,"  ",p2m3,p1m4,"  ",p2m5,p1m6,"  ",p2m7,p1m8)

    print("                     RONDA         4")
    s2m2=sustitucion(p1m2)
    p2m2=permutacion(s2m2)
    s2m4=sustitucion(p1m4)
    p2m4=permutacion(s2m4)
    s2m6=sustitucion(p1m6)
    p2m6=permutacion(s2m6)
    s2m8=sustitucion(p1m8)
    p2m8=permutacion(s2m8)
    print(p1m2,p2m1,"  ",p1m4,p2m3,"  ",p1m6,p2m5,"  ",p1m8,p2m7)     
    print(s2m2,p2m1,"  ",s2m4,p2m3,"  ",s2m6,p2m5,"  ",s2m8,p2m7)
    print(p2m2,p2m1,"  ",p2m4,p2m3,"  ",p2m6,p2m5,"  ",p2m8,p2m7)
    print(p2m1,p2m2,"  ",p2m3,p2m4,"  ",p2m5,p2m6,"  ",p2m7,p2m8)


    
    print("                     Descifrado            ")
    print("                     RONDA         1")
    p1Inm2=permutacionInv(p2m1)
    s1Inm2=sustitucionInv(p1Inm2)
    p1Inm4=permutacionInv(p2m3)
    s1Inm4=sustitucionInv(p1Inm4)
    p1Inm6=permutacionInv(p2m5)
    s1Inm6=sustitucionInv(p1Inm6)
    p1Inm8=permutacionInv(p2m7)
    s1Inm8=sustitucionInv(p1Inm8)
    print(p2m1,p2m2,"  ",p2m3,p2m4,"  ",p2m5,p2m6,"  ",p2m7,p2m8)
    print(p1Inm2,p2m2,"  ",p1Inm4,p2m4,"  ",p1Inm6,p2m6,"  ",p1Inm8,p2m8)
    print(s1Inm2,p2m2,"  ",s1Inm4,p2m4,"  ",s1Inm6,p2m6,"  ",s1Inm8,p2m8)
    
    print("                     RONDA         2")
    p1Inm1=permutacionInv(p2m2)
    s1Inm1=sustitucionInv(p1Inm1)
    p1Inm3=permutacionInv(p2m4)
    s1Inm3=sustitucionInv(p1Inm3)
    p1Inm5=permutacionInv(p2m6)
    s1Inm5=sustitucionInv(p1Inm5)
    p1Inm7=permutacionInv(p2m8)
    s1Inm7=sustitucionInv(p1Inm7)
    print(p2m2,s1Inm2,"  ",p2m4,s1Inm4,"  ",p2m6,s1Inm6,"  ",p2m8,s1Inm8)
    print(p1Inm1,s1Inm2,"  ",p1Inm3,s1Inm4,"  ", p1Inm5,s1Inm6,"  ",p1Inm7,s1Inm8)  
    print(s1Inm1,s1Inm2,"  ",s1Inm3,s1Inm4,"  ",s1Inm5,s1Inm6,"  ",s1Inm7,s1Inm8)
    
    print("                     RONDA         3")
    p2Inm2=permutacionInv(s1Inm2)
    s2Inm2=sustitucionInv(p2Inm2)
    p2Inm4=permutacionInv(s1Inm4)
    s2Inm4=sustitucionInv(p2Inm4)
    p2Inm6=permutacionInv(s1Inm6)
    s2Inm6=sustitucionInv(p2Inm6)
    p2Inm8=permutacionInv(s1Inm8)
    s2Inm8=sustitucionInv(p2Inm8)
    print(s1Inm2,s1Inm1,"  ",s1Inm4,s1Inm3,"  ",s1Inm6,s1Inm5,"  ",s1Inm8,s1Inm7)
    print(p2Inm2,s1Inm1,"  ",p2Inm4,s1Inm3,"  ", p2Inm6,s1Inm5,"  ",p2Inm8,s1Inm7)  
    print(s2Inm2,s1Inm1,"  ",s2Inm4,s1Inm3,"  ",s2Inm6,s1Inm5,"  ",s2Inm8,s1Inm7)

    print("                     RONDA         4")
    p2Inm1=permutacionInv(s1Inm1)
    s2Inm1=sustitucionInv(p2Inm1)
    p2Inm3=permutacionInv(s1Inm3)
    s2Inm3=sustitucionInv(p2Inm3)
    p2Inm5=permutacionInv(s1Inm5)
    s2Inm5=sustitucionInv(p2Inm5)
    p2Inm7=permutacionInv(s1Inm7)
    s2Inm7=sustitucionInv(p2Inm7)
    print(s1Inm1,s2Inm2,"  ",s1Inm3,s2Inm4,"  ",s1Inm5,s2Inm6,"  ",s1Inm7,s2Inm8)
    print(p2Inm1,s2Inm2,"  ",p2Inm3,s2Inm4,"  ",p2Inm5,s2Inm6,"  ",p2Inm7,s2Inm8)  
    print(s2Inm1,s2Inm2,"  ",s2Inm3,s2Inm4,"  ",s2Inm5,s2Inm6,"  ",s2Inm7,s2Inm8)
    print(s2Inm2,s2Inm1,"  ",s2Inm4,s2Inm3,"  ",s2Inm6,s2Inm5,"  ",s2Inm8,s2Inm7,)

main()