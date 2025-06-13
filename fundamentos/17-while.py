# Lista de Filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando while
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index +=1

# 2 - quando condição for atendida, o loop será encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(moviesList[index])
    index +=1


# 3 - quando a condição for atendida, o loop vai para a próxima iteração
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index +=1
        continue
    print(moviesList[index])
    index +=1

# 4 - Avaliaça do filme com while
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0
count = 0

while count < movieRating:
    note = float(input(f"Digite a {count+1}a nota para o filme {movieName}:\n"))
    total += note
    count += 1

if movieRating > 0:
    average  = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")

