largura = int(input("digite a largura: "))
altura  = int(input("digite a altura: "))

cont_altura  = 1
cont_largura = 1
while(cont_altura <= altura):
	while(cont_largura <= largura):
		if((cont_altura == 1) or (cont_altura == altura)):
			print("#",end="")
		elif((cont_largura == 1) or (cont_largura == largura)):
			print("#",end="")
		else:
			print(" ",end="")
		cont_largura += 1
	print()
	cont_largura = 1
	cont_altura += 1