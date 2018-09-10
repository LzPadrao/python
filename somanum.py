print("PROGRAMA SOMA NÚMEROS")
print("")

quant = int(input("Informe a quantidade de números a serem somados"))
i = 1
valor = 0
soma = 0


while i <= quant:
	valor = int(input("Digite o valor: "))
	soma += valor
	i += 1


print(" O resultado é: ",soma)
