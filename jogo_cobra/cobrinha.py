class Cobra:
    def __init__(self, tam_tela=(300,400),
                        posicao=[100,50],# esquerda, cima
                        corpo=[[100,50],[90,50],[80,50]],
                        direcao = 'DIREITA'):
        self.tam_tela = tam_tela
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = direcao
        
                    
    def muda_direcao(self, nova_direcao):
        if nova_direcao == 'DIREITA' and not self.direcao == 'ESQUERDA':
            self.direcao = 'DIREITA'
        if nova_direcao == 'ESQUERDA' and not self.direcao == 'DIREITA':
            self.direcao = 'ESQUERDA'
        if nova_direcao == 'CIMA' and not self.direcao == 'BAIXO':
            self.direcao = 'CIMA'
        if nova_direcao == 'BAIXO' and not self.direcao == 'CIMA':
            self.direcao = 'BAIXO'



    
    def move(self, posicao_comida):
        if self.direcao == 'DIREITA':
            self.posicao[0] += 10
        if self.direcao == 'ESQUERDA':
            self.posicao[0] -= 10
        if self.direcao == 'CIMA':
            self.posicao[1] -= 10
        if self.direcao == 'BAIXO':
            self.posicao[1] += 10
        

        # adiciona pedaço do corpo da cobra da frente da cabeça
        self.corpo.insert(0, list(self.posicao))
        # confere se comeu comida
        if self.posicao == posicao_comida:
            return True

        # remove pedaço da cauda
        self.corpo.pop()
        return False




    def verifica_colisão(self):
        pass




