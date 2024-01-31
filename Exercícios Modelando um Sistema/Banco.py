from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal, numero_da_conta):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self._numero_da_conta = numero_da_conta
        self.saque_realizado = False
        self.deposito_realizado = False
        self.saldo = 0

    @abstractmethod
    def sacar(self, valor_do_saque):
        pass

    @abstractmethod
    def depositar(self, valor_do_deposito):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass

    def consultar_dados_cliente(self):
        print(f'''
            Dados do(a) cliente
            Nome: {self._nome}
            Telefone: {self._telefone}
            Renda Mensal: R${self._renda_mensal:.2f}
            Conta: {'{:0>5}'.format(self._numero_da_conta)}
        ''')

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

class Cliente_homem(Cliente):
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