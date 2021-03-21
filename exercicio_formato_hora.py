#-*-coding: utf_8-*-

total_segundos = int(input("Digite a quantidade de segundos:\n"))

hora = total_segundos//3600
minutos = (total_segundos%3600)//60
segundos = (total_segundos%3600)%60

print(f"{hora}:{minutos}:{segundos}")
