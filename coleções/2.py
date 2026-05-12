anos = {}

while True:
    entrada = input("Digite o ano de nascimento (ou ENTER para sair): ")

    if entrada == "":
        break

    ano = int(entrada)

    # Conta quantas pessoas nasceram no mesmo ano
    if ano in anos:
        anos[ano] += 1
    else:
        anos[ano] = 1

print("\nRelatório de nascimentos:")

for ano in sorted(anos):
    print(f"{ano}: {anos[ano]} pessoa(s)")