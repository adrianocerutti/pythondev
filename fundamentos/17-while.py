# Lista de filmes
movieList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1

# 2 - Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        break
    print(movieList[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        index += 1
        continue
    print(movieList[index])
    index += 1

# 4 - Avaliação do filme com while
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))
total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: "))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")
