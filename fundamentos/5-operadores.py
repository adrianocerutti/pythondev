num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(sum)
print(sub)
print(f"Resto da divisão de {num1} por {num2} é: {mod}")
print(f"Exponenciação do número de {num1} por {num2} é: {exp}")