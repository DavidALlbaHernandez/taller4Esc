alcool = 0
gasolina = 0
Diesel = 0
n = 0
while True:
  n=int(input())
  if n == 1:
    alcool += 1
  if n == 2:
    gasolina += 1
  if n == 3:
    Diesel += 1
  if n == 4:
    break  
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(Diesel))
