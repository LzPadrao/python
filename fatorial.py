fat = int(input("Informe o número que deseja o fatorial: "))
produto = fat * (fat-1)
fat = fat - 2

while fat >= 0:
	produto = fat * produto
	fat = fat - 1

print("O fatorial é: ",produto)