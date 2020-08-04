# -*- coding: utf-8 -*-
#!/usr/bin/python3


class Pacote(object):

	def __init__(self, Origem, Destino, Mensagem, flag):
		self._MACOrigem		= Origem
		self._MACDestino	= Destino
		self._Dados			= Mensagem
		self._Next			= ''
		self._nSequencia	= ''
		self._Rota			= []
		self._flag			= flag

	def GetOrigem(self, Camada):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			return self._MACOrigem
		else:
			return ''

	def GetDestino(self, Camada):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			return self._MACDestino
		else:
			return ''

	def GetDados(self, Camada, MAC):
		
		tipo = str(type(Camada))

		if(tipo == "<class 'no.no'>") and (MAC == self._MACDestino):
			return self._Dados
		else:
			return ''

	def GetNext(self, Camada):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			return self._Next
		else:
			return ''

	def GetnSequencia(self, Camada):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			return self._nSequencia
		else:
			return ''

	def SetNextStep(self, Camada, Next):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			self._Next	= Next
		
	def SetnSequencia(self, Camada, nSequencia):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			self._nSequencia = nSequencia

	def SetRota(self, Camada, Passo):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			self._Rota.append(Passo)

	def GetRota(self, Camada):

		tipo = str(type(Camada))

		if(tipo == "<class 'Camada_Rede.Camada_Rede'>"):
			return self._Rota
		else:
			return ''

	def GetFlag(self, Camada):

		tipo = str(type(Camada))

		if(tipo == "<class 'no.no'>"):
			return self._flag
		else:
			return ''

	