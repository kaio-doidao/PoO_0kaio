def adicionar_valor(inicial, adicional):
    if adicional <= 0:
        raise ValueError(
            "Somente valores positivos devem ser adicionados ao valor inicial"
        )

    return inicial + adicional



try:
    resultado = adicionar_valor(10, 5)
    print("Resultado:", resultado)

except ValueError as erro:
    print("Erro:", erro)



try:
    resultado = adicionar_valor(10, -3)
    print("Resultado:", resultado)

except ValueError as erro:
    print("Erro:", erro)