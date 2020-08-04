# -*- coding: utf-8 -*-
#!/usr/bin/python3


from Camada_Fisica import Camada_Fisica

class Camada_Enlace(object):

	def __init__(self, Grafo, MAC, Camada_Rede, Controle):

		self._Camada_Rede 	= Camada_Rede
		self._Camada_Fisica	= Camada_Fisica(Grafo, MAC, self)
		self._Controle		= Controle	
		self._flagAcesso 	= False
		self._BufferPac		= []
		self._MAC			= MAC

	def Envia_Pacote(self, Pacote):

		#Envia para a camada fisica
		self._Camada_Fisica.Envia_Pacote(Pacote)

	def Recebe_Pacote(self, Pacote):
		
		#Envia para a camada de rede
		self._Camada_Rede.Processa_Pacote(Pacote)

	def Processa_Envio(self,Pacote):

		#Armazena pacote no buffer
		self._BufferPac.append(Pacote)

		#Avisa para o Controle que quer acessar
		self._Controle.SolicitaAcesso(self)

	def Acesso(self):

		if(self._flagAcesso == False):
			print("MAC:",self._MAC,"nao pode acessar no momento")
			return 0

		else:
			#print("MAC:",self._MAC,"acesso liberado")

			#Obtem o primeiro pacote do buffer
			Pacote = self._BufferPac[0]

			#Remove ele do buffer
			self._BufferPac.pop(0)

			#Recebe o pacte
			self.Envia_Pacote(Pacote)

	


