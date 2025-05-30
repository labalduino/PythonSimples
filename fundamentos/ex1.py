#Ex1
# primeiroNome = input("Digite o nome:\n")
# segundoNome = input("Digite o sobrenome:\n")

# nomeFormatado = f"{segundoNome} {primeiroNome}"
# print(nomeFormatado)

#Ex2 - inverter um texto
# texto = "Python é muito interessanta"
# palavras = texto.split()

# textoInvertido = " ".join(palavras[::-1])
# print(textoInvertido)

#Ex3 - palindromo
texto1 = 'arara'
texto2 = 'python'

#Remove espaço e diexa nome em minúsculo
texto1Format = texto1.lower().replace(" ", "")
texto2Format = texto2.lower().replace(" ", "")

#Verifica se texto original é igual ao seu revers
palindromo1=texto1Format == texto1[::-1]
palindromo2=texto2Format == texto2[::-1]

print(palindromo1)
print(palindromo2)

