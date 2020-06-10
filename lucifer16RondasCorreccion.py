mensaje1=""
mensaje2=""
mensaje3=""
mensaje4=""
mensaje5=""
mensaje6=""
mensaje7=""
mensaje8=""
abc="".join(chr(x) for x in range(255))
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
    permutada=sustito[1]+sustito[2]+sustito[0]+sustito[3]
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
    permutada=sustito[2]+sustito[0]+sustito[1]+sustito[3]
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
    print(mensaje2,p1m1,"  ",mensaje4,p1m3,"  ",mensaje6,p1m5,"  ",mensaje8,p1m7)
    
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
    print(p1m1,p1m2,"  ",p1m3,p1m4,"  ",p1m5,p1m6,"  ",p1m7,p1m8)
    
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
    print(p1m2,p2m1,"  ",p1m4,p2m3,"  ",p1m6,p2m5,"  ",p1m8,p2m7)

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
    
    print("                     RONDA         5")
    s3m1=sustitucion(p2m1)
    p3m1=permutacion(s3m1)
    s3m3=sustitucion(p2m3)
    p3m3=permutacion(s3m3)
    s3m5=sustitucion(p2m5)
    p3m5=permutacion(s3m5)
    s3m7=sustitucion(p2m7)
    p3m7=permutacion(s3m7)
    print(p2m1,p2m2,"  ",p2m3,p2m4,"  ",p2m5,p2m6,"  ",p2m7,p2m8 )     
    print(s3m1,p2m2,"  ",s3m3,p2m4,"  ",s3m5,p2m6,"  ",s3m7,p2m8)
    print(p3m1,p2m2,"  ",p3m3,p2m4,"  ",p3m5,p2m6,"  ",p3m7,p2m8)
    print(p2m2,p3m1,"  ",p2m4,p3m3,"  ",p2m6,p3m5,"  ",p2m8,p3m7)
    
   
    print("                     RONDA         6")
    s3m2=sustitucion(p2m2)
    p3m2=permutacion(s3m2)
    s3m4=sustitucion(p2m4)
    p3m4=permutacion(s3m4)
    s3m6=sustitucion(p2m6)
    p3m6=permutacion(s3m6)
    s3m8=sustitucion(p2m8)
    p3m8=permutacion(s3m8)
    print(p2m2,p3m1,"  ",p2m4,p3m3,"  ",p2m6,p3m5,"  ",p2m8,p3m7)     
    print(s3m2,p3m1,"  ",s3m4,p3m3,"  ",s3m6,p3m5,"  ",s3m8,p3m7)
    print(p3m2,p3m1,"  ",p3m4,p3m3,"  ",p3m6,p3m5,"  ",p3m8,p3m7)
    print(p3m1,p3m2,"  ",p3m3,p3m4,"  ",p3m5,p3m6,"  ",p3m7,p3m8)

    print("                     RONDA         7")
    s4m1=sustitucion(p3m1)
    p4m1=permutacion(s4m1)
    s4m3=sustitucion(p3m3)
    p4m3=permutacion(s4m3)
    s4m5=sustitucion(p3m5)
    p4m5=permutacion(s4m5)
    s4m7=sustitucion(p3m7)
    p4m7=permutacion(s4m7)
    print(p3m1,p3m2,"  ",p3m3,p3m4,"  ",p3m5,p3m6,"  ",p3m7,p3m8)     
    print(s4m1,p3m2,"  ",s4m3,p3m4,"  ",s4m5,p3m6,"  ",s4m7,p3m8)
    print(p4m1,p3m2,"  ",p4m3,p3m4,"  ",p4m5,p3m6,"  ",p4m7,p3m8)
    print(p3m2,p4m1,"  ",p3m4,p4m3,"  ",p3m6,p4m5,"  ",p3m8,p4m7)
    
    
    print("                     RONDA         8")
    s4m2=sustitucion(p3m2)
    p4m2=permutacion(s4m2)
    s4m4=sustitucion(p3m4)
    p4m4=permutacion(s4m4)
    s4m6=sustitucion(p3m6)
    p4m6=permutacion(s4m6)
    s4m8=sustitucion(p3m8)
    p4m8=permutacion(s4m8)
    print(p3m2,p4m1,"  ",p3m4,p4m3,"  ",p3m6,p4m5,"  ",p3m8,p4m7)     
    print(s4m2,p4m1,"  ",s4m4,p4m3,"  ",s4m6,p4m5,"  ",s4m8,p4m7)
    print(p4m2,p4m1,"  ",p4m4,p4m3,"  ",p4m6,p4m5,"  ",p4m8,p4m7)
    print(p4m1,p4m2,"  ",p4m3,p4m4,"  ",p4m5,p4m6,"  ",p4m7,p4m8)


    
    print("                     RONDA         9")
    s5m1=sustitucion(p4m1)
    p5m1=permutacion(s5m1)
    s5m3=sustitucion(p4m3)
    p5m3=permutacion(s5m3)
    s5m5=sustitucion(p4m5)
    p5m5=permutacion(s5m5)
    s5m7=sustitucion(p4m7)
    p5m7=permutacion(s5m7)
    print(p4m1,p4m2,"  ",p4m3,p4m4,"  ",p4m5,p4m6,"  ",p4m7,p4m8)     
    print(s5m1,p4m2,"  ",s5m3,p4m4,"  ",s5m5,p4m6,"  ",s5m7,p4m8)
    print(p5m1,p4m2,"  ",p5m3,p4m4,"  ",p5m5,p4m6,"  ",p5m7,p4m8)
    print(p4m2,p5m1,"  ",p4m4,p5m3,"  ",p4m6,p5m5,"  ",p4m8,p5m7)
   
   
    print("                     RONDA         10")
    s5m2=sustitucion(p4m2)
    p5m2=permutacion(s5m2)
    s5m4=sustitucion(p4m4)
    p5m4=permutacion(s5m4)
    s5m6=sustitucion(p4m6)
    p5m6=permutacion(s5m6)
    s5m8=sustitucion(p4m8)
    p5m8=permutacion(s5m8)
    print(p4m2,p5m1,"  ",p4m4,p5m3,"  ",p4m6,p5m5,"  ",p4m8,p5m7)     
    print(s5m2,p5m1,"  ",s5m4,p5m3,"  ",s5m6,p5m5,"  ",s5m8,p5m7)
    print(p5m2,p5m1,"  ",p5m4,p5m3,"  ",p5m6,p5m5,"  ",p5m8,p5m7)
    print(p5m1,p5m2,"  ",p5m3,p5m4,"  ",p5m5,p5m6,"  ",p5m7,p5m8)

        
    print("                     RONDA         11")
    s6m1=sustitucion(p5m1)
    p6m1=permutacion(s6m1)
    s6m3=sustitucion(p5m3)
    p6m3=permutacion(s6m3)
    s6m5=sustitucion(p5m5)
    p6m5=permutacion(s6m5)
    s6m7=sustitucion(p5m7)
    p6m7=permutacion(s6m7)
    print(p5m1,p5m2,"  ",p5m3,p5m4,"  ",p5m5,p5m6,"  ",p5m7,p5m8)     
    print(s6m1,p5m2,"  ",s6m3,p5m4,"  ",s6m5,p5m6,"  ",s6m7,p5m8)
    print(p6m1,p5m2,"  ",p6m3,p5m4,"  ",p6m5,p5m6,"  ",p6m7,p5m8)
    print(p5m2,p6m1,"  ",p5m4,p6m3,"  ",p5m6,p6m5,"  ",p5m8,p6m7)
   
   
   
    print("                     RONDA         12")
    s6m2=sustitucion(p5m2)
    p6m2=permutacion(s6m2)
    s6m4=sustitucion(p5m4)
    p6m4=permutacion(s6m4)
    s6m6=sustitucion(p5m6)
    p6m6=permutacion(s6m6)
    s6m8=sustitucion(p5m8)
    p6m8=permutacion(s6m8)
    print(p5m2,p6m1,"  ",p5m4,p6m3,"  ",p5m6,p6m5,"  ",p5m8,p6m7)     
    print(s6m2,p6m1,"  ",s6m4,p6m3,"  ",s6m6,p6m5,"  ",s6m8,p6m7)
    print(p6m2,p6m1,"  ",p6m4,p6m3,"  ",p6m6,p6m5,"  ",p6m8,p6m7)
    print(p6m1,p6m2,"  ",p6m3,p6m4,"  ",p6m5,p6m6,"  ",p6m7,p6m8)

         
    print("                     RONDA         13")
    s7m1=sustitucion(p6m1)
    p7m1=permutacion(s7m1)
    s7m3=sustitucion(p6m3)
    p7m3=permutacion(s7m3)
    s7m5=sustitucion(p6m5)
    p7m5=permutacion(s7m5)
    s7m7=sustitucion(p6m7)
    p7m7=permutacion(s7m7)
    print(p6m1,p6m2,"  ",p6m3,p6m4,"  ",p6m5,p6m6,"  ",p6m7,p6m8)     
    print(s7m1,p6m2,"  ",s7m3,p6m4,"  ",s7m5,p6m6,"  ",s7m7,p6m8)
    print(p7m1,p6m2,"  ",p7m3,p6m4,"  ",p7m5,p6m6,"  ",p7m7,p6m8)
    print(p6m2,p7m1,"  ",p6m4,p7m3,"  ",p6m6,p7m5,"  ",p6m8,p7m7)
    
   
    print("                     RONDA         14")
    s7m2=sustitucion(p6m2)
    p7m2=permutacion(s7m2)
    s7m4=sustitucion(p6m4)
    p7m4=permutacion(s7m4)
    s7m6=sustitucion(p6m6)
    p7m6=permutacion(s7m6)
    s7m8=sustitucion(p6m8)
    p7m8=permutacion(s7m8)
    print(p6m2,p7m1,"  ",p6m4,p7m3,"  ",p6m6,p7m5,"  ",p6m8,p7m7)     
    print(s7m2,p7m1,"  ",s7m4,p7m3,"  ",s7m6,p7m5,"  ",s7m8,p7m7)
    print(p7m2,p7m1,"  ",p7m4,p7m3,"  ",p7m6,p7m5,"  ",p7m8,p7m7)
    print(p7m1,p7m2,"  ",p7m3,p7m4,"  ",p7m5,p7m6,"  ",p7m7,p7m8)
    
    print("                     RONDA         15")
    s8m1=sustitucion(p7m1)
    p8m1=permutacion(s8m1)
    s8m3=sustitucion(p7m3)
    p8m3=permutacion(s8m3)
    s8m5=sustitucion(p7m5)
    p8m5=permutacion(s8m5)
    s8m7=sustitucion(p7m7)
    p8m7=permutacion(s8m7)
    print(p7m1,p7m2,"  ",p7m3,p7m4,"  ",p7m5,p7m6,"  ",p7m7,p7m8)     
    print(s8m1,p7m2,"  ",s8m3,p7m4,"  ",s8m5,p7m6,"  ",s8m7,p7m8)
    print(p8m1,p7m2,"  ",p8m3,p7m4,"  ",p8m5,p7m6,"  ",p8m7,p7m8)
    print(p7m2,p8m1,"  ",p7m4,p8m3,"  ",p7m6,p8m5,"  ",p7m8,p8m7)
   
    print("                     RONDA         16")
    s8m2=sustitucion(p7m2)
    p8m2=permutacion(s8m2)
    s8m4=sustitucion(p7m4)
    p8m4=permutacion(s8m4)
    s8m6=sustitucion(p7m6)
    p8m6=permutacion(s8m6)
    s8m8=sustitucion(p7m8)
    p8m8=permutacion(s8m8)
    print(p7m2,p8m1,"  ",p7m4,p8m3,"  ",p7m6,p8m5,"  ",p7m8,p8m7)     
    print(s8m2,p8m1,"  ",s8m4,p8m3,"  ",s8m6,p8m5,"  ",s8m8,p8m7)
    print(p8m2,p8m1,"  ",p8m4,p8m3,"  ",p8m6,p8m5,"  ",p8m8,p8m7)
    print(p8m1,p8m2,"  ",p8m3,p8m4,"  ",p8m5,p8m6,"  ",p8m7,p8m8)
    
    print("                     Descifrado            ")
    print("                     RONDA         1")
    p1Inm2=permutacionInv(p8m1)
    s1Inm2=sustitucionInv(p1Inm2)
    p1Inm4=permutacionInv(p8m3)
    s1Inm4=sustitucionInv(p1Inm4)
    p1Inm6=permutacionInv(p8m5)
    s1Inm6=sustitucionInv(p1Inm6)
    p1Inm8=permutacionInv(p8m7)
    s1Inm8=sustitucionInv(p1Inm8)
    print(p8m1,p8m2,"  ",p8m3,p8m4,"  ",p8m5,p8m6,"  ",p8m7,p8m8)
    print(p1Inm2,p8m2,"  ",p1Inm4,p8m4,"  ",p1Inm6,p8m6,"  ",p1Inm8,p8m8)
    print(s1Inm2,p8m2,"  ",s1Inm4,p8m4,"  ",s1Inm6,p8m6,"  ",s1Inm8,p8m8)
    print(p8m2,s1Inm2,"  ",p8m4,s1Inm4,"  ",p8m6,s1Inm6,"  ",p8m8,s1Inm8)
    
    print("                     RONDA         2")
    p1Inm1=permutacionInv(p8m2)
    s1Inm1=sustitucionInv(p1Inm1)
    p1Inm3=permutacionInv(p8m4)
    s1Inm3=sustitucionInv(p1Inm3)
    p1Inm5=permutacionInv(p8m6)
    s1Inm5=sustitucionInv(p1Inm5)
    p1Inm7=permutacionInv(p8m8)
    s1Inm7=sustitucionInv(p1Inm7)
    print(p8m2,s1Inm2,"  ",p8m4,s1Inm4,"  ",p8m6,s1Inm6,"  ",p8m8,s1Inm8)
    print(p1Inm1,s1Inm2,"  ",p1Inm3,s1Inm4,"  ", p1Inm5,s1Inm6,"  ",p1Inm7,s1Inm8)  
    print(s1Inm1,s1Inm2,"  ",s1Inm3,s1Inm4,"  ",s1Inm5,s1Inm6,"  ",s1Inm7,s1Inm8)
    print(s1Inm2,s1Inm1,"  ",s1Inm4,s1Inm3,"  ",s1Inm6,s1Inm5,"  ",s1Inm8,s1Inm7)
    
    
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
    print(s1Inm1,s2Inm2,"  ",s1Inm3,s2Inm4,"  ",s1Inm5,s2Inm6,"  ",s1Inm7,s2Inm8)

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
    print(s2Inm2,s2Inm1,"  ",s2Inm4,s2Inm3,"  ",s2Inm6,s2Inm5,"  ",s2Inm8,s2Inm7)
    
    
    print("                     RONDA         5")
    p3Inm2=permutacionInv(s2Inm2)
    s3Inm2=sustitucionInv(p3Inm2)
    p3Inm4=permutacionInv(s2Inm4)
    s3Inm4=sustitucionInv(p3Inm4)
    p3Inm6=permutacionInv(s2Inm6)
    s3Inm6=sustitucionInv(p3Inm6)
    p3Inm8=permutacionInv(s2Inm8)
    s3Inm8=sustitucionInv(p3Inm8)
    print(s2Inm2,s2Inm1,"  ",s2Inm4,s2Inm3,"  ",s2Inm6,s2Inm5,"  ",s2Inm8,s2Inm7)
    print(p3Inm2,s2Inm1,"  ",p3Inm4,s2Inm3,"  ", p3Inm6,s2Inm5,"  ",p3Inm8,s2Inm7)  
    print(s3Inm2,s2Inm1,"  ",s3Inm4,s2Inm3,"  ",s3Inm6,s2Inm5,"  ",s3Inm8,s2Inm7)
    print(s2Inm1,s3Inm2,"  ",s2Inm3,s3Inm4,"  ",s2Inm5,s3Inm6,"  ",s2Inm7,s3Inm8)



    print("                     RONDA         6")
    p3Inm1=permutacionInv(s2Inm1)
    s3Inm1=sustitucionInv(p3Inm1)
    p3Inm3=permutacionInv(s2Inm3)
    s3Inm3=sustitucionInv(p3Inm3)
    p3Inm5=permutacionInv(s2Inm5)
    s3Inm5=sustitucionInv(p3Inm5)
    p3Inm7=permutacionInv(s2Inm7)
    s3Inm7=sustitucionInv(p3Inm7)
    print(s2Inm1,s3Inm2,"  ",s2Inm3,s3Inm4,"  ",s2Inm5,s3Inm6,"  ",s2Inm7,s3Inm8)
    print(p3Inm1,s3Inm2,"  ",p3Inm3,s3Inm4,"  ",p3Inm5,s3Inm6,"  ",p3Inm7,s3Inm8)  
    print(s3Inm1,s3Inm2,"  ",s3Inm3,s3Inm4,"  ",s3Inm5,s3Inm6,"  ",s3Inm7,s3Inm8)
    print(s3Inm2,s3Inm1,"  ",s3Inm4,s3Inm3,"  ",s3Inm6,s3Inm5,"  ",s3Inm8,s3Inm7)
    
    
    print("                     RONDA         7")
    p4Inm2=permutacionInv(s3Inm2)
    s4Inm2=sustitucionInv(p4Inm2)
    p4Inm4=permutacionInv(s3Inm4)
    s4Inm4=sustitucionInv(p4Inm4)
    p4Inm6=permutacionInv(s3Inm6)
    s4Inm6=sustitucionInv(p4Inm6)
    p4Inm8=permutacionInv(s3Inm8)
    s4Inm8=sustitucionInv(p4Inm8)
    print(s3Inm2,s3Inm1,"  ",s3Inm4,s3Inm3,"  ",s3Inm6,s3Inm5,"  ",s3Inm8,s3Inm7)
    print(p4Inm2,s3Inm1,"  ",p4Inm4,s3Inm3,"  ",p4Inm6,s3Inm5,"  ",p4Inm8,s3Inm7)  
    print(s4Inm2,s3Inm1,"  ",s4Inm4,s3Inm3,"  ",s4Inm6,s3Inm5,"  ",s4Inm8,s3Inm7)
    print(s3Inm1,s4Inm2,"  ",s3Inm3,s4Inm4,"  ",s3Inm5,s4Inm6,"  ",s3Inm7,s4Inm8)

    print("                     RONDA         8")
    p4Inm1=permutacionInv(s3Inm1)
    s4Inm1=sustitucionInv(p4Inm1)
    p4Inm3=permutacionInv(s3Inm3)
    s4Inm3=sustitucionInv(p4Inm3)
    p4Inm5=permutacionInv(s3Inm5)
    s4Inm5=sustitucionInv(p4Inm5)
    p4Inm7=permutacionInv(s3Inm7)
    s4Inm7=sustitucionInv(p4Inm7)
    print(s3Inm1,s4Inm2,"  ",s3Inm3,s4Inm4,"  ",s3Inm5,s4Inm6,"  ",s3Inm7,s4Inm8)
    print(p4Inm1,s4Inm2,"  ",p4Inm3,s4Inm4,"  ",p4Inm5,s4Inm6,"  ",p4Inm7,s4Inm8)  
    print(s4Inm1,s4Inm2,"  ",s4Inm3,s4Inm4,"  ",s4Inm5,s4Inm6,"  ",s4Inm7,s4Inm8)
    print(s4Inm2,s4Inm1,"  ",s4Inm4,s4Inm3,"  ",s4Inm6,s4Inm5,"  ",s4Inm8,s4Inm7)
    
    print("                     RONDA         9")
    p5Inm2=permutacionInv(s4Inm2)
    s5Inm2=sustitucionInv(p5Inm2)
    p5Inm4=permutacionInv(s4Inm4)
    s5Inm4=sustitucionInv(p5Inm4)
    p5Inm6=permutacionInv(s4Inm6)
    s5Inm6=sustitucionInv(p5Inm6)
    p5Inm8=permutacionInv(s4Inm8)
    s5Inm8=sustitucionInv(p5Inm8)
    print(s4Inm2,s4Inm1,"  ",s4Inm4,s4Inm3,"  ",s4Inm6,s4Inm5,"  ",s4Inm8,s4Inm7)
    print(p5Inm2,s4Inm1,"  ",p5Inm4,s4Inm3,"  ",p5Inm6,s4Inm5,"  ",p5Inm8,s4Inm7)  
    print(s5Inm2,s4Inm1,"  ",s5Inm4,s4Inm3,"  ",s5Inm6,s4Inm5,"  ",s5Inm8,s4Inm7)
    print(s4Inm1,s5Inm2,"  ",s4Inm3,s5Inm4,"  ",s4Inm5,s5Inm6,"  ",s4Inm7,s5Inm8)
    
    
    
    print("                     RONDA         10")
    p5Inm1=permutacionInv(s4Inm1)
    s5Inm1=sustitucionInv(p5Inm1)
    p5Inm3=permutacionInv(s4Inm3)
    s5Inm3=sustitucionInv(p5Inm3)
    p5Inm5=permutacionInv(s4Inm5)
    s5Inm5=sustitucionInv(p5Inm5)
    p5Inm7=permutacionInv(s4Inm7)
    s5Inm7=sustitucionInv(p5Inm7)
    print(s4Inm1,s5Inm2,"  ",s4Inm3,s5Inm4,"  ",s4Inm5,s5Inm6,"  ",s4Inm7,s5Inm8)
    print(p5Inm1,s5Inm2,"  ",p5Inm3,s5Inm4,"  ",p5Inm5,s5Inm6,"  ",p5Inm7,s5Inm8)  
    print(s5Inm1,s5Inm2,"  ",s5Inm3,s5Inm4,"  ",s5Inm5,s5Inm6,"  ",s5Inm7,s5Inm8)
    print(s5Inm2,s5Inm1,"  ",s5Inm4,s5Inm3,"  ",s5Inm6,s5Inm5,"  ",s5Inm8,s5Inm7)
    
    
    print("                     RONDA         11")
    p6Inm2=permutacionInv(s5Inm2)
    s6Inm2=sustitucionInv(p6Inm2)
    p6Inm4=permutacionInv(s5Inm4)
    s6Inm4=sustitucionInv(p6Inm4)
    p6Inm6=permutacionInv(s5Inm6)
    s6Inm6=sustitucionInv(p6Inm6)
    p6Inm8=permutacionInv(s5Inm8)
    s6Inm8=sustitucionInv(p6Inm8)
    print(s5Inm2,s5Inm1,"  ",s5Inm4,s5Inm3,"  ",s5Inm6,s5Inm5,"  ",s5Inm8,s5Inm7)
    print(p6Inm2,s5Inm1,"  ",p6Inm4,s5Inm3,"  ",p6Inm6,s5Inm5,"  ",p6Inm8,s5Inm7)  
    print(s6Inm2,s5Inm1,"  ",s6Inm4,s5Inm3,"  ",s6Inm6,s5Inm5,"  ",s6Inm8,s5Inm7)
    print(s5Inm1,s6Inm2,"  ",s5Inm3,s6Inm4,"  ",s5Inm5,s6Inm6,"  ",s5Inm7,s6Inm8)
    
    
    print("                     RONDA         12")
    p6Inm1=permutacionInv(s5Inm1)
    s6Inm1=sustitucionInv(p6Inm1)
    p6Inm3=permutacionInv(s5Inm3)
    s6Inm3=sustitucionInv(p6Inm3)
    p6Inm5=permutacionInv(s5Inm5)
    s6Inm5=sustitucionInv(p6Inm5)
    p6Inm7=permutacionInv(s5Inm7)
    s6Inm7=sustitucionInv(p6Inm7)
    print(s5Inm1,s6Inm2,"  ",s5Inm3,s6Inm4,"  ",s5Inm5,s6Inm6,"  ",s5Inm7,s6Inm8)
    print(p6Inm1,s6Inm2,"  ",p6Inm3,s6Inm4,"  ",p6Inm5,s6Inm6,"  ",p6Inm7,s6Inm8)  
    print(s6Inm1,s6Inm2,"  ",s6Inm3,s6Inm4,"  ",s6Inm5,s6Inm6,"  ",s6Inm7,s6Inm8)
    print(s6Inm2,s6Inm1,"  ",s6Inm4,s6Inm3,"  ",s6Inm6,s6Inm5,"  ",s6Inm8,s6Inm7)


    print("                     RONDA         13")
    p7Inm2=permutacionInv(s6Inm2)
    s7Inm2=sustitucionInv(p7Inm2)
    p7Inm4=permutacionInv(s6Inm4)
    s7Inm4=sustitucionInv(p7Inm4)
    p7Inm6=permutacionInv(s6Inm6)
    s7Inm6=sustitucionInv(p7Inm6)
    p7Inm8=permutacionInv(s6Inm8)
    s7Inm8=sustitucionInv(p7Inm8)
    print(s6Inm2,s6Inm1,"  ",s6Inm4,s6Inm3,"  ",s6Inm6,s6Inm5,"  ",s6Inm8,s6Inm7)
    print(p7Inm2,s6Inm1,"  ",p7Inm4,s6Inm3,"  ",p7Inm6,s6Inm5,"  ",p7Inm8,s6Inm7)  
    print(s7Inm2,s6Inm1,"  ",s7Inm4,s6Inm3,"  ",s7Inm6,s6Inm5,"  ",s7Inm8,s6Inm7)
    print(s6Inm1,s7Inm2,"  ",s6Inm3,s7Inm4,"  ",s6Inm5,s7Inm6,"  ",s6Inm7,s7Inm8)
    
    
    
    print("                     RONDA         14")
    p7Inm1=permutacionInv(s6Inm1)
    s7Inm1=sustitucionInv(p7Inm1)
    p7Inm3=permutacionInv(s6Inm3)
    s7Inm3=sustitucionInv(p7Inm3)
    p7Inm5=permutacionInv(s6Inm5)
    s7Inm5=sustitucionInv(p7Inm5)
    p7Inm7=permutacionInv(s6Inm7)
    s7Inm7=sustitucionInv(p7Inm7)
    print(s6Inm1,s7Inm2,"  ",s6Inm3,s7Inm4,"  ",s6Inm5,s7Inm6,"  ",s6Inm7,s7Inm8)
    print(p7Inm1,s7Inm2,"  ",p7Inm3,s7Inm4,"  ",p7Inm5,s7Inm6,"  ",p7Inm7,s7Inm8)  
    print(s7Inm1,s7Inm2,"  ",s7Inm3,s7Inm4,"  ",s7Inm5,s7Inm6,"  ",s7Inm7,s7Inm8)
    print(s7Inm2,s7Inm1,"  ",s7Inm4,s7Inm3,"  ",s7Inm6,s7Inm5,"  ",s7Inm8,s7Inm7)
    
    
    
    print("                     RONDA         15")
    p8Inm2=permutacionInv(s7Inm2)
    s8Inm2=sustitucionInv(p8Inm2)
    p8Inm4=permutacionInv(s7Inm4)
    s8Inm4=sustitucionInv(p8Inm4)
    p8Inm6=permutacionInv(s7Inm6)
    s8Inm6=sustitucionInv(p8Inm6)
    p8Inm8=permutacionInv(s7Inm8)
    s8Inm8=sustitucionInv(p8Inm8)
    print(s7Inm2,s7Inm1,"  ",s7Inm4,s7Inm3,"  ",s7Inm6,s7Inm5,"  ",s7Inm8,s7Inm7)
    print(p8Inm2,s7Inm1,"  ",p8Inm4,s7Inm3,"  ",p8Inm6,s7Inm5,"  ",p8Inm8,s7Inm7)  
    print(s8Inm2,s7Inm1,"  ",s8Inm4,s7Inm3,"  ",s8Inm6,s7Inm5,"  ",s8Inm8,s7Inm7)
    print(s7Inm1,s8Inm2,"  ",s7Inm3,s8Inm4,"  ",s7Inm5,s8Inm6,"  ",s7Inm7,s8Inm8)
    
    
    
    print("                     RONDA         16")
    p8Inm1=permutacionInv(s7Inm1)
    s8Inm1=sustitucionInv(p8Inm1)
    p8Inm3=permutacionInv(s7Inm3)
    s8Inm3=sustitucionInv(p8Inm3)
    p8Inm5=permutacionInv(s7Inm5)
    s8Inm5=sustitucionInv(p8Inm5)
    p8Inm7=permutacionInv(s7Inm7)
    s8Inm7=sustitucionInv(p8Inm7)
    print(s7Inm1,s8Inm2,"  ",s7Inm3,s8Inm4,"  ",s7Inm5,s8Inm6,"  ",s7Inm7,s8Inm8)
    print(p8Inm1,s8Inm2,"  ",p8Inm3,s8Inm4,"  ",p8Inm5,s8Inm6,"  ",p8Inm7,s8Inm8)  
    print(s8Inm1,s8Inm2,"  ",s8Inm3,s8Inm4,"  ",s8Inm5,s8Inm6,"  ",s8Inm7,s8Inm8)
    print(s8Inm2,s8Inm1,"  ",s8Inm4,s8Inm3,"  ",s8Inm6,s8Inm5,"  ",s8Inm8,s8Inm7)
main()