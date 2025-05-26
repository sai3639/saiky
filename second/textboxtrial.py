
import pygame
pygame.init()

#set up for textbox
font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode([800, 500])
timer = pygame.time.Clock()
messages = ['Check out this sweet message!',
            'this is another message',
            'great time']

snip = font.render('', True, 'white')
counter = 0
speed = 3
active_message = 0
done = False
message = messages[active_message]


#game loop
run = True
while run:
    screen.fill('dark gray')
    timer.tick(60)
    #box/bubble for the text
    pygame.draw.rect(screen, 'black', [0, 300, 800, 200])

    #len(message) - length of charactes
    #speed = how long for characters to write on screen
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(messages)-1 :
                     active_message +=1
                     done = False
                     message = messages[active_message]
                     counter = 0
                

    #floor division - round down 
    snip = font.render(message[0:counter//speed], True, 'white')
    #blit the snip
    screen.blit(snip, (10, 310))


            
    pygame.display.flip()
pygame.quit()
    
