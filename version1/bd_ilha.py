#Banco de dados ilha_capital
import time as t
import os
from bugs_ilha import *
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

braga = 0
doit = 0
item = {}

nome = [
'Maria',
'José',
'Antonio',
'Joao',
'Ana',
'Luiz',
'Paulo',
'Carlos',
'Manoel',
'Pedro',
'Francisca',
'Frascisco',
'Marcos',
'Raimundo',
'Sebastiao',
'Antonio',
'Marcel',
'Jorge',
'Geraldo',
'Adriana',
'Sandra',
'Luis',
'Fernando',
'Fabio',
'Roberto',
'Marcio',
'Edson',
'Andre',
'Sergio',
'Josefa',
'Patricia',
'Daniel',
'Rodrigo',
'Rafael',
'Joaquim',
'Vera',
'Ricardo',
'Eduardo',
'Terezinha',
'Sonia',
'Alexandre',
'Rita',
'Luciana',
'Claudio',
'Rosa',
'Benedito',
'Leandro',
'Manoela',
'Alice',
'Raimunda',
'Mario',
'Vitor',
'Iago',
'Matias',
'Amanda',
'Elias'
]

#Compras e vendas somente com doits
joia = [
('Anel de pirata',15.5),
('Anel dragão',27.9),
('Peça de Diamante',740.0),
('Peça de Ouro',640.0),
('Peça de Prata',520.0),
('Peça de Bronze',488.0),
('Peça de Cobre',120.0),
('Brinco estrela',16.9),
('Brinco lua',15.3),
('Colar de peixe',12.3),
('Estatua de sereia',90.8),
('Pingente Ouro branco',120.87),
('Pulseira de Ouro',54.4),
('Pulseira de Prata',46.2),
('Aliança de Ouro',48.4),
('Aliança de Prata',37.2)
]

#def maiuscula(frase):
#	novaPalavra = " "
#	frase = frase.split(" ")
#	for palavra in frase:
#		novaPalavra = novaPalavra + palavra.capitalize() + ' '
#	return novaPalavra

def limpar(seg):
	print('\n\t...limpando tela...')
	t.sleep(seg)
	clear()

def ganharDoits():
	
	global doit
	premio, soma = 0,0
	print('\n\tResponda aos calculos e ganhe Doits!!!\n')
	for num in range(5):
		valor1 = rand(15) + 1
		valor2 = rand(15) + 1
		print(valor1,'+',valor2)
		valor = int(input(' ~> '))
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
	return doit

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
		elif nomeX == '@':
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

def conversao():
	global doit, braga
	msm = '''
\t***Conversão realizada***
\n\nGraças ao nosso sistema de deposito
imediato o valor convetido já se
encotra disponivél para uso. Bom proveito\n
'''
	
	print('''
	Sabendo que:
	1 D$ = 1.6 B$
	1 B$ = 0.625 D$
	\nDigite que tipo de conversão deseja:
	1 - De Doits para Bragas
	2 - De Bragas para Doits
	''')
	num = int(input(' ~> '))
	if num == 1:
		d = int(input('Quantidade de Doits para converter? '))
		if d > doit:
			print('\nVocê não tem tudo isso, meu caro ^_^')
		else:
			convertido = d*1.6
			doit -= d
			braga += convertido
			
			print('%.2f D$ = %.2f B$' %(d,d*1.6))
			print('\n\tProcessando solicitação...')
			t.sleep(2)
			print(msm)
			
	elif num == 2:
		b = int(input('Quantidade de Bragas para converter? '))
		if b > braga:
			print('\nVocê não tem tudo isso, meu caro ^_^')
		else:
			convertido = b*0.625
			braga -= b
			doit += convertido
			
			print('%.2f B$ = %.2f D$' %(b,b*0.625))
			print('\n\tProcessando solicitação...')
			t.sleep(2)
			
			print(msm)
	else:
		print('\nTODO ERRADO\n')
	return (braga,doit)

def transacao(lista,moeda):

	lista.sort()
	i = 1
	for (item,valor) in lista:
		print(' ',i,'.',item,' = ',valor,'D$')
		i += 1
	print('\n***Insira 0 para encerrar as compras\n')
	while True:
		produto = int(input('Insira o número do produto: '))
		if produto == 0:
			print('\t<3 Volte sempre <3\n')
			t.sleep(2)
			break
		quantidade = int(input('\nQuantidade desse produto: '))
		subtotal = lista[produto-1][1] * quantidade
		print('\n',lista[produto-1][0],'.....',quantidade,' = ',subtotal,'D$\n')
		while True:
			confirmar = input('Confirme a compra com sim ou nao : ')
			print('\n')
			if confirmar == 'sim':
				if moeda >= subtotal:
					moeda -= subtotal
					print('\tCompra concluída $$')
				else:
					print('\tVocê não tem saldo suficiente :(')
			elif confirmar == 'nao':
				print('\tCompra cancelada, tente de novo\n\tnosso produtos são da melhor qualidade :D')
							
			else:
				print('\tComando inválido, tente novamente')
			t.sleep(2)
			print('\n')
			break
	return moeda

def compras():
	global doit,braga
	print('''
	****BEM VINDO***
	realize aqui suas compras
	
	1.Mercado de joias e pedras
	2.Mercado de veiculos
	3.Mercado de alimentação
	
	''')
	mercado = int(input('\t ~> '))
	if mercado == 1:
		global joia
		doit = transacao(joia,doit)
	elif mercado == 2:
		print('\nEm produção...')
		exit()
		global veiculo
		doit = transacao(veiculo,doit)
	elif mercado == 3:
		print('\nEm produção...')
		exit()
		global alimento
		braga = transacao(alimento,braga)
	else:
		print('\nMercado inexistente!')
	return (braga,doit)

def encerramento():
	print('\n\tObrigado pela atenção...\nEssa área está passando por ajustes... lol\n')
	exit()
