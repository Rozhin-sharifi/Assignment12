import pygame
import random
pygame.init()
from Ducks import Duck
from Stork import stork

class Gun():
    def __init__(self):
        self.x=game.width/2
        self.y=game.height/2
        self.image=pygame.image.load('Assignment12/images/shooter.png')
        self.score=0
        self.sound=pygame.mixer.Sound('Assignment12/sounds/shotgun.wav')
        self.fps=30
    def show(self):
        game.display.blit(self.image,[self.x,self.y]) 

    def fire(self):
        self.sound.play()

class Game:
    def __init__(self):
        self.width=852
        self.height=480
        self.display=pygame.display.set_mode((self.width, self.height))
        self.clock=pygame.time.Clock()
        self.background=pygame.image.load('Assignment12/images/background.jpg')
        self.fps=30


    def play(self):
        pygame.mouse.set_visible(False)
        gun=Gun()
        storks=[]
        ducks=[]

        while True:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                    return

                if event.type==pygame.MOUSEMOTION:
                    gun.x=pygame.mouse.get_pos()[0]
                    gun.y=pygame.mouse.get_pos()[1]
                if event.type==pygame.MOUSEBUTTONDOWN:
                    gun.fire()      
            if random.random()<0.04:
                 ducks.append(Duck())
                 stork.append(Stork())
            for duck in ducks:
                duck.fly()
            for stork in storks:
                stork.fly()
            
            self.display.blit(self.background,[0,0])
            gun.show()
            for duck in ducks:
                duck.show()
            for stork in storks:
                stork.show()

            pygame.display.update()
            self.clock.tick(self.fps)

if __name__=="__main__":
    game= Game()
    game.play()