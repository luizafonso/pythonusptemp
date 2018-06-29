x1 = int(input("Digite o x do primeiro ponto: "))
y1 = int(input("Digite o y do primeiro ponto: "))
x2 = int(input("Digite o x do segundo ponto: "))
y2 = int(input("Digite o y do segundo ponto: "))

maiorX = 0
maiorY = 0
menorX = 0
menorY = 0

if(x1 > x2):
	maiorX = x1
	menorX = x2
else:
	maiorX = x2
	menorX = x1
	
if(y1 > y2):
	maiorY = y1
	menorY = y2
else:
	maiorY = y2
	menorY = y1
	
if(((maiorX - menorX) >= 10) or ((maiorY - menorY) >= 10)):
	print("longe")
else:
	print("perto")