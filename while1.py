num = int(input("Informe o número a ser somado: "))

temp = 0
soma = 0

while num != 0:
	temp = num // 10
	soma = soma + (num % 10)
	num = temp

print("A soma é: ",soma)