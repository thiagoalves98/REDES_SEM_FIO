# -*- coding: utf-8 -*-
#!/usr/bin/python3


class Camada_Fisica(object):

	def __init__(self, Grafo, MAC, Camada_Enlace):
		self._Grafo 			= Grafo 				#Referência ao objeto da classe Grafo 	<class Grafo>
		self._MAC				= MAC 					#MAC do Nó								<str>
		self._Camada_Enlace 	= Camada_Enlace 		#Referência a camada de enlace 			<class Camada_Enlace>

	def Envia_Pacote(self, Pacote):

		#Verifica no grafo os vizinhos alcançaveis
		listaObj = self._Grafo.Obtem_Vizinhos(self._MAC)

		#Envia o pacote para todos os vizinhos(Broadcast)
		for i in range(len(listaObj)):

			listaObj[i]._Camada_Rede.Camada_Enlace._Camada_Fisica.Recebe_Pacote(Pacote)

	def Recebe_Pacote(self, Pacote):

		#Envia o pacote para a camada de enlace
		self._Camada_Enlace.Recebe_Pacote(Pacote)

	
	

