n = int(input("Digite um número inteiro: "))

primo = True
contador = 2
while(contador < n):
	if((n % contador) == 0):
		primo = False
	contador += 1
	
if(primo):
	print("primo")
else:
	print("não primo")