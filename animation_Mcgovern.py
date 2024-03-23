#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:59:51 2024

@author: thomasmcgovern
"""



import pygame

def main():
    pygame.init()

   
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("DJ Moore")

    
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("field.png")
    background = background.convert_alpha()


   
    bear = pygame.image.load("Djmoore.png")
    bear = bear.convert_alpha()
    bear = pygame.transform.scale(bear, (100, 100))
    
    
    ball = pygame.image.load("ball.png")
    ball = ball.convert_alpha()
    ball = pygame.transform.scale(ball, (50, 50))

   
    ball_x= 75
    ball_y= 150

    bear_x = 0
    bear_y = 100

   

      
    clock = pygame.time.Clock()
    keepGoing = True

       
    while keepGoing:

        
        clock.tick(30)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

       
        bear_x += 5
        ball_x += 5
       
        if bear_x > screen.get_width():
            bear_x = 0
        if ball_x > screen.get_width():
            ball_x = 0

        screen.blit(background, (0, 0))
        screen.blit(bear, (bear_x, bear_y))
        screen.blit(ball,(ball_x, ball_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()