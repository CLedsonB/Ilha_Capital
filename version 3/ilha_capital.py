#Sistema de ganhos e gastos
#Guarda dois sistemas de moeda
#Fazer conversao entre eles
#Sistema para ganha dinheiro acertando calculos
#Sistema para ganha dinheiro acertando palavras
#Gastar dinheiro com besteira
from bd_ilha import *
obs = False
clear()

carregamento()
usuario = intro()

while True:
	clear()
	barra = []
	for i in range(10):
        	p = ('x','o')[i < vida]
        	barra.append(p)
	barra = ' '.join(map(str,barra))

	print(f'''
					 Dia : {dias}
					Vida : [ {barra} ]

    -- Digite um dos numeros a seguir, {usuario} :

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
		obs = True
		print('\n[ERROR] - Não é um número (o_O)')

	if opc == 1:
		exibirSaldo()
	elif opc == 2:
		clear()
		doit = ganharDoits()
	elif opc == 3:
		clear()
		braga = ganharBragas()
	elif opc == 4:
		clear()
		braga, doit = conversao()
	elif opc == 5:
		clear()
		braga, doit = compras()
	elif opc == 6:
		exibirItens()
	elif opc == 7:
		clear()
		itemPeca = fugir()
	elif opc == 8:
		clear()
		encerramento()
	elif opc == 34:
		clear()
		bugImagem()
	else:
		print('\n[ERROR] - Número sem utilidade (~_~)')

	vida = alimentacao()
	dias = contarDias()
	limpar(2)
