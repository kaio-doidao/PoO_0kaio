# Classe Medico
class Medico:
    def __init__(self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

    # Método para apresentar os dados do médico
    def apresentar_medico(self):
        return f"Médico: {self.nome} | Especialidade: {self.especialidade} | CRM: {self.crm}"


# Classe Paciente
class Paciente:
    def __init__(self, nome, cpf, contato, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    # Método para exibir informações do paciente
    def exibir_informacoes(self):
        return (
            f"Paciente: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Data de Nascimento: {self.data_nascimento}"
        )


# Exemplo de uso

medico1 = Medico("Dr. Carlos Silva", "Cardiologia", "CRM12345")
print(medico1.apresentar_medico())

paciente1 = Paciente("Ana Souza", "123.456.789-00", "(84) 99999-9999", "10/05/1995")
print(paciente1.exibir_informacoes())







# Classe Medico
class Medico:
    def __init__(self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f"Médico: {self.nome} | Especialidade: {self.especialidade} | CRM: {self.crm}"


# Classe Paciente
class Paciente:
    def __init__(self, nome, cpf, contato, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        return (
            f"Paciente: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Data de Nascimento: {self.data_nascimento}"
        )


# Classe Clinica (Composição)
class Clinica:
    def __init__(self, nome_unidade):
        self.nome_unidade = nome_unidade
        
        # Listas privadas
        self.__corpo_clinico = []
        self.__lista_pacientes = []

    # Método para adicionar médicos
    def adicionar_medico(self, medico):
        self.__corpo_clinico.append(medico)

    # Método para adicionar pacientes
    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    # Métodos opcionais para visualizar os dados
    def listar_medicos(self):
        for medico in self.__corpo_clinico:
            print(medico.apresentar_medico())

    def listar_pacientes(self):
        for paciente in self.__lista_pacientes:
            print(paciente.exibir_informacoes())


# Classe Agendamento (Agregação)
class Agendamento:
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora

    def exibir_agendamento(self):
        return (
            f"Consulta agendada com Dr(a). {self.medico.nome} "
            f"para o paciente {self.paciente.nome} "
            f"em {self.data_hora}"
        )


# Exemplo de uso

# Criando médico e paciente
medico1 = Medico("Dr. Carlos Silva", "Cardiologia", "CRM12345")
paciente1 = Paciente("Ana Souza", "123.456.789-00", "(84) 99999-9999", "10/05/1995")

# Criando clínica
clinica = Clinica("Clínica Vida Saudável")

# Adicionando objetos à clínica
clinica.adicionar_medico(medico1)
clinica.adicionar_paciente(paciente1)

# Criando agendamento
agendamento1 = Agendamento(medico1, paciente1, "20/05/2026 14:30")

# Exibindo informações
print(agendamento1.exibir_agendamento())



















# Classe Paciente com Encapsulamento
class Paciente:
    def __init__(self, nome, cpf, contato, data_nascimento):
        self.nome = nome
        self.__cpf = None  # atributo privado
        self.cpf = cpf     # usa o setter para validar
        self.contato = contato
        self.data_nascimento = data_nascimento

    # Getter do CPF
    @property
    def cpf(self):
        return self.__cpf

    # Setter do CPF com validação
    @cpf.setter
    def cpf(self, valor):
        # Remove pontos e traços, caso existam
        cpf_limpo = valor.replace(".", "").replace("-", "")

        # Verifica se possui exatamente 11 dígitos numéricos
        if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
            self.__cpf = cpf_limpo
        else:
            print("Erro: O CPF deve conter exatamente 11 dígitos.")
            # O valor anterior permanece inalterado

    # Método para exibir informações
    def exibir_informacoes(self):
        return (
            f"Paciente: {self.nome} | "
            f"CPF: {self.__cpf} | "
            f"Data de Nascimento: {self.data_nascimento}"
        )

    # Método dunder __str__
    def __str__(self):
        return f"Paciente: {self.nome} | CPF: {self.__cpf}"


# Exemplo de uso

paciente1 = Paciente(
    "Ana Souza",
    "12345678901",
    "(84) 99999-9999",
    "10/05/1995"
)

# Exibição usando print()
print(paciente1)

# Tentativa de CPF inválido
paciente1.cpf = "123"

# O CPF anterior continua armazenado
print(paciente1)













# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


# Classe Medico herdando de Pessoa
class Medico(Pessoa):
    def __init__(self, nome, endereco, especialidade, crm):
        # Inicializa atributos herdados
        super().__init__(nome, endereco)

        # Atributos próprios
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return (
            f"Médico: {self.nome} | "
            f"Endereço: {self.endereco} | "
            f"Especialidade: {self.especialidade} | "
            f"CRM: {self.crm}"
        )


# Classe Paciente herdando de Pessoa
class Paciente(Pessoa):
    def __init__(self, nome, endereco, cpf, contato, data_nascimento):
        # Inicializa atributos herdados
        super().__init__(nome, endereco)

        self.__cpf = None
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    # Getter
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

    def exibir_informacoes(self):
        return (
            f"Paciente: {self.nome} | "
            f"CPF: {self.__cpf} | "
            f"Data de Nascimento: {self.data_nascimento}"
        )

    # Método __str__
    def __str__(self):
        return f"Paciente: {self.nome} | CPF: {self.__cpf}"


# Subclasse MedicoEspecialista
class MedicoEspecialista(Medico):
    def __init__(self, nome, endereco, especialidade, crm, registro_especialidade):
        # Inicializa atributos da classe Medico
        super().__init__(nome, endereco, especialidade, crm)

        # Novo atributo
        self.registro_especialidade = registro_especialidade

    # Sobrescrita de método (Polimorfismo)
    def apresentar_medico(self):
        return (
            f"Médico Especialista: {self.nome} | "
            f"Endereço: {self.endereco} | "
            f"Especialidade: {self.especialidade} | "
            f"CRM: {self.crm} | "
            f"Registro da Especialidade: {self.registro_especialidade}"
        )


# Exemplo de uso

# Objeto da classe Medico
medico1 = Medico(
    "Dr. Carlos Silva",
    "Rua A, 100",
    "Cardiologia",
    "CRM12345"
)

# Objeto da classe MedicoEspecialista
medico2 = MedicoEspecialista(
    "Dra. Mariana Costa",
    "Av. Central, 200",
    "Neurologia",
    "CRM67890",
    "RQE9988"
)

# Lista com objetos de tipos diferentes
lista_medicos = [medico1, medico2]

# Demonstração do Polimorfismo
for medico in lista_medicos:
    print(medico.apresentar_medico())











from abc import ABC, abstractmethod


# =========================
# Classe Abstrata
# =========================
class DocumentoSaude(ABC):

    @abstractmethod
    def gerar_relatorio(self):
        pass


# =========================
# Classe Base Pessoa
# =========================
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


# =========================
# Classe Medico
# =========================
class Medico(Pessoa):
    def __init__(self, nome, endereco, especialidade, crm):
        super().__init__(nome, endereco)

        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return (
            f"Médico: {self.nome} | "
            f"Especialidade: {self.especialidade} | "
            f"CRM: {self.crm}"
        )


# =========================
# Classe Paciente
# =========================
class Paciente(Pessoa):
    def __init__(self, nome, endereco, cpf, contato, data_nascimento):
        super().__init__(nome, endereco)

        self.__cpf = None
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    # Getter
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
            print("Erro: CPF inválido.")

    def __str__(self):
        return f"Paciente: {self.nome} | CPF: {self.__cpf}"


# =========================
# Exceção Personalizada
# =========================
class PacienteNaoCadastradoError(Exception):
    pass


# =========================
# Classe Clínica
# =========================
class Clinica:
    def __init__(self, nome_unidade):
        self.nome_unidade = nome_unidade
        self.__lista_pacientes = []

    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    # Método de busca com exceção
    def buscar_paciente_por_cpf(self, cpf):

        cpf_limpo = cpf.replace(".", "").replace("-", "")

        for paciente in self.__lista_pacientes:
            if paciente.cpf == cpf_limpo:
                return paciente

        # Levanta exceção caso não encontre
        raise PacienteNaoCadastradoError(
            f"Paciente com CPF {cpf} não encontrado."
        )


# =========================
# Classe Agendamento
# =========================
class Agendamento(DocumentoSaude):
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora

    # Implementação obrigatória do método abstrato
    def gerar_relatorio(self):
        return (
            "===== RELATÓRIO DE CONSULTA =====\n"
            f"Médico: {self.medico.nome}\n"
            f"Especialidade: {self.medico.especialidade}\n"
            f"Paciente: {self.paciente.nome}\n"
            f"CPF: {self.paciente.cpf}\n"
            f"Horário: {self.data_hora}\n"
        )


# =========================
# Exemplo de Uso
# =========================

# Criando médico
medico1 = Medico(
    "Dr. Carlos Silva",
    "Rua A, 100",
    "Cardiologia",
    "CRM12345"
)

# Criando paciente
paciente1 = Paciente(
    "Ana Souza",
    "Rua B, 200",
    "12345678901",
    "(84) 99999-9999",
    "10/05/1995"
)

# Criando clínica
clinica = Clinica("Clínica Vida Saudável")

# Adicionando paciente
clinica.adicionar_paciente(paciente1)

# Criando agendamento
agendamento1 = Agendamento(
    medico1,
    paciente1,
    "20/05/2026 14:30"
)

# Gerando relatório
print(agendamento1.gerar_relatorio())


# =========================
# Tratamento de Exceções
# =========================

try:
    paciente_encontrado = clinica.buscar_paciente_por_cpf("99999999999")
    print(paciente_encontrado)

except PacienteNaoCadastradoError as erro:
    print(f"Erro: {erro}")