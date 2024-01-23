# 1. Crie uma classe que modele o objeto "carro".

class Carro:
    def __init__(self):

        # Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.

        self.ligado = False
        self.cor = "Vermelho"
        self.modelo = "Fiat Uno"
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 100

    # Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 20
        
    def desacelerar(self):
        if not self.ligado:
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= 20
        
    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - velocidade {self.velocidade}'

# Crie uma instância da classe carro.
carro = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro.ligar()
print('O carro está ligado? {}'.format(carro.ligado))
for _ in range(4):
    carro.acelerar()
print('A veocidade do carro é:', carro.velocidade)
print("--------------------------------------")

# Faça o carro "parar" utilizando os métodos da sua classe.
for _ in range(4):
    carro.desacelerar()
print('A veocidade do carro é:', carro.velocidade)
carro.desligar()
print('O carro está ligado? {}'.format(carro.ligado))