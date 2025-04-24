movieName = "Top Gun"

# string[inicio:fim] - indice começa na posição 0 | indice final - 1

# 1 - Buscar toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a útima posição
print(movieName[:7])

# 3 - Buscar toda string da terceira até a última posição
print(movieName[2:])

"""
string[inicio:fim:passo]
indice começa na posição 0 | indice final - 1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Buscar toda string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos indices impares
print(movieName[1::2])

# 6 - Inverter uma string
print(movieName[::-1])