# métodos a serem usados em listas
filmList = ["Inception", "The Shawshank Redemption", 
           "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

# 1 - Tamanho da lista
print(len(filmList))

# 2 - Recuperar um item da lista pelo seu nome
print(filmList.index("Interstellar"))

# 3 - Adiconar item no final da lista
filmList.append("The Lord of the Rings")
print(filmList)

# 4 - Ordenar a lista
filmList.sort()
print(filmList)

# 5 - Copia os itens de uma lista para outra
filmsCopy = filmList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmList.clear()
print(filmList)