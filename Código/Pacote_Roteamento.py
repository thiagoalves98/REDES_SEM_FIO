# -*- coding: utf-8 -*-
#!/usr/bin/python3


class Pacote_Roteamento(object):

	def __init__(self, Origem, Destino, NextStep, nSeq, tipo, Dados):
		self.Origem 	= Origem
		self.NextStep	= NextStep
		self.Destino 	= Destino
		self.nSeq		= nSeq
		self.tipo		= tipo
		self.Dados		= Dados
		self.nSaltos	= 1

	def GetOrigem(self):

		return self.Origem

	def GetDestino(self):

		return self.Destino

	def GetNext(self):

		return self.NextStep

	def GetDados(self):

		return self.Dados

	def GetnSequencia(self):

		return self.nSeq

	def GetTipo(self):

		return self.tipo

	def GetnSaltos(self):

		return self.nSaltos

	def IncrementaSalto(self):

		self.nSaltos += 1

	def SetNextStep(self, MAC):

		self.NextStep = MAC

	def SetDado(self, Dados):

		self.Dados.append(Dados)

	def Set(self, Dados):

		self.Dados = Dados

	





