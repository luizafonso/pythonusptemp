#Dada a quantidade em segundos, quebre esse valor em dias, horas, minutos e segundos. A saída deve estar no formato:
#a dias, b horas, c minutos e d segundos.

#Por favor, entre com o número de segundos que deseja converter: 178615
#2 dias, 1 horas, 36 minutos e 55 segundos.

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = ((segundos % 86400) % 3600) // 60
segundos = ((segundos % 86400) % 3600) % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")