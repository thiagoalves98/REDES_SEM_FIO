# -*- coding: utf-8 -*-
#!/usr/bin/python3

from random import randint

class Controle(object):

	def __init__(self):
		self._listaAcesso 	= []		#Lista com as referências dos objetos que querem acessar 
		self._listaTempo	= []		#Lista com o tempo de espera de cada Nó que entra na fila de acesso

	def SolicitaAcesso(self, No):

		self._listaAcesso.append(No)
		self._listaTempo.append(0)

	def Libera_Acesso(self, n):

		_len = len(self._listaAcesso)

		#Verifica se alguem esta esperando à mais de 10T. Se sim, libera o acesso. Se não, acesso aleatório
		for i in range(_len):
			if(self._listaTempo[i] > 10):
				n = i
			else:
				n = randint(0, _len-1)
				
		#Libera o acesso do Nó n
		self._listaAcesso[n]._flagAcesso = True
		self._listaAcesso[n].Acesso()

		#Bloqueia o acesso do Nó n e remove ele da fila de espera
		self._listaAcesso[n]._flagAcesso = False
		self._listaAcesso.pop(n)
		self._listaTempo.pop(n)

		#Incrementa 1T no tempo de espera dos Nós na fila
		for i in range(len(self._listaAcesso)):
			self._listaTempo[i] +=1

	
