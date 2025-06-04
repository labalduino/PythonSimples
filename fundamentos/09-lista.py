#criando variável do tipo lista
filmMatrix = ["Matrix", 1999, 8.7, True] #valores são passados dentro do [] separados por virgula
print(filmMatrix)

filmList = ["Inception", "The Shawshank Redemption", 
           "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

#1 - Buscar os 2 primeiros itens da lista
print(filmList[:2])

# 2 - Buscar o último item da lista
print(filmList[-1])

#3 - Buscar filmes até uma determinada posição
print(filmList[:3])

#4 - Buscar filmes de uma posição em diante
print(filmList[1:4])