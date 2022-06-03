#Sistema de ganhos e gastos
#Guarda dois sistemas de moeda
#Fazer conversao entre eles
#Sistema para ganha dinheiro acertando calculos
#Sistema para ganha dinheiro acertando palavras
#Gastar dinheiro com besteira
from bd_ilha import *

print('\t***Bem vindo a ilha capital***\n')
print('''
Você estava em um navio que afundou,
após dias cercado de água por todos os lados
você finalmente encontra uma ilha...
bem desenvolvida e tecnológica, a questão
é que você está preso, ninguém consegue acessa
essa ilha naturalmente, como única saida
você acumula dinheiro para fugir.\n
''')

while True:
	print('''
	--Digite um dos numeros a seguir:
	1 - Consultar Saldo
	2 - Ganhar Doits
	3 - Ganhar Bragas
	4 - Converter suas moedas
	5 - Fazer compras
	6 - Encerrar partida
	''')
	opc = ''
	try:
		opc = int(input(' ~> '))
	except:
		print('\n[ERROR] - Não é um número (~_~)')

	if opc == 1:
		print('\n\tSaldo:\n\t %.2f D$ (Doits)\n\t %.2f B$ (Bragas)' %(doit,braga))
		limpar(3)
	elif opc == 2:
		doit = ganharDoits()
		limpar(4)
	elif opc == 3:
		braga = ganharBragas()
		limpar(4)
	elif opc == 4:
		braga, doit = conversao()
		limpar(5)
	elif opc == 5:
		braga, doit = compras()
		limpar(3)
	elif opc == 6:
		encerramento()
	elif opc == 34:
		bugImagem()
		limpar(1)
	else:
		print('\n[ERROR] - Número sem utilidade (~_~)')
		limpar(2)