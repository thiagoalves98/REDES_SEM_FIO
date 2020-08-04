# -*- coding: utf-8 -*-
#!/usr/bin/python3


from no import no
from Grafo import Grafo
from Controle import Controle
import string

#Cria um objeto controle
c = Controle()

def Configura_Rede(n, Alcance):

	nos = []
	IDs	= []

	#Array com as 26 letras do alfabeto
	letras = list(string.ascii_lowercase)

	#Cria um objeto Grafo
	g = Grafo()
	
	#Cria N objetos nó
	for i in range(n):
		nos.append(no(letras[i], Alcance, g, c))
		IDs.append(letras[i])

	#Preenche o grafo com referencias dos nós
	MatrizAdj = g.Gera_MatrizAdj(n, nos, Alcance, IDs)

	#Preeche o controle com referencias dos nós
	#Referencia = c.Cria_Controle(n, nos)

	return nos, MatrizAdj

def EnviaMensagem(nos, Origem, Destino, mensagem):

	letras = list(string.ascii_lowercase)

	indice = 0

	for i in range(len(letras)):
		if(Origem == letras[i]):
			indice = i

	nos[indice].EnviaMensagem(Destino, mensagem)

	_len = len(c._listaAcesso)
	
	while(_len > 0):
		arquivo = open('Script.txt', 'a')

		arquivo.writelines("\n"+'T'+str(i)+":\n")

		arquivo.close()

		i+=1

		c.Libera_Acesso(0)

		_len = len(c._listaAcesso)

def DescobreVizinhos(nNos, nos):

	for i in range(nNos):
		nos[i].Hello()

	_len = len(c._listaAcesso)
	
	while(_len > 0):
		arquivo = open('Script.txt', 'a')

		arquivo.writelines("\n"+'T'+str(i)+":\n")

		arquivo.close()

		i+=1

		c.Libera_Acesso(0)

		_len = len(c._listaAcesso)

def AtualizaRotas(nNos, nos):

	########################################################### Atualiza as rotas atuais de cada Nó

	for i in range(nNos):
		arquivo = open('Script.txt', 'a')

		arquivo.writelines("\n"+"MAC: "+str(nos[i]._MAC)+" "+str(nos[i]._Camada_Rede.TabelaRotas)+"\n")

		arquivo.close()

def main():

	#nNos = 5
	nNos = input("nNos	 :	")
	#Alcance = 500
	Alcance = input("Alcance:	")

	#Matriz de Adjacência
	MatrizAdj = []

	#Cria uma rede com N roteadores de alcance X
	nos, MatrizAdj = Configura_Rede(nNos, Alcance)

	#Reseta o Script da simulação anterior
	arquivo = open('Script.txt', 'w')
	arquivo.close()

	AtualizaRotas(nNos, nos)

	DescobreVizinhos(nNos, nos)

	AtualizaRotas(nNos, nos)

	while(True):

		Origem 	= raw_input("Origem	 :	")
		Destino = raw_input("Destino : 	")
		Msg		= raw_input("Mensagem: 	")

		EnviaMensagem(nos, Origem, Destino, Msg)

		AtualizaRotas(nNos, nos)

if __name__=="__main__":
	main()