#!/usr/bin/env python3

notas = []
soma = 0
for nota in range(1,6):
  while True:
   try:
       nota2 = float(input("digite a nota %d de 5: " %nota))
       if 0 <= nota2 <= 10:
          break
   except ValueError:
       printf("Digite apenas numeros")
notas.append(nota2)
soma += nota2
print(soma)

for nota in range(5):
	print("Nota %d: %.2f" %(nota+1, notas[nota]))

print ("A Media é: %.2f" %(soma/5))
