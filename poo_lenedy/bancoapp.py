import tkinter as tk
from tkinter import messagebox, simpledialog
from conta import  ContaBancaria
from conta  import Cliente, Endereco

class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo, limite,tarifa_mensal):
        super().__init__( cliente, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal
    def sacar(self, valor):
        if valor <= self.get_saldo() + self.__limite:
            self.set_saldo(self.get_saldo() - valor)
            return True
        else:
            return False
    def cobrar_taxa(self):
        super().sacar(self.__tarifa_mensal)
  

    def exibir_dados(self):
        return  (
            super().exibir_dados() +
            f"\ntipo: {self.get_tipo_conta()}"
            f"\nlimite: {self.__limite}" +
            f"\ntarifa: {self.__tarifa_mensal}"
        )
    def get_tipo_conta(self):
        return "Conta Corrente"

class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente, numero, saldo, taxa_rendimento: float):
        super().__init__( cliente, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def sacar(self, valor):
        return super().sacar(valor)


    def render_juros(self):
        juros = self.get_saldo() * self.__taxa_rendimento
        self.depositar(juros)

      
    def exibir_dados(self):
        return(
        super().exibir_dados() +
        f"\ntipo:{self.get_tipo_conta()}" +
        f"\ntaxa de rendimento:{self.__taxa_rendimento}"
        )
    def get_tipo_conta(self):
        return "Conta Poupança"
class ContaSalario(ContaBancaria):
    def __init__(self, cliente, numero, saldo, empresa, limite_de_saques):
        super().__init__(cliente, numero, saldo)
        self.__empresa = empresa
        self.__limite_de_saques = limite_de_saques
        self.__saques_realizados = 0
    def get_tipo_conta(self):
        return "Conta Salario"
    def depositar(self, valor):
        return False
    def sacar(self, valor):
        if self.__saques_realizados < self.__limite_de_saques:
            if super().sacar(valor):
                self.__saques_realizados += 1
            return True
        return False
    
    def exibir_dados(self):
        return (
        super().exibir_dados() +
        f"\nTipo: {self.get_tipo_conta()}" +
        f"\nEmpresa: {self.__empresa}" +
        f"\nSaques realizados: {self.__saques_realizados}/{self.__limite_de_saques}"
    )
    def receber_salario(self, valor):
        self.set_saldo(self.get_saldo() + valor)
        return True
        
cliente1 = Cliente('evelyn', 999999, Endereco('RUA principal', 321, 'Bairro: brogodo', 'Cidade: cm'))
cliente2 = Cliente('pamela', 676767, Endereco('Rua paia', 333, 'Bairro: planalto', 'Cidade:cm'))
cliente3 = Cliente('kaio lindo', 111111, Endereco('Rua engenho', 888, 'Bairro: Golandim', 'Cidade:cm'))
cliente4 = Cliente('andrielly', 0000000, Endereco('Rua rio', 999, 'Bairro: coqueiros', 'Cidade: rio dos indios'))

class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x600")

        cliente1 = Cliente('evelyn', 999999, Endereco('RUA principal', 321, 'Bairro: brogodo', 'Cidade: cm'))
        cliente2 = Cliente('pamela', 676767, Endereco('Rua paia', 333, 'Bairro: planalto', 'Cidade:cm'))
        cliente3 = Cliente('kaio lindo', 111111, Endereco('Rua engenho', 888, 'Bairro: Golandim', 'Cidade:cm'))
        cliente4 = Cliente('andrielly', 0000000, Endereco('Rua rio', 999, 'Bairro: coqueiros', 'Cidade: rio dos indios'))
       
        self.contas = [
            ContaSalario(cliente1, 1001, 1000, "vivo", 10),
            ContaCorrente(cliente2, 1002, 500, 300, 10 ),
            ContaPoupanca(cliente3, 1003, 5000, 0.05 ),
            ContaPoupanca(cliente4, 1004, 250, 0.06 ),
        ]

        # messagebox.showinfo("Sucesso", "Depósito realizado.")

        self.criar_interface()
    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
    )
        titulo.pack(pady=15)

        self.btn_criarconta = tk.Button(
        self.janela,
        text="Criar Conta",
        width=15,
        command=self.criar_conta
    )
        self.btn_criarconta.pack(pady=10)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_tipo = tk.Label(
            frame,
            text=f"Tipo: {conta.get_tipo_conta()}",
            font=("Arial", 10)
    )
            lbl_tipo.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            # btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            
            # btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            # btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            btn_dados.pack(pady=2)
         
            btn_cliente = tk.Button(
                frame,
                text="Dados do Cliente",
                width=15,
                command=lambda c=conta: self.dados_cliente(c)
            )
            btn_cliente.pack(pady=2)

            
            btn_receber_salario = tk.Button(
                frame,
                text="Receber Salario",
                width=15,
                command=lambda c=conta: self.receber_salario(c)
            )

            if conta.get_tipo_conta() != "Conta Salario":
                btn_receber_salario.config(state="disabled")
                btn_receber_salario.pack(pady=2)

           
            

            btn_receber_salario.pack(pady=2)
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)
            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda c=conta: self.render_juros(c)
            )

            if conta.get_tipo_conta() != "Conta Poupança":
                    btn_rendimento.config(state="disabled")

           

            btn_rendimento.pack(pady=2)
            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda c=conta: self.cobrar_taxa(c)
            )

            if conta.get_tipo_conta() != "Conta Corrente":
                btn_taxa.config(state="disabled")

            btn_taxa.pack(pady=2)
            


    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Conta não permite depósito.")

        self.atualizar_tela()
        

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())
    
    def dados_cliente(self, conta):
        cliente = conta.get_cliente()

        messagebox.showinfo(
        "Dados do Cliente",
        cliente.exibir_dados()
    )

    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showinfo("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
        self.atualizar_tela()
    
    def receber_salario(self, conta):
        if conta.get_tipo_conta() == "Conta Salario":


            valor = simpledialog.askfloat(
            "Receber Salario",
            "Digite o valor do salario:"
        )

            if valor is not None:
                conta.receber_salario(valor)
                messagebox.showinfo("Sucesso", "Salario caiu na conta.")

        else:
                messagebox.showerror("Erro", "Conta não recebe salário")

        self.atualizar_tela()
    
    def cobrar_taxa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_taxa()
            messagebox.showinfo("Sucesso", "Taxa cobrada.")
        else:
            messagebox.showerror("Erro", "Cobrança inválida para essa conta")
        self.atualizar_tela()
    def criar_conta(self):
        janela_cadastro = tk.Toplevel(self.janela)
        janela_cadastro.title("Criar nova conta")
        janela_cadastro.geometry("300x1000")
        janela_cadastro.resizable(False, False)

        tk.Label(janela_cadastro, text="Titular:").pack(pady=5)
        entrada_titular = tk.Entry(janela_cadastro)
        entrada_titular.pack()

        tk.Label(janela_cadastro, text="Número da conta:").pack(pady=5)
        entrada_numero = tk.Entry(janela_cadastro)
        entrada_numero.pack()

        tk.Label(janela_cadastro, text="Saldo inicial:").pack(pady=5)
        entrada_saldo = tk.Entry(janela_cadastro)
        entrada_saldo.pack()



        tk.Label(janela_cadastro, text="CPF:").pack(pady=5)
        entrada_cpf = tk.Entry(janela_cadastro)
        entrada_cpf.pack()

        tk.Label(janela_cadastro, text="Tipo Conta:").pack(pady=5)
        entrada_tipo_conta = tk.Entry(janela_cadastro)
        entrada_tipo_conta.pack()

        tk.Label(janela_cadastro, text="Taxa:").pack(pady=5)
        entrada_taxa = tk.Entry(janela_cadastro)
        entrada_taxa.pack()

        tk.Label(janela_cadastro, text="Empresa:").pack(pady=5)
        entrada_empresa = tk.Entry(janela_cadastro)
        entrada_empresa.pack()

        tk.Label(janela_cadastro, text="Tarifa Mensal:").pack(pady=5)
        entrada_tarifa_mensal = tk.Entry(janela_cadastro)
        entrada_tarifa_mensal.pack()

        tk.Label(janela_cadastro, text="Saques Realizados:").pack(pady=5)
        entrada_saques_realizados = tk.Entry(janela_cadastro)
        entrada_saques_realizados.pack()

        tk.Label(janela_cadastro, text="Limtes de Saques:").pack(pady=5)
        entrada_limites_saques = tk.Entry(janela_cadastro)
        entrada_limites_saques.pack()

        tk.Label(janela_cadastro, text="Cidade:").pack(pady=5)
        entrada_cidade = tk.Entry(janela_cadastro)
        entrada_cidade.pack()

        tk.Label(janela_cadastro, text="Bairro:").pack(pady=5)
        entrada_bairro = tk.Entry(janela_cadastro)
        entrada_bairro.pack()

        tk.Label(janela_cadastro, text="Rua:").pack(pady=5)
        entrada_rua = tk.Entry(janela_cadastro)
        entrada_rua.pack()

        tk.Label(janela_cadastro, text="Número:").pack(pady=5)
        entrada_numero_casa = tk.Entry(janela_cadastro)
        entrada_numero_casa.pack()

        def salvar_conta():
            titular = entrada_titular.get()
            numero = entrada_numero.get()
            saldo = entrada_saldo.get()
            cpf = entrada_cpf.get().replace(".", "").replace("-", "")
            tipo_conta = entrada_tipo_conta.get()

            cidade = entrada_cidade.get()
            bairro = entrada_bairro.get()
            rua = entrada_rua.get()
            numero_casa = entrada_numero_casa.get()

            if titular == "" or numero == "" or saldo == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            try:
                numero = int(numero)
                saldo = float(saldo)
            except ValueError:
                messagebox.showerror("Erro", "Número da conta e saldo devem ser valores numéricos.")
                return

            endereco = Endereco(
            rua,
            int(numero_casa),
            bairro,
            cidade
        )

            cliente = Cliente(
    titular,
    int(cpf),
    endereco
)

            nova_conta = ContaPoupanca(
            cliente,
            numero,
            saldo,
            0.03
        )
            self.contas.append(nova_conta)

            messagebox.showinfo("Sucesso", "Conta criada com sucesso.")

            janela_cadastro.destroy()
            self.atualizar_tela()

        btn_salvar = tk.Button(
            janela_cadastro,
            text="Salvar conta",
            width=15,
            command=salvar_conta
        )
        btn_salvar.pack(pady=15)

        self.atualizar_tela()



janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()

