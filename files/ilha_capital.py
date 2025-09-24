#Sistema de ganhos e gastos
#Guarda dois sistemas de moeda
#Fazer conversao entre eles
#Sistema para ganha dinheiro acertando calculos
#Sistema para ganha dinheiro acertando palavras
#Gastar dinheiro com besteira
from bd_ilha import *
clear()

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
	print(f'''
						 Dia : {dias}
						Vida : {vida}
	--Digite um dos numeros a seguir:

	1 - Consultar Saldo
	2 - Ganhar Doits
	3 - Ganhar Bragas
	4 - Converter suas moedas
	5 - Fazer compras
	6 - Seus itens
	7 - Tentar fugir
	8 - Desistir
	''')

	try:
		opc = ''
		opc = int(input(' ~> '))
	except:
		print('\n[ERROR] - Não é um número (o_O)')

	clear()
	if opc == 1:
		print('\n\tSaldo:\n\t %.2f D$ (Doits)\n\t %.2f B$ (Bragas)' %(doit,braga))
		limpar(3)
	elif opc == 2:
		doit = ganharDoits()
		limpar(3)
	elif opc == 3:
		braga = ganharBragas()
		limpar(3)
	elif opc == 4:
		braga, doit = conversao()
		limpar(5)
	elif opc == 5:
		braga, doit = compras()
		limpar(3)
	elif opc == 6:
		print('Alimentos'.center(15,'_'))
		print('')
		for key in itemKilo.keys():
			print(' ~> ',key,' : ',itemKilo[key],'Kgs' if itemKilo[key] > 1 else 'Kg')
		print()

		print('Objetos'.center(15,'_'))
		print('')
		for key in itemUnidade.keys():
			print(' ~> ', key,': ',itemUnidade[key],'Unidades' if itemUnidade[key] > 1 else 'Unidade')
		print()

		print('Pecas'.center(15,'_'))
		print('')
		for key in itemPeca.keys():
			print(' ~> ', key,': ',itemPeca[key],'Unidades' if itemPeca[key] > 1 else 'Unidade')
		limpar(1)

	elif opc == 7:
		fugir()
	elif opc == 8:
		encerramento()
	elif opc == 34:
		bugImagem()
		limpar(1)
	else:
		print('\n[ERROR] - Número sem utilidade (~_~)')
		limpar(2)

	vida = alimentacao()
	dias += 1
