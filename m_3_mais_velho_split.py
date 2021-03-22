#Digitar o nome e a idade separadamente na mesma linha: usar o comando input.split. 
# As variaveis ficam separadas por virgula, assim como ficarao os valores delas, como strings.
pessoa_1 , idade_1 = input("Digite separadamente o primeiro nome e a idade:\n").split()
#transformar um dos valores em numoro inteiro
idade_1 = int(idade_1)

pessoa_2 , idade_2 = input("Digite separadamente o segundo nome e a idade:\n").split()

idade_2 = int(idade_2)

if idade_1 > idade_2:
    print(f"O mais velho eh {pessoa_1}")
elif idade_1 < idade_2:
    print(f"O mais velho eh {pessoa_2}")
else:
    print("Ambos tem a mesma idade")
