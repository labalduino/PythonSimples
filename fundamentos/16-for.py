# Lista de Filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

print(moviesList)

# 1 - Iterando valores de uma lista
for movie in moviesList:
    print(movie)

# 2 - quando a condição for atendida, o loop será encerrado
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

# 3 - quando a condição for atendida, o loop vai para a próxima iteração
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

# 4 - Avaliaça do filme
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
for i in range(movieRating):
    note = float(input(f"Digite a {i+1}a nota para o filme {movieName}:\n"))
    total += note

if movieRating > 0:
    average  = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")

