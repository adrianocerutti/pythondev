# 1 - Escreva um programa  que lê dois nomes e retorne uma string
# formatada no formato "UltimoNome, PrimeiroNome".
# 2 - Inverta a ordem das palavras em uma string fornecida.
# 3 - Verifique se uma string fornecida é um palíndromo
# (pode ser lida da mesma forma de trás para frente).

# 1
primeiroNome = input("Digite o primeiro nome: ")
ultimoNome = input("Digite o último nome: ")
print(f"{ultimoNome}, {primeiroNome}")

# 2
stringFornecida = input("Digite o texto que será invertido: ")
palavras = stringFornecida.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

# 3
palavra = input("Digite uma palavra: ")
palindromo = palavra[::-1]
print(palavra == palindromo)
