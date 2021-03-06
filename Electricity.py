#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Electricity.py
# Purpose:     A Projectile
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/10/12
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math

class Electricity():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # speed
    # screenWidth
    # screenHeight
    # living
    
    # Methods or Functions
    def __init__(self, target, position, screenSize):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/electricity/electricity2.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.surface = pygame.transform.scale(self.surface, [10, 10])
        self.rect = self.surface.get_rect()
        self.speed = self.setSpeed(target, position)    
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.place(position)
        self.radius = self.rect.width/2
        self.damage = 10
        self.notBroken = True
    
    
    def __str__(self):
        return "I am electricity" + str(self.rect.center) + str(self.notBroken)
    
    def setSpeed(self, target, position):
        tX = target[0]
        tY = target[1]
        mX = position[0]
        mY = position[1]
        speed = [0,0]
        if tX > mX + 5:
            speed[0] = 10
        elif tX < mX -5:
            speed[0] = -10
        else:
            speed[0] = 0
    
        if tY > mY + 5:
            speed[1] = 10
        elif tY < mY - 5:
            speed[1] = -10
        else:
            speed[1] = 0
        
        return speed
    
    def place(self, position):
        self.rect.center = position
        
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                
    def collideWall(self, screenSize):
        if (self.rect.left < 0 
            or self.rect.right > screenSize):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom > screenSize):
            self.speed[1] = self.speed[1]*-1
            self.notBroken = False
    
    
    def collideMazeWall(self, MazeWall):
        if (self.rect.right > MazeWall.rect.left and
            self.rect.left < MazeWall.rect.right):
                if (self.rect.bottom > MazeWall.rect.top and 
                    self.rect.top < MazeWall.rect.bottom):
                        if (self.distToPoint(MazeWall.rect.center) < 
                            self.radius + MazeWall.radius): 
                                self.notBroken = False
            
    def collideAttackZombie(self, zombie):
        if (self.rect.right > zombie.rect.left 
            and self.rect.left < zombie.rect.right):
            if (self.rect.bottom > zombie.rect.top and 
                self.rect.top < zombie.rect.bottom):
                if (self.distToPoint(zombie.rect.center)
                    < self.radius + zombie.radius):  
                    self.notBroken = False
                    zombie.life -=2
                    
    def collideAttackMan(self, man):
        if (self.rect.right > man.rect.left 
            and self.rect.left < man.rect.right):
            if (self.rect.bottom > man.rect.top and 
                self.rect.top < man.rect.bottom):
                if (self.distToPoint(man.rect.center)
                    < self.radius + man.radius):  
                    self.notBroken = False
                    man.life = man.life - 1
        