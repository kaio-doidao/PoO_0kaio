lista = [10, 20, 30]

try:
    print(lista[5])

except IndexError:
    print("Erro: Índice inexistente.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")