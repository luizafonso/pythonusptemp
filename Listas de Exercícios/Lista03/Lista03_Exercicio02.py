n = int(input("Digite o valor de n: "))

contaImpares = 1
conta = 1
while(contaImpares <= n):
	if((conta % 2) != 0):
		print(conta)
		contaImpares += 1
	conta +=1 