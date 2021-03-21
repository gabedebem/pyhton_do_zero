#-*-coding: utf_8-*-

numero_1 = float(input("Digite um numero qualquer:"))
peso_numero_1 = float(input("Digite o peso para o primeiro número"))
numero_2 = float(input("Digite o segundo numero:"))
peso_numero_2 = float(input("Digite o peso para o segundo número"))
numero_3 = float(input("Digite o terceiro numero:"))
peso_numero_3 = float(input("Digite o peso para o terceiro número"))

denominador = numero_1+numero_2+numero_3
numerador = (numero_1*peso_numero_1)+(numero_2*peso_numero_2)+(numero_3*peso_numero_3)
denominador = peso_numero_1+peso_numero_2+peso_numero_3

media_ponderada = numerador/denominador
print(f"A media ponderada é {media_ponderada}")
