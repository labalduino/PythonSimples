# função de potência de um número
power = lambda num: num **2

# função para verificar se um número é par
is_even = lambda x: x % 2 == 0

# função que divide um número por outro
div_num = lambda x, y: x/y

# funcão que inverte uma string
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(3))
print(is_even(4))
print(div_num(10,2))
print(div_num(5, 2))
print(reverse_string("Python"))
print(reverse_string("Javascript"))

#funcionalidades relacionadas aos filmes
movie_list = ["Titanic", "The GodFather", "INception", "Jurassic Park","The Matrix"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 9.7, 8.5],
    "INception": [8.0, 7.0, 4.5],
    "Jurassic Park": [5.5, 5.0, 35],
    "The Matrix": [8.0, 9.6, 7.9]
}

# Funçao para calcular a média de avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

# Função que verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in movie_list

# Função para recomendar um filme com base na avaliação média
recommend_movie  = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):2f}"

print(f"Média de Avaliação do filme The Matrix: {average_rating('The Matrix')}")
print(f"INception está na lista? {check_movie('INception')}")
print(f"{recommend_movie('Titanic')}")