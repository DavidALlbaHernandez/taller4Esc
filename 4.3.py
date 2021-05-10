"""
#entradas
valor de rango-->int--->lista
#salidas
valor de la lista--->int--> valores contados
"""
contador=0
for i in range(97,1004):
  if(i%2==0):
    contador=contador+i
print(contador)    
