from abc import ABC, abstractmethod


# =====================================================
# QUESTÃO 4 - Classe Base Pessoa
# =====================================================
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


# =====================================================
# QUESTÃO 1 - Classe Medico
# =====================================================
class Medico(Pessoa):
    def __init__(self, nome, endereco, especialidade, crm):
        super().__init__(nome, endereco)

        self.especialidade = especialidade
        self.crm = crm

    # Método simples
    def apresentar_medico(self):
        return (
            f"Médico: {self.nome} | "
            f"Especialidade: {self.especialidade} | "
            f"CRM: {self.crm}"
        )


# =====================================================
# QUESTÃO 4 - Subclasse MedicoEspecialista
# =====================================================
class MedicoEspecialista(Medico):
    def __init__(
        self,
        nome,
        endereco,
        especialidade,
        crm,
        registro_especialidade
    ):
        super().__init__(nome, endereco, especialidade, crm)

        self.registro_especialidade = registro_especialidade

    # Polimorfismo (sobrescrita)
    def apresentar_medico(self):
        return (
            f"Médico Especialista: {self.nome} | "
            f"Especialidade: {self.especialidade} | "
            f"CRM: {self.crm} | "
            f"RQE: {self.registro_especialidade}"
        )


# =====================================================
# QUESTÃO 1 e 3 - Classe Paciente
# =====================================================
class Paciente(Pessoa):
    def __init__(
        self,
        nome,
        endereco,
        cpf,
        contato,
        data_nascimento
    ):
        super().__init__(nome, endereco)

        self.__cpf = None
        self.cpf = cpf

        self.contato = contato
        self.data_nascimento = data_nascimento

    # Encapsulamento com @property
    @property
    def cpf(self):
        return self.__cpf

    # Setter com validação
    @cpf.setter
    def cpf(self, valor):

        cpf_limpo = valor.replace(".", "").replace("-", "")

        if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
            self.__cpf = cpf_limpo
        else:
            print("Erro: O CPF deve conter exatamente 11 dígitos.")

    # Método simples
    def exibir_informacoes(self):
        return (
            f"Paciente: {self.nome} | "
            f"CPF: {self.__cpf} | "
            f"Data de Nascimento: {self.data_nascimento}"
        )

    # Método __str__
    def __str__(self):
        return f"Paciente: {self.nome} | CPF: {self.__cpf}"


# =====================================================
# QUESTÃO 5 - Classe Abstrata
# =====================================================
class DocumentoSaude(ABC):

    @abstractmethod
    def gerar_relatorio(self):
        pass


# =====================================================
# QUESTÃO 2 e 5 - Classe Clínica
# =====================================================
class Clinica:
    def __init__(self, nome_unidade):

        self.nome_unidade = nome_unidade

        # Listas privadas (Composição)
        self.__corpo_clinico = []
        self.__lista_pacientes = []

    # Adicionar médico
    def adicionar_medico(self, medico):
        self.__corpo_clinico.append(medico)

    # Adicionar paciente
    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    # Buscar paciente por CPF
    def buscar_paciente_por_cpf(self, cpf):

        cpf_limpo = cpf.replace(".", "").replace("-", "")

        for paciente in self.__lista_pacientes:
            if paciente.cpf == cpf_limpo:
                return paciente

        raise PacienteNaoCadastradoError(
            f"Paciente com CPF {cpf} não encontrado."
        )


# =====================================================
# QUESTÃO 2 e 5 - Classe Agendamento
# =====================================================
class Agendamento(DocumentoSaude):
    def __init__(self, medico, paciente, data_hora):

        # Agregação
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora

    # Implementação obrigatória
    def gerar_relatorio(self):
        return (
            "===== RELATÓRIO DA CONSULTA =====\n"
            f"Médico: {self.medico.nome}\n"
            f"Especialidade: {self.medico.especialidade}\n"
            f"Paciente: {self.paciente.nome}\n"
            f"CPF: {self.paciente.cpf}\n"
            f"Horário: {self.data_hora}"
        )


# =====================================================
# QUESTÃO 5 - Exceção Personalizada
# =====================================================
class PacienteNaoCadastradoError(Exception):
    pass


# =====================================================
# EXEMPLOS DE USO
# =====================================================

# Criando médicos
medico1 = Medico(
    "Dr. Carlos Silva",
    "Rua A, 100",
    "Cardiologia",
    "CRM12345"
)

medico2 = MedicoEspecialista(
    "Dra. Mariana Costa",
    "Av. Central, 200",
    "Neurologia",
    "CRM67890",
    "RQE9988"
)

# Criando paciente
paciente1 = Paciente(
    "Ana Souza",
    "Rua B, 250",
    "12345678901",
    "(84) 99999-9999",
    "10/05/1995"
)

# Exibindo informações
print(medico1.apresentar_medico())
print(medico2.apresentar_medico())
print(paciente1.exibir_informacoes())

# Demonstração do __str__
print(paciente1)

# Criando clínica
clinica = Clinica("Clínica Vida Saudável")

# Adicionando dados
clinica.adicionar_medico(medico1)
clinica.adicionar_medico(medico2)

clinica.adicionar_paciente(paciente1)

# Criando agendamento
agendamento1 = Agendamento(
    medico2,
    paciente1,
    "20/05/2026 14:30"
)

# Relatório da consulta
print("\n")
print(agendamento1.gerar_relatorio())

# =====================================================
# Demonstração de Polimorfismo
# =====================================================
print("\n=== POLIMORFISMO ===")

lista_medicos = [medico1, medico2]

for medico in lista_medicos:
    print(medico.apresentar_medico())

# =====================================================
# Tratamento de Exceções
# =====================================================
print("\n=== TRATAMENTO DE EXCEÇÕES ===")

try:
    paciente_busca = clinica.buscar_paciente_por_cpf(
        "99999999999"
    )

    print(paciente_busca)

except PacienteNaoCadastradoError as erro:
    print(f"Erro: {erro}")


# =====================================================
# EXPLICAÇÃO: AGREGAÇÃO x COMPOSIÇÃO
# =====================================================

"""
AGREGAÇÃO:
A classe Agendamento possui referências para objetos
Medico e Paciente já existentes.

Esses objetos continuam existindo mesmo que o
Agendamento seja removido.

Por isso, a relação é de Agregação.


COMPOSIÇÃO:
A classe Clinica possui listas privadas contendo
médicos e pacientes que fazem parte da estrutura
da clínica.

Essa relação representa composição estrutural.
"""