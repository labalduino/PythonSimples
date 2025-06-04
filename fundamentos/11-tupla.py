# criando variável do tipo tupla
filmsTuple = ("Inception", "The Shawshank Redemption", 
           "The Dark Kgnith", "Pulp Fiction", "Interstellar")

# tipo
print(type(filmsTuple))

print(filmsTuple)

# 1 - Buscar os 2 primeiro itens da tupla
print(filmsTuple[:2])

# 2 - Buscar o último item da Tupla
print(filmsTuple[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsTuple[2:])

# 5 - recuperar o indice de um determinado filme pelo nome
print(filmsTuple.index("Pulp Fictions"))