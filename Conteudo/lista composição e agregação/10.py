class Aluno:
    def __init__(self, aluno):
        self.aluno = aluno

    def __str__(self):
        return f"Aluno: {self.aluno}"
    
class Turma:
    def __init__(self, turma):
        self.turma = turma
        self.alunos = []
    
    def __str__(self):
        return f"{self.turma}"

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_turma(self):
        print(f"{self.turma}:")
        for alunos in self.alunos:
            print(f"{alunos}")
    
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []
    
    def adicionar_turma(self, turma):
        self.turmas.append(turma)
    
    def exibir_turmas(self):
        print(f"Turmas do {self.nome}")
        for turmas in self.turmas:
            turmas.exibir_turma()

a1 = Aluno("Vitor Gabriel")
a2 = Aluno("Helia Rafaela")
a3 = Aluno("Arthur Vinicius")
a4 = Aluno("Bernardo Miranda")
a5 = Aluno("Luiz Augusto")
a6 = Aluno("Andrielly Rodrigues")

t1 = Turma("INFO2V")
t2 = Turma("INFO2VA")

ifrn = Escola("IFRN")

t1.adicionar_aluno(a1)
t1.adicionar_aluno(a2)
t1.adicionar_aluno(a3)
t2.adicionar_aluno(a4)
t2.adicionar_aluno(a5)
t2.adicionar_aluno(a6)

ifrn.adicionar_turma(t1)
ifrn.adicionar_turma(t2)

ifrn.exibir_turmas()