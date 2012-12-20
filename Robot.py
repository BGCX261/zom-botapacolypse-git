#------------------------------------------------------------------------------
# Project:     Zomb-botapacolypse
# Name:        Robot.py
# Purpose:     Robot Object
# 
# Authors:     Matt Hahn, Michael Simon, Tim Richter
# Main Author: Matt Hahn
#
# Created:     12/5/12
# Copyright:   (c) Matthew Hahn 2012
# Licence:     GSL
#------------------------------------------------------------------------------
import pygame, math, sys, random

from MazeWall import MazeWall
from Zombie import Zombie

class Robot():
    def __init__(self, speed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/Robot/robotright1.png")]
        self.surfaces += [pygame.image.load("rsc/Robot/robotright2.png")]
        self.surfaces += [pygame.image.load("rsc/Robot/robotshoot2.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.living = True 
        #if pygame.mixer:
        #    self.robotSound = pygame.mixer.Sound("Robot.wav")
        
    def  __str__(self):
        return "I'm a Robot " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        print "I've moved to", position
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        print "I've moved", self.speed
        
    def shootElect(self):
        if self.frame > 1:
            screen.blit(electricity.surface, electricity.rect)
        print "I'm shooting Electricity " 
        
    def hurt(self):
        print "I'm hurt"
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        print "I'm near something ", str(other.rect.center)
        
    def sight(self, other):
        if (self.distToPoint(Man.rect.center)):
            self.shootElect()
        print "I can see ", other
        
    def dropItem(self):
        print "I drop this" 
         
      
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
            self.speed[1] = self.speed[1]*-1
        print "trying to hit edges of screen", screenWidth, screenHeight
        
    def collideMazeWall(self, MazeWall):
        if (self.rect.right > MazeWall.rect.left 
                and self.rect.left < MazeWall.rect.right):
                if (self.rect.bottom > MazeWall.rect.top and 
                    self.rect.top < MazeWall.rect.bottom):
                    if (self.distToPoint(MazeWall.rect.center)
                        < self.radius + MazeWall.radius):  
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1

        print "trying to hit ", str(MazeWall)
        #if pygame.mixer:
        #   self.bounceSound.play()
        
    def collideElectricity(self, Electricity):
        print "trying to hit ", str(Electricity)
        
    def collideProjectile(self, projectile):
        print "I'm being shot by", projectile
        
    def collideRobot (self, other):
        if self.living and other.living:
            if (self.rect.right > other.rect.left 
                and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    if (self.distToPoint(other.rect.center)
                        < self.radius + other.radius):  
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1
                        other.speed[0] = other.speed[0] * -1
                        other.speed[1] = other.speed[1] * -1
                        return True
        return False
        
        
        print "trying to hit ", str(other)  
    