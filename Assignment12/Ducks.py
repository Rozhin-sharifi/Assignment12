from Birds import Bird
class Duck(Bird):
    def __init__(self):
        Duck.__init__(self)
        self.image=pygame.image.load('Assignment12/images/duck.png')