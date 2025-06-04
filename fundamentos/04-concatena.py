# trabalhando com concatenação de valores

name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("======================")

#Alternativa 1
print("Nome do filme:",name)
print("Ano de lançamento:",yearLaunch)
print("Nota do Filme:",noteMovie)

print("======================")
#Alternativa 2
print("Nome do Filme:", name, "\nAno de Lançamento:", yearLaunch, "\nNota do Filme:", noteMovie)


print("======================")
#Alternativa 3
print(f"Nome do Filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do Filme: {noteMovie}\n"
      )