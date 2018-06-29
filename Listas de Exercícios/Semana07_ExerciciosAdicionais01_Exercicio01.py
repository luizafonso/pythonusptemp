def eh_primo(n):
	cont = 2
	primo = True
	while(cont < n):
		if((n % cont) == 0):
			primo = False
		cont += 1
	return(primo)
	
def n_primos(n):
	qtdeNumerosPrimos = 0
	contador = 2
	
	while(contador <= n):
		if(eh_primo(contador)):
			qtdeNumerosPrimos += 1
		contador += 1
	return(qtdeNumerosPrimos)


	
	
x = int(input("Informe um número inteiro maior ou igual a 2: "))
resultado = n_primos(x)
print("Existem",resultado,"números primos entre 2 e",x)