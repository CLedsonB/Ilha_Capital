#Banco de dados ilha_capital
import time as t
import os
from bugs_ilha import *
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

usuario = ''
braga = 0
doit = 0
dias = 1
vida = 5
falha = 0
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
'Joana','Renata','Gabriel','Humberto',
'Stefane','Cleiton'
]

pais = [
'Argentina','Australia','Belgica','Brasil','Canada',
'China','Egito','Franca','Alemanha','Grecia',
'Mexico','India','Italia','Japao','Nigeria',
'Paquistao','Russia','Polonia','Ucrania','Arabia Saudita',
'Espanha','Tailandia','Angola','Bangladesh','Colombia',
'Turquia','Indonesia','Holanda','Portugal','Israel',
'Venezuela','Chile','Filipinas','Romania'
]

comida = [
'Rabanada','Polenta','Risole','Strogonofe','Coxinha',
'Moqueca','Quiabada','Feijoada','Lasanha','Passarinha',
'Bisteca','Peixada','Churrasco','Picanha','Sopa',
'Frango','Figado','Abobrinha','Lasanha','Hamburguer',
'Polvilho'
]

#Compras e vendas somente com doits
#Suporte da funcao compras()
joia = [ # 16
('Anel de pirata',68.5),
('Anel dragão',47.9),
('Peça de Diamante',740.0),
('Peça de Ouro',530.0),
('Peça de Prata',320.0),
('Peça de Bronze',188.0),
('Peça de Cobre',120.0),
('Brinco estrela',56.9),
('Brinco lua',43.3),
('Colar de peixe',40.3),
('Estatua de sereia',299.8),
('Pingente Ouro branco',130.87),
('Pulseira de Ouro',107.4),
('Pulseira de Prata',64.2),
('Aliança de Ouro',88.4),
('Aliança de Prata',58.2)
]
veiculo = [ # 14
('Motocicleta',270.4),
('Bicicleta', 61.3),
('Bicicleta de 3 marchas', 73.3),
('Bicicleta de 8 marchas', 84.9),
('Bicicleta de 12 marchas', 96.2),
('Carro de mão',50.6),
('Triciclo mecânico', 70.89),
('Triciclo motorizado', 134.7),
('Carro de praia', 360.8),
('Patinete', 40.2),
('Skate', 63.2),
('Moto', 320.5),
('Andador',45.9),
('Carrinho de bebe', 140.3)
]

alimento = [
('Agulha', 15.2),
('Arraia', 32.1),
('Anchova', 22.8),
('Bacalhau', 26.3),
('Baiacu-de-espinhos', 18.2),
('Peixe-Agulha', 5.2),
('Piaba', 36.5),
('Sardinha', 14.5),
('Camarão', 45.4),
('Camarão pistola', 58.3),
('Ostra', 51.2),
('Mexilhão', 32.0),
('Lula', 130.2),
('Polvo',183.9),
('Lagosta', 74.8),
('Bagaço de coco', 28.2),
('Carangueijo', 47.3),
('Amora',30.4),
('Mamao', 25.6),
('Graviola', 45.7)
]

pecas = [
('Mastro P',50),('Paubique',35),('Toras',20),
# JANGADA 0 - 2
('Vela',30),('Quilha',20),('Trapezio',100),
('Cordas de controle',35),('Estrutura de sustentacao',80),
# ASA DELTA 3 - 7
('Envoltorio',50),('Cesto',35),
('Queimador',70),('Tanque de propano',120),
('Cordas de suspensao',40),('Valvula de parachute',80),
('Altimetro',150),
# BALAO 8 - 14
('Casco',85),('Proa',90),
('Popa',100),('Conves',170),
('Leme',130),('Helice',140),
('Mastro G',90),('Ancora',110),
('Ponte de comando',200)
# NAVIO 15 - 23
]
metodoFuga = [['Jangada',3],['Planador',5],['Balao',7],['Navio',9]]

pecas1 = [t for i,t in enumerate(pecas) if i <= 2 ]
pecas2 = [t for i,t in enumerate(pecas) if i >= 3  and i <= 7]
pecas3 = [t for i,t in enumerate(pecas) if i >= 8  and i <= 14]
pecas4 = [t for i,t in enumerate(pecas) if i >= 15 and i <= 23]


def carregamento():
	icone = [
'       o ',
'     o   o',
'    o     o',
'   o       o',
'   o       o',
'    o     o',
'     o   o',
'       o '
]
	print('\n\n')
	for linha in icone:
		print('\t\t',linha)
		t.sleep(0.5)
	clear()

def limpar(seg):
	input('\nPressione [ENTER] para continuar...\n')
	print('\n\t...limpando tela...')
	t.sleep(seg)
	clear()

def contarDias():
	global dias
	dias += 1
	print('\n\t + 1 DIA')
	return dias


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
		return print('\n[ERROR] - Não é um número <-_x>  ')

def intro():
	global usuario
	print('''
	*** Bem vindo a Ilha Capital ***

	Voce estava em um navio que afundou,
	apos dias cercado de agua por todos os lados
	voce foi encontrado desacordado, a ilha possui
	um bom desenvolvimento tecnologico, a questao e
	que voce esta preso, ninguem consegue acessar essa
	essa ilha naturalmente, como unica saida voce acumula
	recursos para fugir.
''')
	usuario = input('Insira o seu nome : ')
	return usuario

def exibirSaldo():
	global doit, braga
	titulo = 'SALDO BANCARIO'.center(5,' ')
	print(f'''
	_________________________
	| {titulo}
	|
	| {doit:.2f} D$
	| {braga:.2f} B$
	|
	-------------------------
''')

def exibirItens():
	global itemKilo, itemUnidade, itemPeca
	inventario = ['Alimentos','Objetos','Pecas']
	clear()
	i = 0
	for nome in inventario:
		print('')
		print(inventario[i].center(15,'_'))
		print('')
		if nome == inventario[0]:
			for key in itemKilo.keys():
				print(' ~> ',key,' : ',itemKilo[key],'Kgs' if itemKilo[key] > 1 else 'Kg')
		elif nome == inventario[1]:
			for key in itemUnidade.keys():
				print(' ~> ',key,' : ',itemUnidade[key],'Unidades' if itemUnidade[key] > 1 else 'Unidade')
		elif nome == inventario[2]:
			for key in itemPeca.keys():
				print(' ~> ',key,' : ',itemPeca[key],'Unidades' if itemPeca[key] > 1 else 'Unidade')
		i += 1

#_______Acerte calculos e ganhe doits______
def ganharDoits():
	global doit
	print('''
	Responda aos calculos e ganhe Doits!!!

	[1]. Adicao / Soma
	[2]. Subtracao
	[3]. Multiplicacao
	[4]. Divisao
	[5]. Aleatorio
''')
	try:
		ope = int(input('\n ~> '))

		print('''
	Escolha o nivel de dificuldade ('o')
	Premios aumentam de acordo a dificuldade ($.$)

			Numeros  |  Premios
	[1]. Facil      [1,10]   |   [1,10]   D$
	[2]. Medio      [10,50]  |   [6,26]   D$
	[3]. Dificil    [50,100] |   [50,150] D$

''')
		nivel = int(input('\n ~> '))

		if ope >= 1 and ope <= 5:
			doit = calcular(ope,nivel)
		else:
			print('\n[ERROR] - Valor invalido E|-|.|-|3 ')
	except:
		print('\n[ERROR] - (>.<) Algo de errado não está certo...\nSeu saldo não foi afetado\n')
	return doit

def calcular(ope,nivel):
	global doit
	premio, soma = 0,0
	clear()

	if nivel == 1:
		x1, x2 = 10, 1   # [1,10]
		p1, p2 = 1, 10   # [1,10]
	elif nivel == 2:
		x1, x2 = 40, 10  # [10,50]
		p1, p2 = 30, 5   # [6,26]
	elif nivel == 3:
		x1, x2 = 50, 50  # [50,100]
		p1, p2 = 50, 1   # [50,150]

	for i in range(5):
		valor1 = rand(x1) + x2
		valor2 = rand(x1) + x2
		premio = (rand(100)+p1) / p2
		if ope == 1:
			print(valor1,' + ',valor2)
			resp = valor1 + valor2
		elif ope == 2:
			print(valor1,' - ',valor2)
			resp = valor1 - valor2
		elif ope == 3:
			print(valor1,' * ',valor2)
			resp = valor1 * valor2
		elif ope == 4:
			print(valor1,' / ',valor2)
			resp = round(valor1 / valor2,2)
		elif ope == 5:
			operador = rand(4) + 1

			if operador == 1:
				print(valor1,' + ',valor2)
				resp = valor1 + valor2
			elif operador == 2:
				print(valor1,' - ',valor2)
				resp = valor1 - valor2
			elif operador == 3:
				print(valor1,' * ',valor2)
				resp = valor1 * valor2
			elif operador == 4:
				print(valor1,' / ',valor2)
				resp = round(valor1 / valor2,2)

		valor = input(' ~> ')
		valor = floatConversor(valor)

		if valor == resp:
			soma += premio
			print('\n\tParabéns!!! Você ganhou',premio,'D$\n')
		elif valor == 0:
			bug99()
			break
		elif valor == 91625:
			bugDoit()
			soma += 100
		else:
			soma -= premio
			print('\n\t[ERROR] (!_!) Você perdeu',premio,'D$\n\tRESPOSTA: ',resp,'\n')

	print("---- Balanço final : %.2f D$ ----\n" %(soma))
	doit += soma
	print('\nFIM DA PARTIDA\n')

	return doit

#_____Acerte os nomes e ganhe bragas_____
def ganharBragas():
	global braga
	soma = 0
	print('''
	Descubra a palavra escondida e ganhe Bragas!!!
	>> Nao precisa considerar acentos e pontuacao <<

	    Categoria |  Premios
	[1]. Nomes    |  [1,10]   B$
	[2]. Paises   |  [10,50]  B$
	[3]. Comida   |  [50,100] B$
''')
	try:
		ope = int(input('\n ~> '))

		if ope >= 1 and ope <= 3:
			braga = cifraBraga(ope)
		else:
			print('\n\t[ERROR] - Valor invalido (>"o"<) ')
	except:
		print('\n\t[ERROR] - (>.<) Algo de errado não está certo...\nSeu saldo não foi afetado\n')
	return braga


def cifraBraga(ope):
	global braga
	premio, soma = 0, 0
	clear()

	if ope == 1:
		global nome
		p1, p2 = 10, 1
		categ = nome
	elif ope == 2:
		global pais
		p1, p2 = 40, 11
		categ = pais
	elif ope == 3:
		global comida
		p1, p2 = 50, 51
		categ = comida

	for num in range(5):
		premio = rand(p1) + p2
		local = categ[rand(len(categ))]
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
	cDoit = 0.625
	cBraga  = 1.6
	msm = '''
\t***Conversão realizada***
\nGraças ao nosso sistema de deposito
imediato o valor convetido já se
encotra disponivel para uso. Bom proveito\n
'''
	print(f'''
	Sabendo que:
	1 D$ = {cBraga} B$
	1 B$ = {cDoit} D$
	\nDigite que tipo de conversão deseja:\n
	[1] - Doits --> Braga
	[2] - Braga --> Doits
	''')

	try:
		num = input(' ~> ')
		num = floatConversor(num)
		if num == 1:
			d = input('Quantidade de Doits para converter?\n ~> ')
			d = floatConversor(d)
			if d > doit:
				print('\nVocê não tem tudo isso, meu caro (^_^)')
			else:
				convertido = round(d*cBraga,2)
				doit -= d
				braga += convertido
				print('\n%.2f D$ = %.2f B$' %(d,convertido))
				print('\n\tProcessando solicitação...')
				carregamento()
				print(msm)

		elif num == 2:
			b = input('Quantidade de Bragas para converter?\n ~> ')
			b = floatConversor(b)
			if b > braga:
				print('\nVocê não tem tudo isso, meu caro (v_V)')
			else:
				convertido = round(b*cDoit,2)
				braga -= b
				doit += convertido
				print('\n%.2f B$ = %.2f D$' %(b,convertido))
				print('\n\tProcessando solicitação...')
				carregamento()
				print(msm)
		elif num > 2 or num < 1:
			print('\nTODO ERRADO - Número sem utilidade\n')
	except:
		return (braga,doit)

	return (braga,doit)

#Suporte da funcao compras()
def transacao(lista,moeda,varejo):
	global SIM,NAO
	lista.sort()
	clear()

	while True:
		clear()
		i = 1

		if len(lista) == len(alimento):
			print('\tSaldo : ',round(moeda,2),' B$\n')
			for (item,valor) in lista:
				print(' ',i,'.',item,' = ',valor,'B$')
				i += 1
		else:
			print('\tSaldo : ',round(moeda,2),' D$\n')
			for (item,valor) in lista:
				print (' ',i,'.',item,' = ',valor,'D$')
				i += 1
		print('\n***Insira 0 para encerrar as compras\n')

		try:
			produto = int(input('Insira o número do produto\n ~> '))
		except:
			print('\n\t[ERROR] - Não dá pra trabalha com esse valor (0_0)')
			return (lista, moeda, varejo)
		if produto > len(lista):
			print('\n\t[ERROR] - Número inválido (0.0)\n')
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
			print('\n\t[ERROR] - Não posso trabalhar com esse valor [-__-]')
			return (lista, moeda, varejo)
		subtotal = lista[produto-1][1] * quantidade
		subtotal = round(subtotal,2)
		if len(lista) == len(alimento):
			print('\n',lista[produto-1][0],'.....',quantidade,'Kgs' if quantidade > 1 else 'Kg',' = ',subtotal,'B$\n')
		else:
			print('\n',lista[produto-1][0],'.....',quantidade,'Unidades' if quantidade > 1 else 'Unidade',' = ', subtotal,'D$\n')
		while True:
			confirmar = input('Confirme a compra ( sim / nao )\n ~> ')
			print('\n')
			if SIM.count(confirmar) == 1:
				if moeda >= subtotal:
					moeda -= subtotal
					print('\t$$  Compra concluída  $$')
					try:
						varejo[lista[produto-1][0]] += quantidade
					except:
						varejo[lista[produto-1][0]] = quantidade
				else:
					print('\n\t[ERROR] - Você não tem saldo suficiente :(')
			elif NAO.count(confirmar) == 1:
				print('\tCompra cancelada, tente de novo\n\tnosso produtos são da melhor qualidade :D')
			else:
				print('\n\t[ERROR] - Comando invalido, tente novamente (0.0) ')
			t.sleep(2)
			print('\n')
			break
	return (lista,moeda, varejo)


def transacaoPecas(lista, moeda, varejo):
	global SIM, NAO, metodoFuga
	codigo = []
	clear()

	print('\tSaldo : ',round(moeda,2),' D$\n')

	i = 1
	f = 0
	for k,v in metodoFuga:
		f += v
		print(f'\n\t[{i},{f}] pecas de {k}')
		i += v
	print()

	for i in range(3):
		num = rand(len(pecas))
		codigo.append(num)
		nome, valor = pecas[num]
		print (' ',num+1,'.',nome,' = ',valor,'D$')
	print('\n***Insira 0 para encerrar a compra\n')

	try:
		produto = int(input('Insira o número do produto\n ~> '))
	except:
		print('\n\t[ERROR] - Não dá pra trabalha com esse valor (0_0)')
		return (lista, moeda, varejo)

	if produto > len(lista):
		print('\n\t[ERROR] - Número inválido (U_U)>|_| COOFFE PLEASSE\n')
	elif produto == 0:
		print('\n\t<3 Volte sempre <3\n')
	elif  produto-1 in codigo:
		item = lista[produto-1][0]
		valor = lista[produto-1][1]
		print('\n',item,'..... 1 Unidade = ',valor,'D$\n')
		while True:
			confirmar = input('Confirme a compra ( sim / nao )\n ~> ')
			print('\n')
			if SIM.count(confirmar) == 1:
				if moeda >= valor:
					moeda -= valor
					print('\t$$  Compra concluída  $$')
					try:
						varejo[item] += 1
					except:
						varejo[item] = 1
				else:
					print('\tVocê não tem saldo suficiente :(')
			elif NAO.count(confirmar) == 1:
				print('\tCompra cancelada, tente de novo\n\tnosso produtos são da melhor qualidade :D')
			else:
				print('\n\t[ERROR] - Comando invalido, tente novamente ($_$)')
			t.sleep(2)
			print('\n')
			break
	else:
		print('\n\t[ERROR] - Codigo invalido :~( RESFRIADO')
	return (lista,moeda,varejo)

#____Gaste aqui seu suado dinheiro____
def compras():
	global doit,braga, itemUnidade,itemKilo, itemPeca
	print('''
	****BEM VINDO***

	realize aqui suas compras

	[1]. Mercado de Joias
	[2]. Mercado de Veiculos
	[3]. Mercado de Alimentação
	[4]. Mercado de Pecas de veiculos

	''')
	mercado = input('\t ~> ')
	mercado = floatConversor(mercado)
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
		print('\n\t[ERROR] - Mercado inexistente! :-/ ')
	return (braga,doit)


#______Sistema de fuga_______________

def fugir():
	global itemPeca, falha, metodoFuga, vida

	print('''
	****BEM VINDO***

	Escolha um modo de fuga :
''')
	i = 1
	for k,v in metodoFuga:
		print(f'\t[{i}]. {k}\t( {v} pecas )')
		i += 1

	num  = input('\n\t ~> ')
	num  = floatConversor(num)
	if num == 1:
		global pecas1
		itemPeca, falha, vida = tentativaFuga(itemPeca,pecas1,9,metodoFuga[0])
	elif num == 2:
		global pecas2
		itemPeca, falha, vida = tentativaFuga(itemPeca,pecas2,7,metodoFuga[1])
	elif num == 3:
		global pecas3
		itemPeca, falha, vida = tentativaFuga(itemPeca,pecas3,5,metodoFuga[2])
	elif num == 4:
		global pecas4
		itemPeca, falha, vida = tentativaFuga(itemPeca,pecas4,3,metodoFuga[3])
	else:
		print('\n\t[ERROR] - Modo de fuga inexistente!')

	return itemPeca

def tentativaFuga(pecasM, pecasN, taxa,metodo):
	global falha, dias, vida, itemUnidade
	nomesPm = [nome for nome in pecasM]
	nomesPn = [nome for nome,valor in pecasN]
	conta = sum(1 for c in nomesPm if c in nomesPn)
	numPecas = len(nomesPn)
	favItens = len(itemUnidade)

	if dias % 2 == 0 and (metodo[1] == 5 or metodo[1] == 7):
		favoravel = 5
		# + 5 % planador, balao
	elif dias % 2 != 0 and (metodo[1] == 3 or metodo[1] == 9):
		favoravel = 5
		# + 5 % jangada, navio
	else:
		favoravel = 0
	print(f'''
	Metodo de fuga : {metodo[0]}
	Taxa de sucesso inicial : {round(1/taxa*100,2)} %
	Acrescimo do dia : + {favoravel} %
	Acrescimo Itens : + {favItens} %
	Numero de pecas necessarias : {metodo[1]}

	Pecas necessarias,segue abaixo...
''')
	for nome in nomesPn:
		print('\t1 x ',nome)

	opc = input('\n\tDeseja continuar ? (sim / nao) : ')

	if SIM.count(opc) == 1:
		if conta == numPecas:
			carregamento()
			# TENTANDO BASEADO NA TAXA DE SUCESSO DO MEIO DE TRANSPORTE
			chanceFuga = round(1 / taxa  * 100,2) + favoravel + favItens
			indice = rand(100) + 1
			if indice > chanceFuga:
				print('\n\t\tFUGA MAU SUCEDIDA\n\tVoce perdeu 2 pontos de vida e as pecas do seu meio de transporte [~.~]')
				for nome in nomesPn:
					if pecasM[nome] > 1:
						pecasM[nome] -= 1
					else:
						pecasM.pop(nome)
				falha += 1
				vida -= 2
				print('\n\t- 2 VIDAS')
				return (pecasM, falha, vida)
			else:
				print('\n\t\tFUGA BEM SUCEDIDA !!!\n\tNos nao desistimos (*_*)...|_| UM BRINDE\n')
				status()
		else:
			print('\nQuantidade de pecas insuficiente para uma fuga')
	elif NAO.count(opc) == 1:
		print('\n\tTentativa cancelada, seu fraco\n\tCom certeza se tremeu de medo :-O ')
	else:
		print('\n\t[ERROR] - Comando invalido, tente novamente (0.0) ')

	return (pecasM, falha, vida)

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
					print('\n\t+ 1 VIDA')
			else:
				if vida < 10:
					vida += 1
					print('\n\t+ 1 VIDA')
				itemKilo.pop(ultA)
	else:
		if vida > 1:
			vida -= 1
			print('\n\t- 1 VIDA')
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

def status():
	print(f'''
     _____________________________
     |
     |   Nome : {usuario}
     |   Dias : {dias}
     |   Vida : {vida}
     |
     |   Doits : {doit}
     |   Braga : {braga}
     |
     |   N* de Tentativas : {falha}
     |
     |____________________________
''')
	exit()
