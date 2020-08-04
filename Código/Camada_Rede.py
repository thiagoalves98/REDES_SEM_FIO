# -*- coding: utf-8 -*-
#!/usr/bin/python3


from Camada_Enlace import Camada_Enlace
from Pacote_Roteamento import Pacote_Roteamento
import random
import copy

def Mensagem(Tipo, Msg1, Msg2):

	if(Tipo == 10):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Dados) Preparando pacote de dados. Destino = "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 11):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Dados) Nenhuma rota encontrada para "+str(Msg2)+". Enviando Route Request!\n"
		Script(Msg)
	elif(Tipo == 12):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Dados) Rota encontrada. Next_step = "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 20):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Request) Solicitando rota para "+str(Msg2)+". Enviando RRequest\n"
		Script(Msg)
	elif(Tipo == 50):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Request) Pacote de request recebido. Origem = "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 51):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Request) Pacote descartado (nSeq)\n"
		Script(Msg)
	elif(Tipo == 52):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Request) Enviando Reply\n"
		Script(Msg)
	elif(Tipo == 53):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Request) Repassando pacote\n"
		Script(Msg)
	elif(Tipo == 60):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Reply) Enviando Reply para "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 61):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Reply) Nenhuma rota encontrada para "+str(Msg2)+". Enviando Route Request!\n"
		Script(Msg)
	elif(Tipo == 62):
		Msg = "\nMAC: "+str(Msg1)+"| (Envia_Reply) Rota encontrada. Next_step = "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 70):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Reply) Pacote Reply com destino para "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 71):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Reply) Pacote descartado (nSeq)\n"
		Script(Msg)
	elif(Tipo == 72):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Reply) Pacote recebido\n"
		Script(Msg)
	elif(Tipo == 73):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Reply) Encaminhando pacote para"+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 80):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Dados) Pacote de Dados recebido com destino para "+str(Msg2)+"\n"
		Script(Msg)
	elif(Tipo == 81):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Dados) Pacote Descartado\n"
		Script(Msg)
	elif(Tipo == 82):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Dados) Pacote de dados recebido\n"
		Script(Msg)
	elif(Tipo == 83):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Dados) Nenhuma rota encontrada para "+str(Msg2)+". Enviando Route Request!\n"
		Script(Msg)
	elif(Tipo == 84):
		Msg = "\nMAC: "+str(Msg1)+"| (Recebe_Dados) Rota encontrada. Next_step = "+str(Msg2)+"\n"
		Script(Msg)

def Script(mensagem):
	arquivo = open('Script.txt', 'a')

	arquivo.write(mensagem)

	arquivo.close

class Camada_Rede(object):

	def __init__(self, Grafo, MAC, no, Controle):
		self.MAC			= MAC
		self.Camada_Enlace 	= Camada_Enlace(Grafo, MAC, self, Controle)
		self.no 			= no
		self.TabelaRotas	= []
		self.nSeq			= []
		self.buffer			= []

	def Envia_Dados(self, Pac):

		Pacote = copy.deepcopy(Pac)

		self.LimpaTabela()

		#Obtem dados do pacote
		Origem 	= Pacote.GetOrigem(self)
		Destino = Pacote.GetDestino(self)
		
		#Escreve no Log
		Mensagem(10, self.MAC, Destino)

		#Descobre o Next
		Next 	= self.Next_Step(Destino)

		if(Next == 0):

			#Escreve no Log
			Mensagem(11, self.MAC, Destino)
			
			#Guarda o pacote
			self.buffer.append(Pacote)

			#Envia Request
			self.Envia_Request(Destino)
			
		else:

			#Escreve no Log
			Mensagem(12, self.MAC, Next)
			
			#Cria um numero de sequência
			nSeq = str(self.MAC)+str(random.random())
			self.nSeq.append(nSeq)

			#Seta o número de sequência no pacote
			Pacote.SetnSequencia(self, nSeq)

			#Seta o proximo passo do pacote
			Pacote.SetNextStep(self, Next)

			#Seta um passo
			Pacote.SetRota(self, self.MAC)

			#Envia para o enlace
			self.Envia_Pacote(Pacote)

	def Envia_Request(self, Destino):

		#Escreve mensagem no Log
		Mensagem(20, self.MAC, Destino)

		#Cria um número de sequência
		nSeq = str(self.MAC)+str(random.random())
		self.nSeq.append(nSeq)

		#Dados
		Dados = []

		#Cria um pacote request
		Pacote_RReq = Pacote_Roteamento(self.MAC, Destino, 0, nSeq, "RReq", Dados)

		#Set um passo no pacote
		Pacote_RReq.SetDado(self.MAC)

		#Envia para o enlace
		self.Envia_Pacote(Pacote_RReq)

	def Envia_Pacote(self, Pacote):

		#Envia o pacote para a camada de enlace
		self.Camada_Enlace.Processa_Envio(Pacote)

	def Processa_Pacote(self, Pacote):

		tipo = str(type(Pacote))

		if(tipo == "<class 'Pacote_Roteamento.Pacote_Roteamento'>"):

			tipo = Pacote.GetTipo()

			if(tipo == 'Hello'):
				self.Recebe_Hello(Pacote)
			if(tipo == 'RReq'):
				self.Recebe_Request(Pacote)
			if(tipo == 'RRep'):
				self.Recebe_Reply(Pacote)
		
		elif(tipo == "<class 'Pacote.Pacote'>"):

			self.Recebe_Dados(Pacote)

		else:

			print("Pacote nao reconhecido")

	def Recebe_Request(self, PacReq):

		Pacote_RReq = copy.deepcopy(PacReq)

		#Obtem dados do pacote
		Origem 	= Pacote_RReq.GetOrigem()
		Destino = Pacote_RReq.GetDestino()

		#Escreve mensagem no Log
		Mensagem(50, self.MAC, Origem)

		#Obtem o nSeq do pacote
		nSeq = Pacote_RReq.GetnSequencia()

		#Descarta o pacote caso o nSeq já esteja na lista
		if nSeq in self.nSeq:
			Mensagem(51, self.MAC, 0)

		else:

			#Set um passo no pacote
			Pacote_RReq.SetDado(self.MAC)

			#Guarda o número de sequência
			self.nSeq.append(nSeq)

			#Envia Reply caso seja o destino do request
			if(Destino == self.MAC):

				#Escreve mensagem no Log
				Mensagem(52, self.MAC, 0)

				#Obtem os dados do pacote
				Dados = Pacote_RReq.GetDados()

				#Envia um pacote Reply
				self.Envia_Reply(Origem, Dados)

			#Repassa o pacote
			else:

				#Escreve mensagem no Log
				Mensagem(53, self.MAC, 0)

				#Envia para o enlace
				self.Envia_Pacote(Pacote_RReq)
	
	def Envia_Reply(self, Destino, Rota):

		#Escreve mensagem no Log
		Mensagem(60, self.MAC, Destino)
	
		#Cria um número de sequência
		nSeq = str(self.MAC)+str(random.random())
		self.nSeq.append(nSeq)

		#Inverte o caminho
		Rota.reverse()

		#Pega o segundo passo da lista invertida
		Next = Rota[1]

		#Cria um pacote Reply
		Pacote_RRep = Pacote_Roteamento(self.MAC, Destino, Next, nSeq, "RRep", Rota)

		#Envia o pacote para o enlace
		self.Envia_Pacote(Pacote_RRep)

	def Recebe_Reply(self, PacResp):

		Pacote_RRep = copy.deepcopy(PacResp)
		
		#Obtem dados do pacote
		Origem 	= Pacote_RRep.GetOrigem()
		Destino = Pacote_RRep.GetDestino()
		Next 	= Pacote_RRep.GetNext()
		Saltos	= Pacote_RRep.GetnSaltos()
		nSeq 	= Pacote_RRep.GetnSequencia()
		Dados 	= Pacote_RRep.GetDados()

		#Escreve mensagem no Log
		Mensagem(70, self.MAC, Destino)
		
		#Descarta o pacote caso o nSeq já esteja na lista
		if nSeq in self.nSeq:
			Mensagem(71, self.MAC, 0)

		#Recebe o pacote caso seja o destino
		elif(Destino == self.MAC):

			#Escreve mensagem no Log
			Mensagem(72, self.MAC, 0)

			#Guarda o número de sequência
			self.nSeq.append(nSeq)

			#Formata a rota
			Rota = self.FormataRota(Origem, Dados[Saltos-1], Saltos)

			#Aprende a rota
			self.TabelaRotas.append(Rota)

			#Libera o pacote
			self.LiberaBuffer(Origem)

		#Encaminha o pacote caso seja o next step
		elif(Next == self.MAC):

			#Descobre o próximo passo
			Next = Dados[Saltos+1]

			#Escreve mensagem no Log
			Mensagem(73, self.MAC, Next)

			#Formata a rota
			Rota = self.FormataRota(Origem, Dados[Saltos-1], Saltos)

			#Aprende a rota
			self.TabelaRotas.append(Rota)

			#Guarda o número de sequência
			self.nSeq.append(nSeq)

			#Define o próximo passo do pacote
			Pacote_RRep.SetNextStep(Next)

			#Incrementa um salto no pacote
			Pacote_RRep.IncrementaSalto()

			#Envia para o enlace
			self.Envia_Pacote(Pacote_RRep)

		else:

			#Escreve mensagem no Log
			Mensagem(71, self.MAC, 0)

	def Recebe_Dados(self, PacDados):

		Pacote = copy.deepcopy(PacDados)

		#Obtem dados do pacote
		Origem 	= Pacote.GetOrigem(self)
		Destino = Pacote.GetDestino(self)
		nSeq 	= Pacote.GetnSequencia(self)
		Next 	= Pacote.GetNext(self)

		#Escreve mensagem no Log
		Mensagem(80, self.MAC, Destino)

		#Descarta pacote repitido
		if nSeq in self.nSeq:

			#Escreve mensagem no Log
			Mensagem(81, self.MAC, 0)

		#Recebe o pacote caso seja o destino
		elif(Destino == self.MAC):

			#Seta Passo
			Pacote.SetRota(self, self.MAC)

			#Escreve mensagem no Log
			Mensagem(82, self.MAC, 0)

			#Guarda o número de sequência
			self.nSeq.append(nSeq)

			Rota = Pacote.GetRota(self)

			#Envia o pacote para o Nó
			self.no.RecebeMensagem(Pacote, Origem, Rota)

		#Encaminha o pacote caso seja o next step
		elif(Next == self.MAC):

			#Encontra o próximo passo
			Next = self.Next_Step(Destino)

			if(Next == 0):

				#Escreve mensagem no Log
				Mensagem(83, self.MAC, Destino)

				#Guarda o pacote no buffer
				self.buffer.append(Pacote)

				#Envia Route Request
				self.Envia_Request(Destino)

			else:

				#Seta Passo
				Pacote.SetRota(self, self.MAC)

				#Escreve mensagem no Log
				Mensagem(84, self.MAC, Next)

				#Guarda o nSeq
				self.nSeq.append(nSeq)

				#Define o próximo passo
				Pacote.SetNextStep(self, Next)

				#Envia para o enlace
				self.Envia_Pacote(Pacote)
		
		#Descarta o pacote caso não seja o next step
		else:

			#Escreve mensagem no Log
			Mensagem(81, self.MAC, 0)

	def Recebe_Hello(self, Pacote_Hello):

		Origem 		= Pacote_Hello.GetOrigem()

		Msg = "\nMAC: "+str(self.MAC)+"| (Recebe_Hello) Pacote hello recebido de "+str(Origem)+"\n"
		Script(Msg)

		#Obtem os dados do pacote
		Rota =  Pacote_Hello.GetDados()
	
		#Verifica se a Rota existe. Se sim, discarta. Se não, adiciona
		if Rota in self.TabelaRotas:

			Msg = "\nMAC: "+str(self.MAC)+"| (Recebe_Hello) Rota já existente para "+str(Origem)+". Pacote descartado\n"
			Script(Msg)

		else:

			Msg = "\nMAC: "+str(self.MAC)+"| (Recebe_Hello) Adicionando nova rota para "+str(Origem)+"\n"
			Script(Msg)

			self.TabelaRotas.append(Rota)

	def Envia_Hello(self):
		
		Msg = "\nMAC: "+str(self.MAC)+"| (Envia_Hello) Enviando pacote hello\n"
		Script(Msg)

		Dados = []

		#Formata uma rota
		Dados.append(self.MAC)
		Dados.append(self.MAC)
		Dados.append(1)

		#Cria um pacote hello
		Pacote_Hello = Pacote_Roteamento(0, 0, 0, 0, "Hello", Dados)

		#Envia para a camada de enlace
		self.Envia_Pacote(Pacote_Hello)

	def LiberaBuffer(self, MAC):
		
		for i in range(len(self.buffer)):

			destino = self.buffer[i].GetDestino(self)

			if(destino == MAC):

				Pacote = self.buffer[i]

				self.buffer.pop(i)

				self.Envia_Dados(Pacote)

				break

	def Next_Step(self, Destino):

		nextStep = 0

		for i in range(len(self.TabelaRotas)):

			if(self.TabelaRotas[i][0] == Destino):

				nextStep = self.TabelaRotas[i][1]

		return nextStep

	def LimpaTabela(self):

		_len = len(self.TabelaRotas)

		TabelaAtualizada = []

		for i in range(_len):
			Rota_a = self.TabelaRotas[i][0:2]
			dist_a = self.TabelaRotas[i][2]

			Menor  = False

			for j in range(i+1, _len, 1):
				Rota_b = self.TabelaRotas[j][0:2]
				dist_b = self.TabelaRotas[j][2]

				if(Rota_a == Rota_b):
					if(dist_b <= dist_a):
						Menor = True

			if(Menor == False):
				TabelaAtualizada.append(self.TabelaRotas[i])

		self.TabelaRotas = TabelaAtualizada

	def FormataRota(self, Destino, Next_step, Saltos):
		Rota = []
		Rota.append(Destino)
		Rota.append(Next_step)
		Rota.append(Saltos)

		return Rota

	

