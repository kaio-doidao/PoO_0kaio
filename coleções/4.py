# Recebe a frase
frase = input("Digite uma frase: ")

# Converte para minúsculas
frase = frase.lower()

# Remove pontuações simples
pontuacoes = ".,!?"
for p in pontuacoes:
    frase = frase.replace(p, "")

# Divide a frase em palavras
palavras = frase.split()

# Conjunto de palavras únicas
palavras_unicas = set(palavras)

# Dicionário de frequência
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# Exibe palavras únicas
print("\nPalavras únicas:")
for palavra in sorted(palavras_unicas):
    print(palavra)

# Exibe frequências
print("\nFrequência das palavras:")
for palavra in sorted(frequencia):
    print(f"{palavra}: {frequencia[palavra]}")