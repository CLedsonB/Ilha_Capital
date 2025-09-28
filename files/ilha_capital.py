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
	carregamento()
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
		limpar(3)
	elif opc == 2:
		clear()
		doit = ganharDoits()
		limpar(3)
	elif opc == 3:
		clear()
		braga = ganharBragas()
		limpar(3)
	elif opc == 4:
		clear()
		braga, doit = conversao()
		limpar(5)
	elif opc == 5:
		clear()
		braga, doit = compras()
		limpar(3)
	elif opc == 6:
		exibirItens()
		limpar(1)
	elif opc == 7:
		clear()
		itemPeca = fugir()
		limpar(2)
	elif opc == 8:
		clear()
		encerramento()
	elif opc == 34:
		clear()
		bugImagem()
		limpar(1)
	else:
		if obs == True:
			limpar(2)
		else:
			print('\n[ERROR] - Número sem utilidade (~_~)')
			limpar(2)

	vida = alimentacao()
	dias = contarDias()
