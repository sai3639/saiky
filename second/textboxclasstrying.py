class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, messages):
        self.font = pygame.font.Font('freesansbold.ttf', 24)

        self.snip = font.render('', True, 'white')
        self.counter = 0
        self.speed = 3
        #self.active_message =0
        self.done = True
        #self.message= messages[self.active_message]


        def message1(self):
            self.clock.tick(60)
            self.message = "hi"
            pygame.draw.rect(self.screen, 'dark gray', [0, 300, 800,200])

            if self.counter < self.speed * len(self.message):
                self.counter +=1
            elif self.counter >= self.speed*len(self.message):
                self.done = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN and self.done and self.active_message < len(self.message)-1:
                    self.active_message += 1
                    self.done = False
                    #self.message = messages{active_message]
                    self.counter = 0




class Text:
    



def message1(self):
    self.font = pygame.font.Font('freesansbold.ttf', 24)

    self.snip = font.render('', True, 'white')
    self.counter = 0
    self.speed = 3
    self.active_message =0
    self.done = True
    self.messages = "hi"
    self.message= self.messages[self.active_message]
    self.clock.tick(60)
    
    pygame.draw.rect(self.screen, 'dark gray', [0, 300, 800,200])

    if self.counter < self.speed * len(self.message):
        self.counter +=1
    elif self.counter >= self.speed*len(self.message):
        self.done = True

    for event in pygame.event.get():
        if event.key == pygame.K_RETURN and self.done and self.active_message < len(self.message)-1:
                self.active_message += 1
                self.done = False
                self.message = self.messages{self.active_message]
                self.counter = 0






            
#messages = list of lists?
                    #dictionary of messages to cylce through?
                    #message1: ...., message2:,,,,
                    #define different definitions/methods for each message/
                    #string of messages and call each when needed?
        
        
