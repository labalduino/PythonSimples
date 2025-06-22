"""
 *args - utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
    - os argumentos são passados como um tupla

 **kwarg - além dos valores podemos passar também as respectivas chaves para cada argumento.
 - os argumentos são passados como um dicionário
"""

# 1 - soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é {sum_total}")

sum(7)
sum(7,9)
sum(8,8,2,10,4,5)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos:")
presentation(name="Python",category="Backend", level = "iniciante")
presentation(name="Visão computacional com Python",category="IA", level = "Avançado")
presentation(name="Dashboards com Dash",category="Data Science", level = "Intermediário")