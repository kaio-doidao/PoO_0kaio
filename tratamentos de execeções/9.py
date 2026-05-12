# Criando exceção personalizada
class SenhaCurtaError(Exception):
    pass


def cadastrar_senha(senha):
    if len(senha) < 8:
        raise SenhaCurtaError(
            "A senha deve ter pelo menos 8 caracteres."
        )

    print("Senha cadastrada com sucesso!")


# Testes
try:
    cadastrar_senha("123")

except SenhaCurtaError as erro:
    print("Erro:", erro)


try:
    cadastrar_senha("senha123")

except SenhaCurtaError as erro:
    print("Erro:", erro)