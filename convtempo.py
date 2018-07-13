#programa converte o numero de segundos
#Criado por Luiz Gustavo
#Curso Ciência da Computação
entrada = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(entrada)

horas_tmp = segundos // 3600
a = horas_tmp // 24
b = horas_tmp % 24
segundos_rest = segundos % 3600
c = segundos_rest // 60
d = segundos_rest % 60

print(a," dias, ",b," horas, ",c," minutos, ",d," segundos.")
