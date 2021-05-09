class Bird():
    def __init__(self):
        
        self.direction=random.choice(['ltr','rtl'])
        self.y=random.randint(0,game.height/2)
        if self.direction=='ltr':
            self.x=-50
        elif self.direction=='rtl':
            self.x=game.width +50
        self.image=pygame.image.load('Assignment12/images/duck.png')
        self.speed=10
    
    def show(self):
        if self.direction=='ltr':
            game.display.blit(self.image,[self.x,self.y]) 
        elif self.direction=='rtl':  
            game.display.blit(pygame.transform.flip(self.image,True,False),[self.x,self.y]) 

    def fly(self):
        
        if self.direction=='ltr':
            self.x+=5
        elif self.direction=='rtl':
            self.x-=5
