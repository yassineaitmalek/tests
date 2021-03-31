import math
import random
import pygame
import tkinter as tk

class snake(object):
    def __init__(self,color,pos):
        pass
        
    def move(self):
        pass
    
    def reset(self):
        pass
        
    def addcube(self):
        pass
    
    def draw(self,surface):
        pass
        
        

class cube(object):
    rows =0
    w=0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
        
    def move(self, dirnx, dirny):
        pass
        
    def draw(self, surface, eyes=False):
        pass
        
    
    
def drawgrid(w,rows,surface):
    sizegrid= w//rows
    x=0
    y=0
    for i in range(rows):
        x+=sizegrid
        y+=sizegrid
        
        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
        pygame.draw.line(surface,(255,255,255),(0,y),(w,y))
    
    
def redrawwindow(surface):
   
    surface.fill(0,0,0)
    drawgrid(w,rows,surface)
    pygame.display.update()
    
    
    
def randomsnack(rows,items):
    pass
    
def messagebox(subject,content):
    pass
    

    



def main():
    global w ,rows
    w=500
    height=500
    row=20
    
    wn=pygame.display.set_mode((w,w))
    s=snake((255,0,0),(10,10))
    flag = True
    clock= pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        
        redrawwindow(wn)
        
        
        
        
        
        
        
        
        