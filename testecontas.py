from contas import Conta
from clientes import Cliente
from extratos import extrato
cliente1 = Cliente(123,'Edgar','Los Laureles')
cliente2 = Cliente(456,'Marco Aurelio','Perimetral')

conta1 = Conta([cliente1,cliente2],982,0)

conta1.gerarsaldo()
conta1.depositar(1500)
conta1.gerarsaldo()
conta1.sacar(500)
conta1.gerarsaldo()

conta1.extrato(123)
print(cliente1.ender)
