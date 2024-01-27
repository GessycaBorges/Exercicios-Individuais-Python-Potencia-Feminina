# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

class Cliente:
    def __init__(self, nome, telefone, renda_mensal, numero_da_conta):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self._numero_da_conta = numero_da_conta
        self.saque_realizado = False
        self.deposito_realizado = False
        self.saldo = 0

    def sacar(self, valor_do_saque):
        if valor_do_saque <= self.saldo:
            self.saldo -= valor_do_saque
            print(f'O saque no valor de R${valor_do_saque:.2f} foi realizado com sucesso \n')
            self.saque_realizado = True
            return self.consultar_saldo()
        else:
            print(f'Não foi possível sacar R${valor_do_saque:.2f} \n')
            self.saque_realizado = False
            return self.consultar_saldo()

    def depositar(self, valor_do_deposito):
        if valor_do_deposito >= 0:
            self.saldo += valor_do_deposito
            print(f'O depósito no valor de R${valor_do_deposito:.2f} foi realizado com sucesso \n')
            self.deposito_realizado = True
            return self.consultar_saldo()
        else:
            self.deposito_realizado = False
            print('Valor inválido.')

    def consultar_saldo(self):
        print(f'Saldo disponível: R${self.saldo:.2f}')

class Cliente_mulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal, numero_da_conta):
        super().__init__(nome, telefone, renda_mensal, numero_da_conta)
        self.saldo = 0
        self.cheque_especial = renda_mensal
        self.saldo_disponivel = self.saldo + renda_mensal
        self.saque_realizado = False
        self.deposito_realizado = False

    def sacar(self, valor_do_saque):
            # Se tiver saldo disponível para saque no saldo
            if valor_do_saque <= self.saldo:
                self.saldo -= valor_do_saque
                print(f'O saque no valor de R${valor_do_saque:.2f} foi realizado com sucesso. \n')
                self.saque_realizado = True
            # Quando é necessário tirar do cheque especial
            elif valor_do_saque <= self.saldo_disponivel:
                # Retira o resto do saldo, se houver, diminui do valor disponpivel
                self.saldo -= valor_do_saque
                self.saldo_disponivel += self.saldo
                # Ao retirar o saldo fica igual a zero e o saldo disponível se torna o cheque especial
                self.saldo = 0
                self.cheque_especial = self.saldo_disponivel
                print(f'O saque no valor de R${valor_do_saque:.2f} foi realizado com sucesso \n')
                self.saque_realizado = True
            else:
                print(f'Não foi possível sacar R${valor_do_saque}')
                self.saque_realizado = False
            
            self.consultar_saldo()
            return self.saque_realizado

    def depositar(self, valor_do_deposito):
        if valor_do_deposito >= 0:
            # Se o saldo disponível for maior que o cheque especial, somar apenas no saldo
            if self.saldo_disponivel >= self._renda_mensal:
                self.saldo += valor_do_deposito
                print(f'O depósito no valor de R${valor_do_deposito:.2f} foi realizado com sucesso \n')
                self.deposito_realizado = True
                return self.consultar_saldo()
            else:
                self.cheque_especial += valor_do_deposito
                # Se o saldo disponível for maior que o cheque especial, o valor do cheque especial volta a ser cheio e o restante soma no saldo
                if self.cheque_especial >= self._renda_mensal:
                    self.saldo_disponivel = self.cheque_especial + self.saldo
                    self.cheque_especial = self._renda_mensal
                    self.saldo = self.saldo_disponivel - self.cheque_especial
                print(f'O depósito no valor de R${valor_do_deposito:.2f} foi realizado com sucesso \n')
                self.deposito_realizado = True
                return self.consultar_saldo()
        else:
            print('Valor inválido.')

    def consultar_saldo(self):
        print(f'Saldo disponível:\n * Saldo: R${self.saldo:.2f} \n * Cheque especial: R${self.cheque_especial:.2f}.')

class Conta_corrente():
    numero_da_conta = 0

    def __init__(self):
        Conta_corrente.numero_da_conta += 1
        self.numero = Conta_corrente.numero_da_conta
        self.registro_de_operacao = []
        
    def operacoes(self, tipo, valor, cliente):
        if tipo == "depositar":
            cliente.depositar(valor)
            if cliente.deposito_realizado == True:
                deposito = f'''
                    Tipo de operação: Depósito
                    Cliente: {cliente._nome}
                    Conta número: {'{:0>5}'.format(self.numero)}
                    Valor Depositado: R${f'{valor:.2f}'}
                '''
                self.registro_de_operacao.append(deposito)
        elif tipo == "sacar":
            cliente.sacar(valor)
            if cliente.saque_realizado == True:
                saque = f'''
                    Tipo de operação: Saque
                    Cliente: {cliente._nome}
                    Conta número: {'{:0>5}'.format(self.numero)}
                    Valor Sacado: R${f'{valor:.2f}'}
                '''
                self.registro_de_operacao.append(saque)            

    def consultar_operacoes(self):
        for operacao in self.registro_de_operacao:
            print(operacao)

        



conta = Conta_corrente()
cliente = Cliente_mulher("Ana", "999999999", 1500, conta)
outra_cliente = Cliente_mulher("Maria", "988888888", 1000, conta)

outra_conta = Conta_corrente()
cliente_homem = Cliente("João", "997777777", 1000, outra_conta)

conta.operacoes("sacar", 300, cliente)
print('----------------')
conta.operacoes("depositar", 600, cliente)
print('----------------')
conta.operacoes("sacar", 300, outra_cliente)
print('----------------')
conta.operacoes("depositar", 600, outra_cliente)
print('----------------')

outra_conta.operacoes("sacar", 300, cliente_homem)
print('----------------')
outra_conta.operacoes("depositar", 600, cliente_homem)
print('----------------')
outra_conta.operacoes("sacar", 300, cliente_homem)
print('----------------')

outra_conta.consultar_operacoes()