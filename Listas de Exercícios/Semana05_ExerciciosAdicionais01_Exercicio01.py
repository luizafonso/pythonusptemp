def fizzbuzz(n):
	divPor3 = False
	divPor5 = False
	divPor15 = False
	retorno = ""
	if(n % 3 == 0):
		divPor3 = True
	if(n % 5 == 0):
		divPor5 = True
	if((divPor3 == True) and (divPor5 == True)):
		return("FizzBuzz")
	elif(divPor3 == True):
		return("Fizz")
	elif(divPor5 == True):
		return("Buzz")
	else:
		return(n)
