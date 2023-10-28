import pygame
import sys

from const import*
from game import*

class Main():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption('CHESS')
        self.game=Game()

    
    def mainloop(self):
        game=self.game
        screen=self.screen
        while True:
            game.show_bg(screen)
            game.show_peices(screen)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()    

main=Main()
main.mainloop()