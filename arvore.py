class ArvoreVP():
    def __init__(self, TipoObjeto):
        self.none = TipoObjeto
        self.none.setPai(self.none)
        self.none.setEsquerda(self.none)
        self.none.setDireita(self.none)
        self.none.setCor("Preto")
        self.raiz = self.none
    def inserir(self, nodoZ):
        nodoY = self.none
        nodoX = self.raiz
        while nodoX != self.none:
            nodoY = nodoX
            if nodoZ.getChave() < nodoX.getChave():
                nodoX = nodoX.getEsquerda()
            else:
                nodoX = nodoX.getDireita()
        nodoZ.setPai(nodoY)
        if nodoY == self.none:
            self.raiz = nodoZ
        elif nodoZ.getChave() < nodoY.getChave():
            nodoY.setEsquerda(nodoZ)
        else:
            nodoY.setDireita(nodoZ)
        nodoZ.setEsquerda(self.none)
        nodoZ.setDireita(self.none)
        nodoZ.setCor("Vermelho")

        self.consertaInserir(nodoZ)
    def consertaInserir(self, nodoZ):
        while nodoZ.getPai().cor is "Vermelho":
            if nodoZ.getPai() is nodoZ.getPai().getPai().getEsquerda():
                nodoY = nodoZ.getPai().getPai().getDireita()
                if nodoY.cor is "Vermelho":
                    nodoZ.getPai().setCor("Preto")
                    nodoY.setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    nodoZ = nodoZ.getPai().getPai()
                else:
                    if nodoZ is nodoZ.getPai().getDireita():
                        nodoZ = nodoZ.getPai()
                        self.rotacaoEsquerda(nodoZ)
                    nodoZ.getPai().setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    self.rotacaoDireita(nodoZ.getPai().getPai())
            else:
                nodoY = nodoZ.getPai().getPai().getEsquerda()
                if nodoY.getCor() is "Vermelho":
                    nodoZ.getPai().setCor("Preto")
                    nodoY.setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    nodoZ = nodoZ.getPai().getPai()
                else:
                    if nodoZ is nodoZ.getPai().getEsquerda():
                        nodoZ = nodoZ.getPai()
                        self.rotacaoDireita(nodoZ)
                    nodoZ.getPai().setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    self.rotacaoEsquerda(nodoZ.getPai().getPai())
        self.raiz.setCor("Preto")
    def rotacaoEsquerda(self,nodoX):
        nodoY = nodoX.getDireita() #define y
        if nodoY is not self.none:
            nodoX.setDireita(nodoY.getEsquerda()) #Tranforna o filho esquerdo de y no filho direito de x
            if nodoY.getEsquerda() is not self.none:
                nodoY.getEsquerda().setPai(nodoX) #Muda a progenitor de fato
            nodoY.setPai(nodoX.getPai())
            if nodoX.getPai() is self.none:
                self.raiz = nodoY
            elif nodoX == nodoX.getPai().getEsquerda():
                nodoX.getPai().setEsquerda(nodoY)
            else:
                nodoX.getPai().setDireita(nodoY)
            nodoY.setEsquerda(nodoX)
            nodoX.setPai(nodoY)
    def rotacaoDireita(self,nodoX):
        nodoY = nodoX.getEsquerda() #define y
        if nodoY is not self.none:
            nodoX.setEsquerda(nodoY.getDireita()) #Tranforna o filho direito de y no filho esquerdo de x
            if nodoY.getDireita() is not self.none:
                nodoY.getDireita().setPai(nodoX) #Muda a progenitor de fato
            nodoY.setPai(nodoX.getPai())
            if nodoX.getPai() is self.none:
                self.raiz = nodoY
            elif nodoX == nodoX.getPai().getDireita():
                nodoX.getPai().setDireita(nodoY)
            else:
                nodoX.getPai().setEsquerda(nodoY)
            nodoY.setDireita(nodoX)
            nodoX.setPai(nodoY)

    def imprimeEmOrdem(self, nodo):
            if nodo is not self.none:
                self.imprimeEmOrdem(nodo.getEsquerda())
                print("%s\n" %nodo)
                self.imprimeEmOrdem(nodo.getDireita())

    def buscar(self,raiz, numeroCartao):
        if raiz is self.none:
            return None
        elif raiz.getChave() == numeroCartao:
            return raiz
        elif numeroCartao < raiz.getChave():
            return self.buscar(raiz.getEsquerda(), numeroCartao)
        else:
            return self.buscar(raiz.getDireita(), numeroCartao)
