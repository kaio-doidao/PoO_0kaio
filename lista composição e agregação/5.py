class Professor:
    def __init__(self, nome, titulaçao):
        self.nome = nome
        self.titulaçao = titulaçao

    def __str__(self):
        return f"Nome: {self.nome}, {self.titulaçao}"

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
    
    def detalhar_disciplina(self):
        print(f"{self.nome} - {self.professor}")

professor = Professor("Rodrigo", "Doutor")
disciplina = Disciplina("Ciencias da natureza", professor)
disciplina.detalhar_disciplina()