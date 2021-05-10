"""
#entradas
valor de rango-->int--->lista
#salidas
valor de la lista--->int--> divisibles de (i%7)
"""
lista=[]
for i in range(1,101):
  if(i%7!=0):
    lista.append(i)
print(lista) 