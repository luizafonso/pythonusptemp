def ehPrimo(p):
	contador = 2
	primo = 1
	while(contador < p):
		if((p % contador) == 0):
			primo = 0
		contador += 1
	return(primo)
	


def maior_primo(n):
	contador = 2
	maiorPrimo = 1
	while(contador <= n):
		if(ehPrimo(contador)):
			maiorPrimo = contador
		contador += 1
	return(maiorPrimo)
