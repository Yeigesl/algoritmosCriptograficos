#Isabel Gómez Yareli Elizabeth 
#Zavala Estala Lisset
#Grupo 1 Criptografía
#-*- coding: utf8 -*-


#Permutación inicial
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#Permutación inicial para la llave 
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permutacion aplicada a la llave para conseguir Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#Expandimos matriz para obtener una matriz de  48bits para aplicar  xor con  Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]
#SBOX
S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

#Permutación para cada SBOX después de cada ronda
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Permutación final aplicada al final de las 16 rondas 
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#Matriz que determina el desplazamiento para  cada ronda de llaves 
DES = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def cadenaABit(texto):#Convierte la cadena en una lista de bits
    arreglo = list()
    for letra in texto:
        valbin = valorBinario(letra, 8)#Valor de char a  byte
        arreglo.extend([int(x) for x in list(valbin)]) #Añade bits al final de la lista
    return arreglo

def bitArregloACad(arreglo): #Regresa  la cadena del arreglo de bits 
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in 
    divideCadena(arreglo,8)]])   
    return res

def valorBinario(val, tamBit): #Devuelve el  valor binario como una cadena del tamaño dado 
    valbin = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(valbin) > tamBit:
        raise "El valor binario no es tan largo como se esperaba"
    while len(valbin) < tamBit:
        valbin = "0"+valbin #Se agregan los ceros necesarios
    return valbin

def divideCadena(s, n):#División de la lista en tamaño n 
    return [s[k:k+n] for k in range(0, len(s), n)]
CIFRAR=1
DESCIFRAR=0
class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.claves = list()
        
    def run(self, clave, texto, accion=CIFRAR, relleno=False):
        if len(clave) < 8:
            raise "La clave debería ser mayor a 8 bytes"
        elif len(clave) > 8:
            clave = clave[:8] #Tamaño de clave mayor a 8 cortar para obtener pedazos de 8 
        self.password =clave
        self.texto = texto
        
        if relleno and accion==CIFRAR:
            self.agreRelleno()
        elif len(self.texto) % 8 != 0:#Si no se especifica el tamaño deben ser múltiplos de 8 
            raise "El tamaño de los datos debería se múltiplo de 8"
        
        self.generaClaves() #Genera todas las llaves
        bloqueTexto = divideCadena(self.texto, 8) #Divide el texto en bloques de 8 bytes 
        result = list()
        for bloque in bloqueTexto:#Se recorre cada uno de los bloques
            bloque = cadenaABit(bloque)#Convierte el bloque en un arreglo de bits
            bloque= self.permut(bloque,PI)#Aplicamos la Permutación inicial 
            g, d = divideCadena(bloque, 32) #g(LEFT), d(RIGHT)
            tmp = None
            for i in range(16): #Se hacen las 16 rondas 
                d_e = self.expand(d, E) #Expandimos d para que se pueda aplicar con  Ki(48bits)
                if accion == CIFRAR:
                    tmp = self.xor(self.claves[i], d_e)#En caso de cifar usar Ki
                else:
                    tmp = self.xor(self.claves[15-i], d_e)#En caso de descifrar comenzar con 
                    #la ultima llave
                tmp = self.sustituye(tmp) #Aplica las SBox
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permut(d+g, PI_1) #Ultima Permutación y agregar el resultado al
            #resultado 
        final_res = bitArregloACad(result)
        if relleno and accion==DESCIFRAR:
            return self.removePadding(final_res) #Se quita lo agregado si se decifra y
            #es verdadero 
        else:
            return final_res #Regresa la cadena de cifrado o descifrado
    
    def sustituye(self, d_e):#Sustituimos  bytes usando  SBOX
        subblocks = divideCadena(d_e, 6)#Separamos el arreglo en sublistas de 6  bits 
        result = list()
        for i in range(len(subblocks)): #Aplicamos a todas las sublistas 
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)#Obtenemos la fila con el primer y ultimo bit. 
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Columnas son 2,3,4 y  5 bits
            val = S_BOX[i][row][column] #Toma el valor en la  SBOX apropiado para la ronda  (i)
            bin = valorBinario(val, 4)#Convertimos el valor a binario 
            result += [int(x) for x in bin]#Agregamos el resultado a la lista 
        return result
        
    def permut(self, block, table):#Permutamos el bloque usando la tabla de permutación
        return [block[x-1] for x in table]
    
    def expand(self, block, table):#Realizamos excatamente lo mismo 
        return [block[x-1] for x in table]
    
    def xor(self, t1, t2):#Aplicamos xor y regresamos el resultado de la lista 
        return [x^y for x,y in zip(t1,t2)]
    
    def generaClaves(self):#Algortimos que genera todas las llaves 
        self.claves = []
        clave = cadenaABit(self.password)
        clave = self.permut(clave, CP_1) #Aplicamos la permuatación inicial sobre la llave 
        g, d = divideCadena(clave, 28) #Dividimos en  (g->LEFT),(d->RIGHT)
        for i in range(16):#Hacemos las 16 rondas 
            g, d = self.desplaza(g, d, DES[i]) #Aplicamos el desplazamiento asociado 
            #con la ronda  no siempre 1
            tmp = g + d #Las unimos 
            self.claves.append(self.permut(tmp, CP_2)) #Aplicamos la permutacion en
            #llave para obtener  Ki

    def desplaza(self, g, d, n): #Desplazamos la lista con el valor dado
        return g[n:] + g[:n], d[n:] + d[:n]
    
    def agregaRelleno(self):#Agregamos relleno utilizando la especificación PKCS5
        rell_len = 8 - (len(self.texto) % 8)
        self.texto += rell_len * chr(pad_len)
    
    def quitaRelle(self, data):#Removemos el relleno del texto plano 
        rell_len = ord(data[-1])
        return data[:-rell_len]
    
    def cifra(self, clave, texto, relleno=False):
        return self.run(clave, texto, CIFRAR, relleno)
    
    def descifra(self, clave, texto, relleno=False):
        return self.run(clave, texto, DESCIFRAR, relleno)
    
if __name__ == '__main__':
    clave = "Santiago"
    texto= "Denytamo"
    d = des()
    mensajeCifrado = d.cifra(clave,texto)
    mensajeDescifrado = d.descifra(clave,mensajeCifrado)
    print("Cifrado: ",mensajeCifrado)
    print("Descifrado: ", mensajeDescifrado)
