# -*- coding: utf-8 -*-
#!/usr/bin/python3


from Camada_Rede   import Camada_Rede
from Pacote		   import Pacote
from copy import copy

class no(object):

	def __init__(self, MAC, Alcance, Grafo, Controle):

		self._MAC 			= MAC
		self._Camada_Rede 	= Camada_Rede(Grafo, MAC, self, Controle)
		self._bufferMsg		= []

	def EnviaMensagem(self, Destino, Mensagem):

		nBytesMensagem = len(Mensagem) * 4

		nPacotes = int(nBytesMensagem / 32)

		i = 0
		j = 8

		round(nPacotes + 0,5)

		while(nPacotes >= 0):

			frame = Mensagem[i:j]

			if(nPacotes == 0):
				Pac = Pacote(self._MAC, Destino, frame, True)
			else:
				Pac = Pacote(self._MAC, Destino, frame, False)

			self._Camada_Rede.Envia_Dados(Pac)

			nPacotes += -1

			i = j
			j += 8

	def RecebeMensagem(self, Pacote, Origem, Rota):

		Dados 	= Pacote.GetDados(self, self._MAC)
		flag	= Pacote.GetFlag(self)

		#Guarda o frame
		self._bufferMsg.append(Dados)

		if(flag == True):

			Mensagem = [''.join(self._bufferMsg)]

			print(" ")

			print("MAC :", self._MAC, "| Mensagem recebida de ", Origem, "Mensagem:", Mensagem)

			print("Rota do pacote", Rota)

			print(" ")

			del self._bufferMsg[:]

	def Hello(self):

		self._Camada_Rede.Envia_Hello()

	def GetMAC(self):

		return self._MAC

