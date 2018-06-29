def soma_hipotenusas(n):
	lista = []
	cont1 = 1
	while(cont1 <= (n - 2)):
		c1 = cont1
		cont2 = 1
		#print("cateto 1:",c1)
		while(cont2 <= (n - 2)):
			c2 = cont2
			hip = n - c1 - c2
			if(hip > 1):
				if(((c1 ** 2) + (c2 ** 2)) == (hip ** 2)):
					valorJaExiste = False
					conta = 0
					if(len(lista) > 0):
						while(conta < len(lista)):
							if(hip == lista[conta]):
								valorJaExiste = True
							conta += 1
					if(valorJaExiste == False):
						lista.append(hip)
			cont2 += 1
		cont1 += 1
	#print("Para n =",n,", as hipotenusas são: ",end="")
	soma = 0
	i = 0
	while(i < len(lista)):
		#print(lista[i],", ",end="")
		soma += lista[i]
		i += 1
	#print()
	return(soma)
		
		
x = int(input("informe um valor: "))
print("resultado:",soma_hipotenusas(x))