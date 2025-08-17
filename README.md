# Desafio: Criando um Sistema Bancário

Este projeto consiste na criação de um sistema bancário em Python. O objetivo é implementar as operações de saque, depósito e extrato.

## Operações

### Depósito

* Deve ser possível depositar apenas valores positivos.
* Nesta primeira versão, o sistema trabalhará com apenas um usuário, não sendo necessário identificar agência e conta bancária.
* Todos os depósitos deverão ser armazenados e exibidos na operação de extrato.

### Saque

* O sistema permitirá a realização de 3 saques diários com um limite máximo de R$ 500,00 por saque.
* Caso o saldo seja insuficiente, uma mensagem deve informar o usuário que o saque não poderá ser realizado por falta de saldo.
* Todos os saques devem ser armazenados e exibidos na operação de extrato.

### Extrato

* A operação de extrato deve listar todos os depósitos e saques efetuados.
* Ao final da listagem, o saldo atual da conta deve ser exibido.
* Os valores devem ser apresentados no formato R$ xxx.xx.
* Se não houver movimentações, deve ser exibida a mensagem: "Não foram realizadas movimentações.".
