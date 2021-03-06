class Nodo():
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.pai = None
        self.cor = "Preto"
    def getChave(self):
        return self.chave
    def setChave(self, chave):
        self.chave = chave
    def getEsquerda(self):
        return self.esquerda
    def setEsquerda(self, esquerda):
        self.esquerda = esquerda
    def getDireita(self):
        return self.direita
    def setDireita(self, direita):
        self.direita = direita
    def getPai(self):
        return self.pai
    def setPai(self, pai):
        self.pai = pai
    def setCor(self, cor):
        self.cor = cor
    def getCor(self):
        return self.cor

class Clients(Nodo):
    def __init__(self, numeroCartao):
        self.chave = numeroCartao
        self.bandeira = None
        self.nome = None
        self.limiteTotal = 0
    def __str__(self):
        return "%s\nCartão %s\n%016i\nLimite disponível: R$ %.2f" %(self.nome,self.bandeira,self.chave,self.limiteTotal)
    def __sub__(self, valorCompra):
        self.limiteTotal -= valorCompra
    def inserirBandeira(self,bandeira):
        self.bandeira = bandeira
    def inserirNome(self,nome):
        self.nome = nome
    def inserirLimiteTotal(self,limiteTotal):
        self.limiteTotal = limiteTotal

class Establishment(Nodo):
    def __init__(self, chave):
        self.chave = chave
        self.nome = None
        self.endereco = None
        self.horario = None
        self.montante = 0
        self.valor = 0
    def __str__(self):
        return ("%04i - %s\n%s\nHorário de funcionamento: %s\nMontante negociado: R$ %.2f\nTaxas a pagar: R$ %.2f"
         %(self.chave, self.nome,self.endereco,self.horario,self.montante,self.valor))
    def __add__(self, valorCompra):
        self.montante += valorCompra
        self.valor += (valorCompra*0.02)
    def inserirNome(self, nome):
        self.nome = nome
    def retornaNome(self):
        return self.nome
    def inserirEndereco(self,endereco):
        self.endereco = endereco
    def inserirHorario(self,horario):
        self.horario = horario
    def inserirMontante(self,montante):
        self.montante = montante
    def inserirValor(self,valor):
        self.valor = valor
