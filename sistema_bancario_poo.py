from datetime import datetime
from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.conta = None

    def criar_conta(self, numero):
        self.conta = ContaCorrente(numero, self)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            transacao = Deposito(valor)
            self.historico.adicionar_transacao(transacao)
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            transacao = Saque(valor)
            self.historico.adicionar_transacao(transacao)
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação falhou! Verifique o saldo e o valor informado.")
            return False

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico.transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"\nSaldo: R$ {self._saldo:.2f}")
        print("==========================================")

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        else:
            if super().sacar(valor):
                self.numero_saques += 1

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

def main():
    cliente = Cliente("João Silva", "12345678900", "Rua das Flores, 123")
    cliente.criar_conta(1)
    conta = cliente.conta

    while True:
        opcao = input("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> ").lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Operação falhou! Entrada inválida.")
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Operação falhou! Entrada inválida.")
        elif opcao == "e":
            conta.exibir_extrato()
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
