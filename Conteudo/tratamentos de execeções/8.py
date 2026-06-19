print("Abrindo arquivo...")

try:
    resultado = 1 / 0

except ZeroDivisionError:
    print("Erro: divisão por zero.")

finally:
    print("Fechando arquivo...")