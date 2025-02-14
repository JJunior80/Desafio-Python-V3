# Sistema Bancário em Python - POO

## Descrição
Este projeto consiste em um sistema bancário desenvolvido em Python utilizando o paradigma de **Programação Orientada a Objetos (POO)**. Ele permite ao usuário realizar operações básicas como depósito, saque e exibição de extrato. O objetivo deste projeto é oferecer uma experiência prática no desenvolvimento de software financeiro, aplicando conceitos de **encapsulamento, herança e abstração**.

## Funcionalidades
- **Depósito**: Permite adicionar saldo à conta, registrando a transação no extrato com data e hora.
- **Saque**: Permite retirar dinheiro da conta, respeitando o saldo disponível, o limite por saque e o número máximo de saques diários.
- **Extrato**: Exibe todas as transações realizadas na conta, incluindo data e hora, bem como o saldo atual.
- **Histórico de Transações**: Armazena todas as operações realizadas na conta.
- **Modelo POO**: Implementação com classes para **Cliente**, **Conta**, **Conta Corrente** e **Histórico de Transações**.
- **Interface de Transação**: Implementação da interface `Transacao` para garantir que depósitos e saques sejam corretamente registrados.
- **Classe de Histórico**: Gerencia todas as transações da conta de forma estruturada.

## Como Usar
1. Execute o programa no terminal com o comando:
   ```sh
   python sistema_bancario_poo.py
   ```
2. Escolha uma opção do menu exibido:
   - `[d]` para Depositar
   - `[s]` para Sacar
   - `[e]` para visualizar o Extrato
   - `[q]` para Sair
3. Siga as instruções para cada operação.
4. Se atingir o limite de saques diários, aguarde até o próximo dia para novas movimentações.

## Código-Fonte
O código foi estruturado seguindo os princípios de **POO**, organizando as operações bancárias em classes bem definidas, como `Cliente`, `Conta`, `ContaCorrente`, `Historico` e `Transacao`.

## Requisitos
- Python 3.x instalado.
- Terminal para executar o programa.

## Autor
Este projeto foi desenvolvido para fins educacionais e pode ser aprimorado com novas funcionalidades no futuro. Caso queira melhorar o código, sinta-se à vontade para contribuir!

