#Banco de dados ilha_capital
import time as t
import os
from bugs_ilha import *
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

braga = 500
doit = 500
dias = 1
vida = 5
itemKilo = {}
itemUnidade = {}
itemPeca = {}
SIM = ['SIM','Sim','sim','s','S']
NAO = ['NÃO','Não','N','não','n','nao']

#Nomes sem acentos para
#praticidade do usuario
#Suporte da funcao ganheBragas()
nome = [
'Maria','José','Antonio','Joao',
'Ana','Luiz','Paulo','Carlos',
'Manoel','Pedro','Francisca','Frascisco',
'Marcos','Raimundo','Sebastiao','Antonio',
'Marcelo','Jorge','Geraldo','Adriana',
'Sandra','Luis','Fernando','Fabio',
'Roberto','Marcio','Edson','Andre',
'Sergio','Josefa','Patricia','Daniel',
'Rodrigo','Rafael','Joaquim','Vera',
'Ricardo','Eduardo','Tereza','Sonia',
'Alexandre','Rita','Luciana','Claudio',
'Rosa','Benedito','Leandro','Manoela',
'Alice','Mario','Vitor','Beatriz',
'Iago','Matias','Amanda','Elias',
'Joana','Renata','Gabriel','Humberto'
]

#Compras e vendas somente com doits
#Suporte da funcao compras()
joia = [
('Anel de pirata',58.5),
('Anel dragão',37.9),
('Peça de Diamante',740.0),
('Peça de Ouro',530.0),
('Peça de Prata',320.0),
('Peça de Bronze',188.0),
('Peça de Cobre',120.0),
('Brinco estrela',46.9),
('Brinco lua',33.3),
('Colar de peixe',30.3),
('Estatua de sereia',299.8),
('Pingente Ouro branco',120.87),
('Pulseira de Ouro',97.4),
('Pulseira de Prata',54.2),
('Aliança de Ouro',78.4),
('Aliança de Prata',48.2)
]
veiculo = [
('Motocicleta',270.4),
('Bicicleta', 61.3),
('Bicicleta de 3 marchas', 73.3),
('Bicicleta de 8 marchas', 84.9),
('Bicicleta de 12 marchas', 96.2),
('Carro de mão',50.6),
('Triciclo mecânico', 70.89),
('Triciclo motorizado', 134.7),
('Carro de praia', 320.8),
('Patinete', 40.2),
('Skate', 63.2)
]

alimento = [
('Agulha', 5.2),
('Arraia', 22.1),
('Anchova', 12.8),
('Bacalhau', 26.3),
('Baiacu-de-espinhos', 18.2),
('Peixe-Agulha', 5.2),
('Piaba', 16.5),
('Sardinha', 4.5),
('Camarão', 35.4),
('Camarão pistola', 48.3),
('Ostra', 51.2),
('Mexilhão', 32.0),
('Lula', 130.2),
('Polvo',183.9),
('Lagosta', 74.8),
('Bagaço de coco', 20.2),
('Carangueijo', 7.3)
]

pecas = [
('Mastro P',50),
('Paubique',35),
('Toras',20),
# JANGADA 0 - 2
('Vela',30),
('Quilha',20),
('Trapezio',100),
('Cordas de controle',35),
('Estrutura de sustentacao',80),
# ASA DELTA 3 - 7
('Envoltorio',50),
('Cesto',35),
('Queimador',70),
('Tanque de propano',120),
('Cordas de suspensao',40),
('Valvula de parachute',60),
('Altimetro',100),
# BALAO 8 - 14
('Casco',35),
('Proa',40),
('Popa',50),
('Conves',120),
('Leme',80),
('Helice',90),
('Mastro G',40),
('Ancora',60),
('Ponte de comando',120),
# NAVIO 15 - 23
]

pecas1 = [tupla for indice, tupla in enumerate(pecas) if indice <= 2 ]
pecas2 = [tupla for indice, tupla in enumerate(pecas) if indice >= 3 and indice <= 7]
pecas3 = [tupla for indice, tupla in enumerate(pecas) if indice >= 8 and indice <= 14]
pecas4 = [tupla for indice, tupla in enumerate(pecas) if indice >= 15 and indice <= 23]


#Transforma todas as primeiras letras
#da frase em Maiusculas

#def maiuscula(frase):
#	novaPalavra = " "
#	frase = frase.split(" ")
#	for palavra in frase:
#		novaPalavra = novaPalavra + palavra.capitalize() + ' '
#	return novaPalavra

def limpar(seg):
	input('\nPressione [ENTER] para continuar...\n')
	print('\n\t...limpando tela...')
	t.sleep(seg)
	clear()

#_______Converte strings e inteiros____
#em float
def floatConversor(s):
	ponto = s.find('.')
	virgula = s.find(',')
	try:
		if ponto > 0:
			total = round(float(s),2)
		elif virgula > 0:
			ponto = virgula
			inteiros = s[:ponto]
			inteiros = float(inteiros)
			centavos = s[ponto+1:]
			centavos = float(centavos)
			while centavos > 1:
				centavos /= 10
			total = inteiros+round(centavos,2)
		elif ponto and virgula == -1:
			total = round(float(s),2)
		else:
			print('\n[ERROR] - ALGO INESPERADO ACONTECEU [V_V]')
		return total
	except:
		return print('[ERROR] - Não é um número')


#_______Acerte calculos e ganhe doits______
def ganharDoits():
	global doit
	premio, soma = 0,0
	print('\n\tResponda aos calculos e ganhe Doits!!!\n')
	try:
		for num in range(5):
			valor1 = rand(30) + 1
			valor2 = rand(30) + 1
			print(valor1,'+',valor2)
			valor = input(' ~> ')
			valor = floatConversor(valor)
			premio = (rand(100)+1) / 10 #[1,10]

			if valor == valor1+valor2:
				soma += premio
				print('\n\tParabéns!!! Você ganhou',premio,'D$\n')
			elif valor == 99:
				bug99()
				break
			elif valor == 91625:
				bugDoit()
				soma += 100
			else:
				soma -= premio
				print('\n\t[ERROR] (!_!) Você perdeu',premio,'D$\n\tRESPOSTA: ',valor1+valor2,'\n')
		print("---- Balanço final : %.2f D$ ----\n" %(soma))
		doit += soma
		print('\nFIM DA PARTIDA\n')
	except:
		print('\n[ERROR] - (>.<) Algo de errado não está certo...\nSeu saldo não foi afetado\n')
	return doit

#_____Acerte os nomes e ganhe bragas_____
def ganharBragas():
	global nome, braga
	soma = 0
	print('\nDescubra o nome e ganhe Bragas!!\n')
	print('-Não se precupe com acentos e simbolos-\n')
	for num in range(5):
		premio = (rand(100)+1) / 10 #[1,10]
		local = nome[rand(len(nome))]
		lacunas = local.replace(local[rand(len(local))],'_')
		lacunas2 = lacunas.replace(local[rand(len(local))],'_')
		print('  [',lacunas2,']')
		nomeX = input("\n ~> ")
		if nomeX.capitalize() == local:
			soma += premio
			print('\n\tParabéns!! Você ganhou',premio,'B$\n')
		elif nomeX == '.':
			bug991()
			break
		elif nomeX == 'braga':
			bugBraga()
			soma += 100
		else:
			soma -= premio
			print('\n\t[ERROR] |_(>.<)_| Você perdeu',premio,'B$\n\tRESPOSTA:', local,'\n')
	print("---- Balanço final : %.2f B$ ----\n" %(soma))
	braga += soma
	print('\nFIM DA PARTIDA\n')
	return braga

#_______________Converter suas moedas_______
#Braga <-> Doit
def conversao():
	global doit, braga
	msm = '''
\t***Conversão realizada***
\nGraças ao nosso sistema de deposito
imediato o valor convetido já se
encotra disponivel para uso. Bom proveito\n
'''
	print('''
	Sabendo que:
	1 D$ = 1.6 B$
	1 B$ = 0.625 D$
	\nDigite que tipo de conversão deseja:\n
	1 - Doits --> Braga
	2 - Braga --> Doits
	''')
	num = input(' ~> ')
	try:
		num = floatConversor(num)
		if num == 1:
			d = input('Quantidade de Doits para converter?\n ~> ')
			d = floatConversor(d)

			if d > doit:
				print('\nVocê não tem tudo isso, meu caro (^_^)')
			else:
				convertido = d*1.6
				doit -= d
				braga += convertido
				print('\n%.2f D$ = %.2f B$' %(d,d*1.6))
				print('\n\tProcessando solicitação...')
				t.sleep(2)
				print(msm)

		elif num == 2:
			b = input('Quantidade de Bragas para converter?\n ~> ')
			b = floatConversor(b)
			if b > braga:
				print('\nVocê não tem tudo isso, meu caro (v_V)')
			else:
				convertido = b*0.625
				braga -= b
				doit += convertido
				print('\n%.2f B$ = %.2f D$' %(b,b*0.625))
				print('\n\tProcessando solicitação...')
				t.sleep(2)
				print(msm)
		else:
			print('\nTODO ERRADO - Número sem utilidade\n')
	except:
		print('\n[ERROR] - Não é um número .\ _(0_0)_ /. ')
	return (braga,doit)

#Suporte da funcao compras()
def transacao(lista,moeda,varejo):
	global SIM,NAO
	lista.sort()

	while True:
		clear()
		i = 1
		if len(lista) == len(alimento):
			print('\tSaldo : ',moeda,' B$\n')
			for (item,valor) in lista:
				print(' ',i,'.',item,' = ',valor,'B$')
				i += 1
		else:
			print('\tSaldo : ',moeda,' D$\n')
			for (item,valor) in lista:
				print (' ',i,'.',item,' = ',valor,'D$')
				i += 1
		print('\n***Insira 0 para encerrar as compras\n')

		try:
			produto = int(input('Insira o número do produto\n ~> '))
		except:
			print('[ERROR] - Não dá pra trabalha com esse valor (0_0)')
			break
		if produto > len(lista):
			print('\n[ERROR] - Número inválido (0.0)\n')
			break
		if produto == 0:
			print('\n\t<3 Volte sempre <3\n')
			break
		try:
			quantidade = input('\nQuantidade desse produto ( unidade / kilo )\n ~> ')
			if len(lista) == len(alimento):
				quantidade = floatConversor(quantidade)
			elif len(lista) != len(alimento):
				quantidade = int(quantidade)
		except:
			print('\n[ERROR] - Não posso trabalhar com esse valor [-__-]')
			break
		subtotal = lista[produto-1][1] * quantidade
		subtotal = round(subtotal,2)
		if len(lista) == len(alimento):
			print('\n',lista[produto-1][0],'.....',quantidade,'Kgs' if quantidade > 1 else 'Kg',' = ',subtotal,'B$\n')
		else:
			print('\n',lista[produto-1][0],'.....',quantidade,'Unidades' if quantidade > 1 else 'Unidade',' = ', subtotal,'D$\n')
		while True:
			confirmar = input('Confirme a compra com sim ou nao\n ~> ')
			print('\n')
			if SIM.count(confirmar) == 1:
				if moeda >= subtotal:
					moeda -= subtotal
					print('\tCompra concluída $$')
					try:
						varejo[lista[produto-1][0]] += quantidade
					except:
						varejo[lista[produto-1][0]] = quantidade
				else:
					print('\t[ERROR] - Você não tem saldo suficiente :(')
			elif NAO.count(confirmar) == 1:
				print('\tCompra cancelada, tente de novo\n\tnosso produtos são da melhor qualidade :D')
			else:
				print('\t[ERROR] - Comando invalido, tente novamente (0.0) ')
			t.sleep(2)
			print('\n')
			break
	return (lista,moeda, varejo)


def transacaoPecas(lista, moeda, varejo):
	global SIM, NAO
	codigo = []

	print('\tSaldo : ',moeda,' D$\n')
	for i in range(3):
		num = rand(len(pecas))
		codigo.append(num)
		nome, valor = pecas[num]
		print (' ',num+1,'.',nome,' = ',valor,'D$')
	print('\n***Insira 0 para encerrar a compra\n')

	try:
		produto = int(input('Insira o número do produto\n ~> '))
	except:
		print('[ERROR] - Não dá pra trabalha com esse valor (0_0)')
	if produto > len(lista):
		print('\n[ERROR] - Número inválido (U_U)>|_| COOFFE PLEASSE\n')
	elif produto == 0:
		print('\n\t<3 Volte sempre <3\n')
	elif  produto-1 in codigo:
		item = lista[produto-1][0]
		valor = lista[produto-1][1]
		print('\n',item,'..... 1 Unidade = ',valor,'D$\n')
		while True:
			confirmar = input('Confirme a compra com sim ou nao\n ~> ')
			print('\n')
			if SIM.count(confirmar) == 1:
				if moeda >= valor:
					moeda -= valor
					print('\tCompra concluída $$')
					try:
						varejo[item] += 1
					except:
						varejo[item] = 1
				else:
					print('\tVocê não tem saldo suficiente :(')
			elif NAO.count(confirmar) == 1:
				print('\tCompra cancelada, tente de novo\n\tnosso produtos são da melhor qualidade :D')
			else:
				print('\t[ERROR] - Comando invalido, tente novamente ($_$)')
			t.sleep(2)
			print('\n')
			break
	else:
		print('\n [ERROR] - Codigo invalido :~( RESFRIADO')
	return (lista,moeda,varejo)

#____Gaste aqui seu suado dinheiro____
def compras():
	global doit,braga, itemUnidade,itemKilo, itemPeca
	print('''
	****BEM VINDO***

	realize aqui suas compras

	1.Mercado de Joias
	2.Mercado de Veiculos
	3.Mercado de Alimentação
	4.Mercado de Pecas de veiculos

	''')
	mercado = input('\t ~> ')
	mercado = floatConversor(mercado)
	clear()
	if mercado == 1:
		global joia
		joia,doit,itemUnidade = transacao(joia,doit,itemUnidade)
	elif mercado == 2:
		global veiculo
		veiculo,doit,itemUnidade = transacao(veiculo,doit,itemUnidade)
	elif mercado == 3:
		global alimento
		alimento,braga,itemKilo = transacao(alimento,braga,itemKilo)
	elif mercado == 4:
		global pecas
		pecas,doit,itemPeca = transacaoPecas(pecas,doit,itemPeca)
	else:
		print('\n[ERROR] - Mercado inexistente!')
	return (braga,doit)


#______Sistema de fuga_______________

def fugir():
	global itemPeca
	print('''
	****BEM VINDO***

	Escolha um modo de fuga

	1. Jangada
	2. Planador
	3. Balao
	4. Navio

	''')
	num  = input('\t ~> ')
	num  = floatConversor(num)
	clear()
	if num == 1:
		global pecas1
	elif num == 2:
		global pecas2
	elif num == 3:
		global pecas3
	elif num == 4:
		global pecas4
	else:
		print('\n[ERROR] - Modo de fuga inexistente!')


def tentativaFuga(inventario, pecasNecess, numPecas, taxa):
	nomes = [nome[0] for nome in inventario]
	conta = sum(1 for chave in nomes if chave in pecasNecess)

	if conta == numPecas:
		# TENTANDO BASEADO NA TAXA DE SUCESSO DO MEIO DE TRANSPORTE
		chanceFuga = 1 / taxa  * 100
		indice = rand(100) + 1
		if indice > chanceFuga:
            		print('Fuga mau sucedida')
			# NAO CONSEGIU
			# REMOVER 1 UNIDADE DE CADA PECA
		else:
			print('fuga bem sucedida')
			# FUGA BEM SUCEDIDA
	else:
		print('Quantidade de pecas insuficiente para uma fuga')

#______Sistema de sobrevivencia_______

def alimentacao():
	global vida, itemKilo

	if itemKilo:
		ultA = list(itemKilo.keys())[-1]
		ultK = itemKilo[ultA]
		size = len(itemKilo)

		if size > 0:
			if ultK > 0.5:
				itemKilo[ultA] -= 0.5
				if vida < 10:
					vida += 1
			else:
				if vida < 10:
					vida += 1
				itemKilo.pop(ultA)
	else:
		if vida > 1:
			vida -= 1
		else:
			vida = 0
			print('\n\n\t[NAO SOBREVIVEU]\n\n')
			encerramento()
	return vida


#  lista   | 0 | 0 |  3  |  2  |  1  |  1  |  1  |  1  |  1  |
#  comida  | 0 | 0 | 0.5 | 0.5 | 2.5 | 2.0 | 1.5 | 1.0 | 0.5 |
#  vida    | 5 | 4 |  5  |  6  |  7  |  8  |  9  |  10 | 10  |


def encerramento():
	print('\n\t...FIM DE JOGO...\nSeja mais forte da proxima vez... lol\n')
	exit()
