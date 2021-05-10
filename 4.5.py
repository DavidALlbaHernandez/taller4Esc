"""
#entradas
valor de terminos--->int--->k
valor a determinar--->int--->v
#salidas
valor rango--->int--> suma valores del rango
"""
k=int(input("Ingrese numero de terminos: "))
v=int(input("Ingrese valor a determinar: "))
suma=0
for i in range(1,k+1):
    suma=suma+((i**2+1)/i)
if(suma>v):
			print("valor superior al rango a determinar")
else:
	print("La suma es " ,round(suma,2))
