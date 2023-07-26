from random import randint
import pgzrun

WIDTH = 1000
HEIGHT = 500

class Player(Actor): #inheritance
    '''This is clear Player,that inherits from Actor'''
    speed = 5
    
    def _init_(self,image):
       super()._init_(image)
       self.pos = (WIDTH/2,HEIGHT/2)
    
    def movement(self):
        '''this is method movement, that controls the player movement'''
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed
        if keyboard.up:
            self.y += self.speed
        if keyboard.down:
            self.y -= self.speed
        if keyboard.space:
            self.angle += self.speed


class Enemy(Actor):
    speed = 2
    
    def __init__(self, image):
        super().__init__(image) # call parent class constructor
        self.pos = (-100, HEIGHT/2) # set initial position
    
    def tracking(self,p):
    #enemy control
      if p.x > self.x:
        self.x += self.speed
      if p.x < self.x:
        self.x -= self.speed
      if p.y > self.y:
        self.y += self.speed
      if p.y < self.y:
        self.y -= self.speed
    print(f'player {p.pos} enemy {self.pos}')
    if self.colliderect(p):
        exit()

class Fruit(Actor):
     
    def __init__(self, image):
        super().__init__(image)
        x = randint(50,WIDTH-50)
        y = randint(50,HEIGHT-50)
    
    def relocate(self):
        self.x = randint(50,WIDTH-50)
        self.y = randint(50,HEIGHT-50)

#game start now

p = Player('hero')
e = Enemy('enemy')
c = Fruit('fruit')
score = 0

def draw(): #class actor behaviour
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score: {score}',(10,10), color='white')

def update():
        p.movement()
        e.tracking(p)