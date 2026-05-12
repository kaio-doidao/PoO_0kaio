def divisao_segura(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Erro: divisão por zero.")
        return None

    except TypeError:
        print("Erro: os parâmetros devem ser números.")
        return None


# Testes
print(divisao_segura(10, 2))
print(divisao_segura(10, 0))
print(divisao_segura(10, "a"))