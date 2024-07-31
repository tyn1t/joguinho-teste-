class Player:
    def __init__(self, nome: str, moeda: float=0) -> None:
        self.nome = nome
        self.moeda = moeda 
        self.bolsa = dict()
        self.vida = 100
        self.status = True
        self.poder = 1
        self.nivel = 1 
        self.ataque = 1
        self.defesa = 0.1 
        self.xp = 0
        
    def level(self, xp_0):
        if self.xp == (self.nivel * 100): 
            self.nivel += 1
            self.poder += 1
            self.nivel += 1 
            self.ataque += 1
            self.defesa += 0.1 
            self.xp = 0
    
    def morre(self):
        if self.vida <= 0:
            self.status = False
            
    def __repr__(self):
        return  self.bolsa
    
    def fala(self):
        return f'Bora luta'
    
    
            
    
    