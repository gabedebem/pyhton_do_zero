
n_1, n_2, n_3 = input("Digite tres numeros separadamente para entao coloca-los em ordem crescente\n").split()
n_1 = int(n_1)
n_2 = int(n_2)
n_3 = int(n_3)

if n_1<n_2>n_3:
    if n_1<n_3:
        print(f"{n_1}\n {n_3}\n {n_2}")
    else:
        print(f"{n_3}\n {n_1}\n {n_2}")

elif n_2<n_1>n_3: 
    if n_2>n_3:
        print(f"{n_3}\n {n_2}\n {n_1}")
    else:
        print(f"{n_2}\n{n_3}\n{n_1}")

elif n_1<n_3>n_2:
    if n_1>n_2:
        print(f"{n_2}\n {n_1}\n {n_3}")
    else:
        print(f"{n_1}\n{n_2}\n{n_3}")
