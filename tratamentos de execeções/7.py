def verificar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError(
            "Nota inválida: deve estar entre 0 e 10"
        )

    print("Nota válida.")


# Testes
try:
    verificar_nota(8)
    verificar_nota(15)

except ValueError as erro:
    print("Erro:", erro)