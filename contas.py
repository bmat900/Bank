class Conta:
    def __init__ (self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
    def depositar (self, valor):
        self.saldo += valor
    def sacar (self,valor):
        if self.saldo < valor:
            return 'Saldo insuficiente para saque'
        else:
            self.saldo -= valor
            return f'Saque realizado de: {valor}'
    def transferevalor (self, contaDestino, valor):
        if self.saldo < valor:
            return 'Saldo insuficiente para transferencia'
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return 'transferencia realizada'
    def gerarsaldo (self):
        print(f'Numero: {self.numero} \n Saldo: {self.saldo}')
