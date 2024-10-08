import pygame, sys, random, pygame_menu
from pygame.locals import *
from pygame_menu import themes
import pygame_menu.events
import pygame_menu.menu

pygame.init()

#Definindo cores
WHITE = (255,255,255)
BLACK = (0,0,0)
BUTTON_LIGHT = (0,181,171)      #cor para botões claros
GREY = (210,210,210)

#Definindo fontes
smallfont = pygame.font.SysFont('Verdana',30)
mediumfont = pygame.font.SysFont('Verdana', 45)
bigfont = pygame.font.SysFont('Verdana', 60)

#vairiáveis importantes
FPS = 60
SPEED = 0                       #influencia no tempo que o botão vai ficar aceso
SCORE = 0                       #pontuação do jogador
SCREEN_WIDTH = 1000             #dimensões da tela
SCREEN_HEIGH = 600

#Criando tela
DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
DISPLAYSURFACE.fill(BLACK)
pygame.display.set_caption("Press The Button")

class MainMenu:
    #Menu do jogo: Play e Quit
    def __init__(self):
        self.screen = DISPLAYSURFACE

    def run(self):
        self.running = True
        while self.running:
            self.mouse = pygame.mouse.get_pos()                 #pega a posição do mouse
            #print(self.mouse[0], self.mouse[1])
            self.draw()
            self.events()
            self.update()

    def draw(self):
            title = mediumfont.render('Press The Button',True,WHITE)       #título do jogo

            pygame.draw.rect(DISPLAYSURFACE, BLACK,[470,303,65,36])     #botão para Play e texto
            play_text = smallfont.render('Play',True, WHITE)
            
            pygame.draw.rect(DISPLAYSURFACE, BLACK,[470,372,65,36])     #botão para Quit e texto
            quit_text = smallfont.render('Quit',True, WHITE)
            
            DISPLAYSURFACE.blit(title,(324,151))                        #blit das surfaces
            DISPLAYSURFACE.blit(play_text,(471,300))    
            DISPLAYSURFACE.blit(quit_text,(470,369))


    def events(self):
        for event in pygame.event.get():                                #evento de saída
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:                    
                if 470 <= self.mouse[0] <= 535 and 372 <= self.mouse[1] <= 408:             #caso o clique seja na área em que o botão de Quit está
                    pygame.quit()
                    sys.exit()

                if 470 <= self.mouse[0] <= 535 and 303 <= self.mouse[1] <= 339:             #caso o clique seja na área em que o botão de Play está
                    DISPLAYSURFACE.fill(BLACK)
                    self.update()
                    game.run()

    def update(self):
        pygame.display.update()

class PauseMenu:
    def __init__(self) -> None:
        self.screen = DISPLAYSURFACE

    #função draw
    #função events

class Game:
    #Jogo em si
    def __init__(self):
        pygame.init()
        self.screen = DISPLAYSURFACE
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            print("Game running")
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                key = pygame.key.get_pressed()
                if key[K_RETURN]:
                    DISPLAYSURFACE.fill(BLACK)
                    gameover.run()

                if key[K_ESCAPE]:
                    DISPLAYSURFACE.fill(BLACK)
                    menu.run()


class GameOver():
    #Tela de Game Over: Mostra pontuação e Enter volta para o Menu
    def __init__(self):
        self.display = DISPLAYSURFACE

    def run(self):
        self.runnig = True
        while self.runnig:
            self.mouse = pygame.mouse.get_pos()
            self.draw()
            self.events()
            self.update()

    def draw(self):
        game_over = bigfont.render('GAME OVER',True,WHITE)              #mensagem de game over

        score_text = smallfont.render('Score:', True, WHITE)
        scores = smallfont.render('20',True, WHITE)

        pygame.draw.rect(DISPLAYSURFACE, BLACK,[428,359,143,36])         #botão para Play Again e texto
        play_again_text = smallfont.render('Play Again',True, WHITE)
            
        pygame.draw.rect(DISPLAYSURFACE, BLACK,[470,428,65,36])         #botão para Quit e texto
        quit_text = smallfont.render('Quit',True, WHITE)
            
        DISPLAYSURFACE.blit(game_over,(329,157))                        #blit das surfaces
        DISPLAYSURFACE.blit(score_text,(427,244))
        DISPLAYSURFACE.blit(scores,(534,244))
        DISPLAYSURFACE.blit(play_again_text,(429,359))    
        DISPLAYSURFACE.blit(quit_text,(470,428))


    def events(self):
        for event in pygame.event.get():                                #evento de saída
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:                    
                #caso o clique seja na área em que o botão de Play Again está
                if 428 <= self.mouse[0] <= 571 and 359 <= self.mouse[1] <= 395:
                    DISPLAYSURFACE.fill(BLACK)
                    self.update()       
                    game.run()
                
                #caso o clique seja na área em que o botão de Quit está
                if 470 <= self.mouse[0] <= 535 and 428 <= self.mouse[1] <= 464:            
                    pygame.quit()
                    sys.exit()
                
        
    def update(self):
        pygame.display.update()

#class Buttons():
    #5 Botões: Brilham em ordem aleatória

menu = MainMenu()
game = Game()
gameover = GameOver()

while True:
    menu.run()
