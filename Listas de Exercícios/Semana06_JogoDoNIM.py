def computador_escolhe_jogada(n, m):
	qtdePecasRetirar = 0
	resto = n % (m+1)
	if( resto == 0):
		qtdePecasRetirar = m
	else:
		qtdePecasRetirar = resto
	return(qtdePecasRetirar)
	
def usuario_escolhe_jogada(n, m):
	qtdePecasRetirar = 0
	jogadaValida = False
	while(jogadaValida == False):
		qtdePecasRetirar = int(input("Quantas peças você vai tirar? "))
		print()
		if ((0 < qtdePecasRetirar <= m) and (qtdePecasRetirar <= n)):
			jogadaValida = True
		else:
			print("Oops! Jogada inválida! Tente de novo.\n")
	return(qtdePecasRetirar)
	
def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	print()
	vezDoUsuario = False
	jogadaInicial = True
	if(((n % (m+1)) == 0) and (jogadaInicial == True)):
		print("Você começa!\n")
		vezDoUsuario = True
		jogadaInicial = False
	else:
		print("Computador começa!\n")
		vezDoUsuario = False
		jogadaInicial = False
	while(n != 0):
		if(vezDoUsuario == True):
			qtdePecasRetirar = usuario_escolhe_jogada(n, m)
			n -= qtdePecasRetirar
			if(qtdePecasRetirar == 1):
				print("Você tirou uma peça.")
			else:
				print("Você tirou",qtdePecasRetirar,"peças. ")
			if(n == 1):
				print("Agora resta apenas uma peça no tabuleiro.\n")
			elif(n > 1):
				print("Agora restam",n,"peças no tabuleiro.\n")			
		else:
			qtdePecasRetirar = computador_escolhe_jogada(n, m)
			n -= qtdePecasRetirar
			if(qtdePecasRetirar == 1):
				print("O computador tirou uma peça.")
			else:
				print("O computador tirou",qtdePecasRetirar,"peças. ")
			if(n == 1):
				print("Agora resta apenas uma peça no tabuleiro.\n")
			elif(n > 1):
				print("Agora restam",n,"peças no tabuleiro.\n")			
		vezDoUsuario = not(vezDoUsuario)
	vezDoUsuario = not(vezDoUsuario)
	if(vezDoUsuario == True):
		print("Fim do jogo! Você ganhou!\n")
		return(0)
	else:
		print("Fim do jogo! O computador ganhou!\n")
		return(1)
		
def campeonato():
	contador = 1
	placarUsuario = 0
	placarComputador = 0
	while(contador <= 3):
		print("**** Rodada",contador,"****\n")
		computadorGanhou = partida()
		if(computadorGanhou == 0):
			placarUsuario += 1
		else:
			placarComputador += 1
		contador += 1
	print("**** Final do campeonato! ****\n")
	print("Placar: Você",placarUsuario,"X",placarComputador,"Computador")
		
escolha = int(input("\nBem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if(escolha == 1):
	print("\nVoce escolheu uma partida isolada!\n")
	partida()
if(escolha == 2):
	print("\nVoce escolheu um campeonato!\n")
	campeonato()