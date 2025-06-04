movieName = "Top Gun"

# string[inicio:fim] - indice começa na posição 0 | indice final  - 1

# 1 - Buscar toda string a partir da primeira posição. Se não for informado o indice final, 
# é retornada toda a string
print(movieName[0:7])
print(movieName[0:])

# 2 - Buscar toda a string até a ultima posicão
print(movieName[:7])

# 3 - Buscar toda string da terceira até a última posição
print(movieName[2:])

'''
string[inicio:fim:passo]
indice começa na posição 0 | indice final  - 1
passo - determina o incremento. POr padrão esse número é o 1.
'''

# 4  - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos índices ímpares
print(movieName[1::2])

#6 - Inverter uma string de trás para frente
print(movieName[::-1])