# -*- coding: utf-8 -*-
#!/usr/bin/python3


import numpy
import random
import networkx as nx
import matplotlib.pyplot as plt

class Grafo(object):

	def __init__(self):
		self._MatrizAdj		= []					#Matriz de adjacência com as distancias			<numpy>
		self._nos			= []					#Lista com os objetos da classe Nós 			<class nó>
		self._Alcance		= 0 					#Alcance de um Nós 								<int>
		self._IDs			= ''					#Identificador de cada objetos 					<str>

	def Gera_MatrizAdj(self, n, Objetos, Alcance, IDs):

		#Cria uma matriz de zeros com tamanho n x n
		MatrizAdj = numpy.zeros(shape=(n,n))

		#Preenche a matriz simetrica de forma aleatória
		for i in range(n):
			for j in range(n):
				if(i == j):
					continue
				else:
					distancia = int(100 + (random.random() * 899))
					MatrizAdj[i][j] = distancia
					MatrizAdj[j][i] = distancia
			
		#Matriz teste
		MatrizAdj = numpy.array([[000.0, 500.0, 000.0, 000.0, 000.0], [500.0, 000.0, 500.0, 500.0, 000.0], [000.0, 500.0, 000.0, 000.0, 000.0], [000.0, 500.0, 000.0, 000.0, 500.0], [000.0, 000.0, 000.0, 500.0, 000.0]])
		
		#Salva as variáveis na classe
		self._MatrizAdj = MatrizAdj
		self._nos 		= Objetos
		self._Alcance 	= Alcance
		self._IDs		= IDs

		self.Gera_Arquivo(n, MatrizAdj)

		self.Exibe_Grafo(n, MatrizAdj, IDs, Alcance)
	
		return MatrizAdj

	def Gera_Arquivo(self, n, MatrizAdj):
		
		#Cria um arquivo
		arquivo = open('MatrizAdj.txt', 'w')

		#Percorre a MatrizAdj e preenche o arquivo
		for i in range(n):
			for j in range(n):
				if(i == j):
					arquivo.write('000.0' +'		')
				else:
					arquivo.write(str(MatrizAdj[i][j]) +'		')

			arquivo.write('\n')

		arquivo.close()

	def Exibe_Grafo(self, n, MatrizAdj, IDs, Alcance):
		#n = numero de Nós <int>
		#MatrizAdj = 
		#IDs = MAC de cada nó <str>
		#Alcance = alcance de cada nó <int>
		
		#Cria um objeto nx
		Grafo 	= nx.Graph()
		Arestas = {}

		#Cria os Nós
		for i in range(n):
			Grafo.add_node(IDs[i])

		#Cria as Arestas
		for i in range(n):
			for j in range(n):
				if(MatrizAdj[i][j] > 0) and (MatrizAdj[i][j] <= Alcance):
					
					Grafo.add_edge(IDs[i], IDs[j])
					par = (IDs[i], IDs[j])
					x = {par : MatrizAdj[i][j]}
					Arestas.update(x)

		#Cria draw
		graph_pos=nx.shell_layout(Grafo)
		nx.draw_networkx_nodes(Grafo,graph_pos)
		nx.draw_networkx_edges(Grafo,graph_pos)
		nx.draw_networkx_labels(Grafo, graph_pos)
		nx.draw_networkx_edge_labels(Grafo, graph_pos, edge_labels = Arestas)
		
		#Exibe Grafo
		plt.show()

	def Obtem_Vizinhos(self, MAC):

		try:
			n = self._IDs.index(MAC)

		except ValueError:
			print("O MAC nao foi encontrado na lista")
			return -1

		else:
			#Lista de referencia aos objetos vizinhos
			listaObj = []

			for i in range(len(self._IDs)):

				#Se 0 < d <= Alcance, é meu vizinho
				if(self._MatrizAdj[n][i] > 0) and (self._MatrizAdj[n][i] <= self._Alcance):

					listaObj.append(self._nos[i])

			return listaObj

	

