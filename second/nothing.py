import pygame
pygame.init()
screen = pygame.display.set_mode([800, 500])
pygame.draw.rect(screen, 'grey', [0, 300, 800, 200])
pygame.display.flip()




class Cat(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.clock = pygame.time.Clock()
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        self.screen = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
        #self.win = pygame.display.set_mode((win_width,win_height))
        self.clicked = False
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height =  tilesize

    
        self.image = pygame.image.load(r'C:\Users\saira\paragame\ParaNOTnormal-Investigating\Paranotnormal Investigating\img\boy01.png')
        self.image = pygame.transform.scale(self.image, (tilesize, tilesize))
        #self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def is_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
               
                self.clicked = True
                self.message1()
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        return self.clicked
        #self.screen.blit((self.image,(self.rect.x, self.rect.y) ))
        
        
    def update(self):
        self.is_clicked()
       
        

        #pygame.display.update()

        


    def message1(self):
        #pygame.draw.rect(self.screen, 'dark gray', [0, 300, 800,200])
     
        
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.snip = self.font.render('', True, 'white')
        self.counter = 0
        self.speed = 3
        self.active_message = 0
        self.done = False
        self.messages = ['hi there',
                         'whats up']
        self.message= self.messages[self.active_message]


        m = True
        while m:
            pygame.draw.rect(self.screen, 'dark gray', [0, 300, 800,200])


            
            self.clock.tick(fps)
                    
                    
          

            if self.counter < self.speed * len(self.message):
                self.counter +=1
    
            elif self.counter >= self.speed*len(self.message):

                self.done = True
                
            keys = pygame.key.get_pressed()
           
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.done and self.active_message < len(self.messages)-1:
                            
                            self.active_message += 1
                            self.done = False
                            self.message = self.messages[self.active_message]
                            self.counter = 0
                    else:
                        m = False
                          

                    
            snip = self.font.render(self.message[0:self.counter//self.speed], True, 'white')
                #blit the snip
            self.screen.blit(snip, (10, 310))
                    
            pygame.display.flip()


            

            # if self.done == True:
            #     m = False
            #m = False
           
 def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            if Cat.is_clicked == True:
                self.cat = Cat.message1(self)
                        
