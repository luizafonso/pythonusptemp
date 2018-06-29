#Digite um número inteiro: 78615
#O dígito das dezenas é 1

num = int(input("Digite um número inteiro: "))

dezena = num // 10
dezena = dezena % 10

print("O dígito das dezenas é",dezena)