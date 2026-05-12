import random

# Gera 25 números únicos entre 1 e 40
numeros_sorteados = random.sample(range(1, 41), 25)

# Ordena os números
numeros_sorteados.sort()

# Exibe o resultado
print("Números sorteados:")
print(numeros_sorteados)