def soma_hipotenusas(n):
	soma = 0
	hipotenusas = []
	for a in range(5, n+1):
		for b in range(a-1, 0, -1):
			for c in range(a-1, 0, -1):
				if((c ** 2) + (b ** 2) == (a ** 2)):
					if(not(a in hipotenusas)):
						hipotenusas.append(a)
	for i in range(0, len(hipotenusas)):
		soma += hipotenusas[i]
	return(soma)

x = int(input("informe um valor: "))
print("O valor da soma das hipotenusas é",soma_hipotenusas(x))



