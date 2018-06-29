n = input("Digite um númeoro inteiro: ")

digitoAnterior = ""
achouDigitoConsecutivoRepetido = 0
for cada in n:
	if(cada == digitoAnterior):
		achouDigitoConsecutivoRepetido = 1

	digitoAnterior = cada
	
if(achouDigitoConsecutivoRepetido):
	print("sim")
else:
	print("não")