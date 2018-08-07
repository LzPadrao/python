num = int(input("Informe um número para analise: "))

if((num % 3 == 0) and (num % 5 == 0)):
    print("FizzBuzz")
else:
    print(num)