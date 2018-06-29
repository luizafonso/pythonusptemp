def maior(x, y, z):
	maior = 0
	if((x >= y) and (x >= z)):
		maior = x
	elif((y >= z) and (y >= x)):
		maior = y
	else:
		maior = z
	return(maior)

def formaTriangulo(n):
	lado1 = 0
	lado2 = 0
	lado3 = 0
	for a in range(1, n):
		for b in range (1, n - a ):
			c = n - a - b
			print("lado a:", a, end="")
			print(" lado b:", b, end="")
			print(" lado c:",c, end="")
			if((a < b+c ) and (b < a+c) and (c < a+b)):
				print("--------> é triângulo!",end="")
				
				if(((a ** 2) + (b ** 2) == (c ** 2)) or ((a ** 2) + (c ** 2) == (b ** 2)) or ((c ** 2) + (b ** 2) == (a ** 2))):
					print(" ----->É triângulo retângulo!")
				else:
					print()
			else:
				print()
	
	
	
	
		
	


x = int(input("informe um valor: "))
formaTriangulo(x)

