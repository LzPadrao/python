print("Trabalhando com BOOLEANOS no Python")
print()
print("Sendo 5 > 3 o resultado deve ser TRUE")
resultado = 5 > 3
print(resultado)
print()
print("Mostrando o tipo de FALSE")
tipo = type(False)
print(tipo)
print("FALSE pertence a classe BOOL")
print()
print("UTILIZANDO OPERADORES LÓGICOS")
print("##-- AND --##")
print("Sendo X = 1000")
x = 1000
print("x > 0 AND x**2 > 100 o valor retornado deve ser TRUE")
operador = x > 0 and x**2 > 100
print(operador)
print("Havendo um resultado FALSE na condição toda a regra será FALSE")
print("x < 0 AND x**2 > 100 o valor retornado deve ser FALSE pois X não é menor que 0")
operador2 = x < 0 and x**2 > 100
print(operador2)
print()
print("##-- OR --##")
print("x < 0 OR x**2 > 100 o valor retornado será TRUE")
print("Havendo um resultado TRUE na condição toda a regra será TRUE")
operador3 = x < 0 or x**2 > 100
print(operador3)
print()
print("##-- NOT --##")
print("x > 0 o valor retornado será TRUE, se colocar o NOT o resultado será FALSE")
operador4 = x > 0
print("O resultado é ",operador4)
print("Utilizando o NOT(x > 0)")
operador5 = not(operador4)
print("Aplicando o NOT o resultado agora é ",operador5)
print()
print("##-- TABELA VERDADE --##")
print("AND")
print("TRUE AND TRUE = TRUE")
print("TRUE AND FALSE = FALSE")
print("FALSE AND TRUE = FALSE")
print("FALSE AND FALSE = FALSE")
print()
print("OR")
print("TRUE OR TRUE = TRUE")
print("TRUE OR FALSE = TRUE")
print("FALSE OR TRUE = TRUEE")
print("FALSE OR FALSE = FALSE")
print()
print("NOT")
print("NOT(TRUE) = FALSE")
print("NOT(FALSE) = TRUE")
print()
print("PRECEDENCIA DE OPERADORES")
print("NIVEL    - TIPO              - OPERADOR          ")
print("7 maior  - Exponenciação     - **                ")
print("6        - Multiplicação     - *,/,//,%          ")
print("5        - Adição            - +,-               ")
print("4        - Relacional        - ==,!=,<=,>=,<,>   ")
print("3        - Lógico            - NOT               ")
print("2        - Lógico            - AND               ")
print("1 menor  - Lógico            - OR                ")