import math

a = int(input("Informe um valor para A "))
b = int(input("Informe um valor para B "))
c = int(input("Informe um valor para C "))

# calculando o delta
print()
delta = b**2-(4*a*c)
print("O valor de delta -> ",delta)

# obtendo o divisor da formula
divisor = 2 * a
print("O valor do divisor -> ",divisor)

# raiz de delta
if(delta<0):
    print("Não há solução no conjunto dos números reais!")
else:
    if(delta==0):
        print("Existe apenas uma raiz real")
    else:
        raiz = math.sqrt(delta)
        lin1 = (-b + raiz) / divisor
        lin2 = (-b - raiz) / divisor
        print()
        print("O valor da raiz ",raiz)
        print()
        print("Raiz 1 é ",float(lin1))
        print("Raiz 2 é ",float(lin2))