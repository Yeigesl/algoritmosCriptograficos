abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
RFC="IAGY9704103T"
clave="ALEXPECKS"
import numpy
import gmpy2


def elmentos(lista):
	posiciones=[]
	for i in lista:                
	  if i in abc:                        
	    posiciones.append(abc.index(i))
	return posiciones



def cifra(trigrama,k):
	valTri=[]
	e=0
	otp=[]
	total=[]
	oTP=[]
	tam=3
	for i in range(len(k)):
		c=trigrama[e]*k[i]
		otp.append(c)

		e+=1
		if e==3:
		    e=0
	#print("Antes de sumar:",otp)
	while len(otp)>tam:
		pedazo=otp[:tam]
		total.append(pedazo)
		otp=otp[tam:]
	total.append(otp)
		#print("valores cortados",total)
	for elemento in total:
		suma=sum(elemento)% len(abc)	
		oTP.append(suma)
	return oTP


def dCifra(trigrama,k):
	valTri=[]
	e=0
	otp=[]
	total=[]
	oTP=[]
	tam=3
	for i in range(len(k)):
		c=trigrama[e]*k[i]
		otp.append(c)
		e+=1
		if e==3:
		    e=0
	#print("Antes de sumar:",otp)
	while len(otp)>tam:
		pedazo=otp[:tam]
		total.append(pedazo)
		otp=otp[tam:]
	total.append(otp)
		#print("valores cortados",total)
	for elemento in total:
		suma=sum(elemento)% len(abc)	
		oTP.append(suma)
	return oTP
    
    
def cifrar(valoresCif):
	mensajeCifrado=[]
	for i in range(len(valoresCif)):
		mensajeCifrado.append(abc[valoresCif[i]])
	return mensajeCifrado


def dCifrar(valoresCif):
	mensajeDCifrado=[]
	for i in range(len(valoresCif)):
		mensajeDCifrado.append(abc[valoresCif[i]])
	return mensajeDCifrado


def divide(lista,tam):
	total=[]
	while len(lista)>tam:
		pedazo=lista[:tam]
		total.append(pedazo)
		lista=lista[tam:]
	total.append(lista)
	return total
  
def calcula(lista):
	res1=(lista[0]*lista[3])
	res2=(lista[1]*lista[2])
	res=(res1-res2)%len(abc)
	return res

def calInv(lista,v):
	inversa=[]
	for i in range(len(lista)):
		val=(lista[i]*v)%len(abc)
		inversa.append(val)
	return inversa
		    
def main():
	print("Los valores de sus letras son")
	elemen=elmentos(RFC)
	print("Mensaje:",elemen)
	cEle=elmentos(clave)
	print("Clave:",cEle)
	#print("Procedemos a cifrar")
	#print("Los trigramas para el mensaje serán los siguientes")
	#print(elemen[0:3])
	#print(elemen[3:6])
	#print(elemen[6:9])
	#print(elemen[9:12])
	#print("Los valores ya aplicado el modulo y sumados son:")
	c1_3=cifra(elemen[0:3],cEle)
	#print(c1_3)
	c4_6=cifra(elemen[3:6],cEle)
	#print(c4_6)
	c7_9=cifra(elemen[6:9],cEle)
	#print(c7_9)
	c10_12=cifra(elemen[9:12],cEle)
	#print(c10_12)
	valoresCif=c1_3+c4_6+c7_9+c10_12
	print("En general los valores para sustituir en cifrado son:")
	print(valoresCif)
	cif=cifrar(valoresCif)
	print("Mensaje Cifrado:",cif)
	print("Posteriormente procedemos a obtener el descifrado")
	print("Primero calculamos el determinante")
	matK=divide(cEle,3)
	print(matK)
	det=numpy.linalg.det(matK)
	print("Det(K):",round(det))
	tam=len(abc)
	print("Posteriormente calculamos el inverso multiplicativo")
	modulo=int(round(det%tam))
	print("MOD:",modulo)
	inverso=int(gmpy2.invert(modulo,tam))
	print("INV_DET:",inverso)
	nNUm=modulo*inverso
	mod=gmpy2.invert(nNUm,tam)
	print("mod:",mod)
	print("Procedemos a obtener la adjunta de K")
	print("Si la clave es:",cEle)
	cf1=cEle[4:6]+cEle[7:9]
	#print("cf1:",cf1)
	cf1R=calcula(cf1)
	#print("res1:",cf1R)
	cf2=[]
	cf2.append(cEle[3])
	cf2.append(cEle[5])
	cf2.append(cEle[6])
	cf2.append(cEle[8])
	#print("cf2:",cf2)
	cf2R=-(calcula(cf2))
	#print("res2:",cf2R)
	cf3=[]
	cf3.append(cEle[3])
	cf3.append(cEle[4])
	cf3.append(cEle[6])
	cf3.append(cEle[7])
	#print("cf3:",cf3)
	cf3R=calcula(cf3)
	#print("res3:",cf3R)
	cf4=[]
	cf4.append(cEle[1])
	cf4.append(cEle[2])
	cf4.append(cEle[7])
	cf4.append(cEle[8])
	#print("cf4:",cf4)
	cf4R=-(calcula(cf4))
	#print("res4:",cf4R)
	cf5=[]
	cf5.append(cEle[0])
	cf5.append(cEle[2])
	cf5.append(cEle[6])
	cf5.append(cEle[8])
	#print("cf4:",cf5)
	cf5R=calcula(cf5)
	#print("res4:",cf5R)
	cf6=[]
	cf6.append(cEle[0])
	cf6.append(cEle[1])
	cf6.append(cEle[6])
	cf6.append(cEle[7])
	#print("cf6:",cf6)
	cf6R=-(calcula(cf6))
	#print("res4:",cf6R)
	cf7=[]
	cf7.append(cEle[1])
	cf7.append(cEle[2])
	cf7.append(cEle[4])
	cf7.append(cEle[5])
	#print("cf7:",cf7)
	cf7R=calcula(cf7)
	#print("res7:",cf7R)
	cf8=[]
	cf8.append(cEle[0])
	cf8.append(cEle[2])
	cf8.append(cEle[3])
	cf8.append(cEle[5])
	#print("cf8:",cf8)
	cf8R=-(calcula(cf8))
	#print("res7:",cf8R)
	cf9=[]
	cf9.append(cEle[0])
	cf9.append(cEle[1])
	cf9.append(cEle[3])
	cf9.append(cEle[4])
	#print("cf9:",cf9)
	cf9R=calcula(cf9)
	#print("res7:",cf9R)
	mAdjK=[]
	mAdjK.append(cf1R)
	mAdjK.append(cf2R)
	mAdjK.append(cf3R)
	mAdjK.append(cf4R)
	mAdjK.append(cf5R)
	mAdjK.append(cf6R)
	mAdjK.append(cf7R)
	mAdjK.append(cf8R)
	mAdjK.append(cf9R)
	mTAdjK=[]
	mTAdjK.append(cf1R)
	mTAdjK.append(cf4R)
	mTAdjK.append(cf7R)
	mTAdjK.append(cf2R)
	mTAdjK.append(cf5R)
	mTAdjK.append(cf8R)
	mTAdjK.append(cf3R)
	mTAdjK.append(cf6R)
	mTAdjK.append(cf9R)
	mAdjKD=divide(mAdjK,3)
	mTAdjKD=divide(mTAdjK,3)
	print("Por lo que la matriz adjunta de k es:")
	print("mAdj(K):",mAdjKD)
	print("Por lo que la matriz transpuesta de la adjunta de k es:")
	print("mTAdj(K):",mTAdjKD)
	print("Para obtener los valores multiplicamos mTAdj(K) por el inv_Det con mod37")
	print("Por lo que la matriz inversa  de k es:")
	inv_K=calInv(mTAdjK,inverso)
	inv_KD=divide(inv_K,3)
	print("MINV_K:",inv_KD)
	print("Ya encontrados los valores procedemos a descifrar")
	cifE=elmentos(cif)
	print("Mensaje Cifrado y sus valores son:",cif,cifE)
	print("Procedemos a DesCifrar")
	print("Los trigramas para el mensaje a descrifrar serán los siguientes")
	print(cifE[0:3])
	print(cifE[3:6])
	print(cifE[6:9])
	print(cifE[9:12])
	#print("Los valores ya aplicado el modulo y sumados son:")
	d1_3=dCifra(cifE[0:3],inv_K)
	#print(d1_3)
	d4_6=dCifra(cifE[3:6],inv_K)
	#print(d4_6)
	d7_9=dCifra(cifE[6:9],inv_K)
	#print(d7_9)
	d10_12=dCifra(cifE[9:12],inv_K)
	#print(d10_12)
	valoresDcif=d1_3+d4_6+d7_9+d10_12
	print("En general los valores para sustituir son:")
	print(valoresDcif)
	dCif=dCifrar(valoresDcif)
	print("Mensaje Claro:",dCif)


	



main()
