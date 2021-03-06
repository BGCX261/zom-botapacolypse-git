#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        StunGun.py
# Purpose:     A Weapon
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/11/12
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math

class StunGun():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # screenWidth
    # screenHeight
    # notBroken
    
    # Methods or Functions
    def __init__(self, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/stunGun/stunGun.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.place(position)
        self.notBroken = True
    
    
    def __str__(self):
        return "I am a Stun Gun" + str(self.rect.center) + str(self.notBroken)
    
    def place(self, position):
        print "I've moved to", position
    
    def distToPoint(self):
        print "I can see", str(distToPoint)
        
    def collideWall(self):
        print "Trying to hit screen walls", screenWidth, screenHeight
        
    def collideMazeWall(self, mazeWall):
        print "Trying to hit the maze wall", str(mazeWall)
        
    def collideRobot(self, robot):
        print "Trying to collide with the robot", str(robot)
        
    def collideZomie(self, other):
        print "Trying to collide with the zombie", str(zombie)

    def attack(self, other):
        print "Trying to attack", str(other)
   
    def createElectricity(self, electricity):
        print "I have created electricity", str(self)
    
    def useDown(self):
        print "I have been used", str(useDown)
        
    def broken(self):
        print "I have broken", str(self)
   
    def remove(self):
        print "I am being removed from the game", str(self)
                    
        #return True
        
        
        #return False
        
        