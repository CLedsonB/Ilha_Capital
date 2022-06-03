#Sistema de ganhos e gastos
#Guarda dois sistemas de moeda
#Fazer conversao entre eles
#Sistema para ganha dinheiro acertando calculos
#Sistema para ganha dinheiro acertando palavras
#Gastar dinheiro com besteira
from bd_ilha import *

###____________INICIO DO PROGRAMA______###
print('\t***Bem vindo a ilha capital***\n')

print('''
Você estava em um navio que afundou,
após dias cercado de água por todos os lados
você finalmente encontra uma ilha...
bem desenvolvida e tecnológica, a questão
é que você está preso, ninguém consegue acessa
essa ilha naturalmente, como única saida
você aculmula dinheiro para fugir.\n
''')
while True:
	print(
	'''\n--Digite um dos numeros a seguir:
	1 - Consultar Saldo
	2 - Ganhar Doits
	3 - Ganhar Bragas
	4 - Converter suas moedas
	5 - Fazer compras
	6 - Encerrar partida
	''')
	opc = int(input(' ~> '))

	if opc == 1:
		print('\n\tSaldo:\n\t %.2f D$ (Doits)\n\t %.2f B$ (Bragas)' %(doit,braga))
		limpar(3)
	elif opc == 2:
		doit += ganharDoits()
		limpar(4)
	elif opc == 3:
		braga += ganharBragas()
		limpar(4)
	elif opc == 4:
		braga, doit = conversao()
		limpar(5)
	elif opc == 5:
		braga, doit = compras()
	elif opc == 6:
		encerramento()
	elif opc == 34:
		bugImagem()
		limpar(1)
	else:
		print('\tTODO ERRADO')