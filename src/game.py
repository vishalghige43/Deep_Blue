import pygame
from const import*
from board import*
from piece import*
from square import*

class Game():
    def __init__(self):
        self.board=Board()
    # show methods
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLM):
                if(row+col)%2==0:
                    color=(200,235,200) #light green
                else :
                    color=(119,54,88) # dark green
                rect=(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)
                pygame.draw.rect(surface,color,rect)

    def show_peices(self,surface):
        for row in range(ROWS):
            for col in range(COLM):
                if self.board.square[row][col].has_peice():
                    peice=self.board.square[row][col].peice
                    img=pygame.image.load(peice.texture)
                    img_center=col*SQSIZE+SQSIZE//2,row*SQSIZE+SQSIZE//2
                    peice.texture_rect=img.get_rect(center=img_center)
                    surface.blit(img,peice.texture_rect)
                    
