movieName = 'Top Gun'
movieDescription = '''
    Top Gun Maverick, 
    é um filme de aviação,
    muito consagrada na indústria'''

print(movieName.upper()) # tudo maiusculo
print(movieName.lower()) # tudo minusculo
print(movieName.capitalize()) # Primeira Letra maiúscula
print(movieName.title()) # Primeira Letra maiúscula
print(movieName.center(10, '-')) # Retorna string centralizada com caracteres de preenchimento
print(movieName.find('u')) # Retorna a posição de um determinado caracter
print(movieDescription.count('o')) #Retorna a contagem de caracteres
print(movieName.replace('Top','Matrix')) #Altera elemento por outro
print(movieDescription.split(','))