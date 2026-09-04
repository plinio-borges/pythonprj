#!/usr/bin/env python3

autor = "Fabio Pires"
#Lista: é uma sequencia ordenada de valores (entre colchetes).

portas_alvo = [22, 80, 443, 3306, 8080, 3000, 5000, 8000, 137, 138, 139, 445, "DNS"]
portas_alvo.append(21) #Adiciona a porta 21 na variável portas_alvo
servicos = [ "ssh", "https", "dns" ]

print('A lista de portas é:', portas_alvo)
print(f'A lista de portas é: {portas_alvo}')

print("O índice 2 tem o valor: ", portas_alvo[2])
print("O índice -1 tem o valor: ", portas_alvo[-1])

#lista=[]
for NUM in range(10):
        print(NUM)

for NUM in range(10):
        print(portas_alvo[NUM])

for NUM in range(1,11):
        print(NUM)

for NUM in range(1,11):
	print(portas_alvo[NUM])

#Dicionaries: é um tipoo de dado que trabalha sobre chave:valor

status_servico = {
	'host': '8.8.8.8',
	'porta': '443',
	'estado': 'aberta',
	'servico': 'https',
}

print(status_servico['host'])
print(status_servico['servico'])

servicos = {22: 'SHH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MYSQL', 'DNS': 53}

for PORTA in portas_alvo:
	nome = servicos.get(PORTA, 'desconhecido' )
	print(f'Porta {PORTA}: Servico {nome} ')
