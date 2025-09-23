#Banco de dados ilha_capital
import time as t
import os
from bugs_ilha import *
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

braga = 0
doit = 0
itemKilo = {}
itemUnidade = {}
itemPeca = []
vida = 5
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
('Repolho', 6.8),
('Cenoura',8.3),
('Tomate', 5.9),
('Bagaço de coco', 20.2),
('Limão', 7.3)
]

pecas = [
	['Mastro P','Paubique','Toras'], # jangada
	['Vela','Quilha','Trapezio','Cordas de controle','Estrutura de sustentacao'],  # Asa delta
	['Envoltorio','Cesto','Queimador','Tanque de propano','Cordas de suspensao','Valvula de parachute','altimetro'], # balao
	['Casco','Proa','Popa','Conves','Leme','Helice','Mastro G','Ancora','Ponte de comando'], # navio
]

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
			print('\n[ERROR]')
		return total
	except:
		return print('Não é um número')


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
				print('\n\tERROR!!! Você perdeu',premio,'D$\n\tRESPOSTA: ',valor1+valor2,'\n')
		print("---- Balanço final : %.2f D$ ----\n" %(soma))
		doit += soma
		print('\nFIM DA PARTIDA\n')
	except:
		print('\nAlgo de errado não está certo...\nSeu saldo não foi afetado\n')
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
			print('\n\tERROR!! Você perdeu',premio,'B$\n\tRESPOSTA:', local,'\n')
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
	\nDigite que tipo de conversão deseja:
	1 - De Doits para Bragas
	2 - De Bragas para Doits
	''')
	num = input(' ~> ')
	try:
		num = floatConversor(num)
		if num == 1:
			d = input('Quantidade de Doits para converter?\n ~> ')
			d = floatConversor(d)

			if d > doit:
				print('\nVocê não tem tudo isso, meu caro ^_^')
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
				print('\nVocê não tem tudo isso, meu caro ^_^')
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
		print('\n[ERROR] - Não é um número \(0_0)/ ')
	return (braga,doit)

#Suporte da funcao compras()
def transacao(lista,moeda,varejo):
	global SIM,NAO
	lista.sort()

	while True:
		i = 1
		clear()
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
		quantidade = input('\nQuantidade desse produto(unidade/kilo)\n ~> ')
		try:
			if len(lista) == len(alimento):
				quantidade = floatConversor(quantidade)
			else:
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
					print('\tVocê não tem saldo suficiente :(')
			elif NAO.count(confirmar) == 1:
				print('\tCompra cancelada, tente de novo\n\tnosso produtos são da melhor qualidade :D')
			else:
				print('\t[ERROR] - Comando invalido, tente novamente')
			t.sleep(2)
			print('\n')
			break
	return (lista,moeda, varejo)

#____Gaste aqui seu suado dinheiro____
def compras():
	global doit,braga, itemUnidade,itemKilo
	print('''
	****BEM VINDO***

	realize aqui suas compras

	1.Mercado de joias e pedras
	2.Mercado de veiculos
	3.Mercado de alimentação

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
	else:
		print('\n[ERROR] - Mercado inexistente!')
	return (braga,doit)

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
			exit()
	return vida


#  lista   | 0 | 0 |  3  |  2  |  1  |  1  |  1  |  1  |  1  |
#  comida  | 0 | 0 | 0.5 | 0.5 | 2.5 | 2.0 | 1.5 | 1.0 | 0.5 |
#  vida    | 5 | 4 |  5  |  6  |  7  |  8  |  9  |  10 | 10  |


def encerramento():
	print('\n\tObrigado pela atenção...\nEssa área está passando por ajustes... lol\n')
	exit()
