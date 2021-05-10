"""
#entradas
valor entero mayor--->int--->N
valor entero menor--->int--->k
#salidas
valor de la lista--->int--> N-i=k
"""
N=int(input("ingrese valor de N: "))
K=int(input("Ingrese valor de K: "))
while (N>K):
  lista=[]
  for i in range (K,N+1):
    lista.append(i)
  lista.sort(reverse=True)
  print(lista)
  break
else:
  print("el valor de K debe ser menor que el valor de N")

