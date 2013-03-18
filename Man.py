#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Man.py
# Purpose:     The Player Object
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/11/12
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math
from Zombie import Zombie
from Robot import Robot
from MazeWall import MazeWall


class Man():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # speed
    # screenWidth
    # screenHeight
    # living
    
    # Methods or Functions
    def __init__(self, maxSpeed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc\man\man.png")]
        self.surfaces += [pygame.image.load("rsc\man\mann.png")]
        self.surfaces += [pygame.image.load("rsc\man\mane.png")]
        self.surfaces += [pygame.image.load("rsc\man\manw.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2.5
        self.maxSpeed = maxSpeed
        self.speed = [0,0]
        self.noSpeed = 0
        self.place(position)
        self.ammo = 20
        self.attackRadius = 40
        self.life = 100
        self.living = True
        self.heading = "s"
        self.haveNothing = True
        self.haveStick = False
        self.havePistol = False
        
    def __str__(self):
        return "I am the Man" + str(self.rect.center) + str(self.speed) + str(self.living)
    
    def place(self, position):
        #print "I've moved to", position
        self.rect = self.rect.move(position)
    
    def move(self):
        #print "I've moved", self.speed
        self.rect = self.rect.move(self.speed)
        
    def checkHave (self):
        if self.haveStick == True:
            self.havePistol = False
            self.haveNothing = False
        elif self.havePistol == True:
            self.haveStick = False
            self.haveNothing = False
        else:
            self.haveNothing == True
            self.haveStick = False
            self.havePistol = False
    
    def direction(self, dir):
        #print "I am trying to move", dir
        if dir == "up":
            if self.haveNothing:
                self.surface = pygame.image.load("rsc\man\mann.png")
            if self.havePistol:
                self.surface = pygame.image.load("rsc\man\manwgunn.png")
            if self.haveStick:
                self.surface = pygame.image.load("rsc\man\mannS.png")
            self.speed[1] = -self.maxSpeed
            self.heading = "n"
        elif dir == "down":
            if self.haveNothing:
                self.surface = pygame.image.load("rsc\man\mans.png")
            if self.havePistol:
                self.surface = pygame.image.load("rsc\man\manwguns.png")
            if self.haveStick:
                self.surface = pygame.image.load("rsc\man\mansS.png")
            self.speed[1] = self.maxSpeed
            self.heading = "s"
        elif dir == "stop up":
            self.speed[1] = self.noSpeed
        elif dir == "stop down":
            self.speed[1] = self.noSpeed
            
        if dir == "right":
            if self.haveNothing:
                self.surface = pygame.image.load("rsc\man\mane.png")
            if self.havePistol:
                self.surface = pygame.image.load("rsc\man\manwgune.png")
            if self.haveStick:
                self.surface = pygame.image.load("rsc\man\maneS.png")
            self.speed[0] = self.maxSpeed
            self.heading = "e"
        elif dir == "left":
            if self.haveNothing:
                self.surface = pygame.image.load("rsc\man\manw.png")
            if self.havePistol:
                self.surface = pygame.image.load("rsc\man\manwgunw.png")
            if self.haveStick:
                self.surface = pygame.image.load("rsc\man\manwS.png")
            self.speed[0] = -self.maxSpeed
            self.heading = "w"
        elif dir == "stop right":
            self.speed[0] = self.noSpeed
        elif dir == "stop left":
            self.speed[0] = self.noSpeed
        
        
    def distToPointWithOffset(self, pt, offset):
        x1 = self.rect.center[0] + offset[0]
        x2 = pt[0]
        y1 = self.rect.center[1] + offset[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #print "I'm near something ", str(other.rect.center)

    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #print "I'm near something ", str(other.rect.center)
        
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > screenWidth):
            self.speed[0] = self.speed[0]*0
        if (self.rect.top < 0 
            or self.rect.bottom > screenHeight):
            self.speed[1] = self.speed[1]*0
        
        if (self.rect.top < 0):
            self.speed = [0, 1]
            if (self.rect.top > 0):
                self.speed = [0, 0]
        if (self.rect.left < 0):
            self.speed = [1, 0]
            if (self.rect.left > 0):
                self.speed = [0, 0]
        if (self.rect.right > screenWidth):
            self.speed = [-1, 0]
            if (self.rect.right < screenWidth):
                self.speed = [0, 0]
        if (self.rect.bottom > screenHeight):
            self.speed = [0, -1]
            if (self.rect.bottom < screenHeight):
                self.speed = [0, 0]
        #print "Trying to hit screen walls", screenWidth, screenHeight    
    
    def collideMazeWall(self, MazeWall):
        if (self.rect.right > MazeWall.rect.left 
                and self.rect.left < MazeWall.rect.right):
                if (self.rect.bottom > MazeWall.rect.top and 
                    self.rect.top < MazeWall.rect.bottom):
                    if (self.distToPointWithOffset(MazeWall.rect.center, [0,5])
                        < self.radius + MazeWall.radius): 
                        
                        
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1
                        
                        self.move()
                        self.move()
                        
                        
                        self.speed[0] = 0
                        self.speed[1] = 0
        
    def collideRobot(self, other):
        pass
        #print "Trying to collide with the robot", str(Robot)

    def collideStick(self, stick):
        if (self.rect.right > stick.rect.left 
                and self.rect.left < stick.rect.right):
                if (self.rect.bottom > stick.rect.top and 
                    self.rect.top < stick.rect.bottom):
                    if (self.distToPoint(stick.rect.center)
                        < self.radius + stick.radius):
                        self.haveStick = True
                        stick.notBroken = False
        pass
        #print "I have collided with", stick
    
    def collidePistol(self, pistol):
        if (self.rect.right > pistol.rect.left 
            and self.rect.left < pistol.rect.right):
            if (self.rect.bottom > pistol.rect.top and 
                self.rect.top < pistol.rect.bottom):
                if (self.distToPoint(pistol.rect.center)
                    < self.radius + pistol.radius):
                    self.havePistol = True
                    pistol.notBroken = False
        pass
        #print "I have collided with", pistol
        

    def pickUpStick(self, stick):
        if self.haveStick == True:
            print "-----------------------------------------------------"    

    def pickUpPistol(self, pistol):
        if self.havePistol == True:
            print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"          
    
    def attackWithStick(self, stick, other):
        pass
    def attackWithPistol(self, pistol, other):
        pass
        #print "I have attacked", str(pistol), other

        pass
        #print "I have died"
    
    def remove(self):
        if self.life <= 0:
            self.living = False
        #print "I am being removed from the game", self
                    
        #return True
        

        #return False
        
        