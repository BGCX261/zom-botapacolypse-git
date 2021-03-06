import pygame, math, sys, random
from Man import Man
from Zombie import Zombie
from Robot import Robot
from MazeWall import MazeWall
from Stick import Stick
from Electricity import Electricity
from Pistol import Pistol
from Projectile import Projectile
from HealthBar import HealthBar
from mazeMap1 import level
from gameover import GameOver
from Menu import Button
from WinBlock import WinBlock

if pygame.mixer:
    pygame.mixer.init()

#-------------Level----------------------
pygame.init()

clock = pygame.time.Clock()

screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

map = level("maze1.lvl", screenSize)

bgColor = 50, 50, 50



singlePlayer = Button("BEGIN THE END...", [350,300], (238, 0, 0))
exit = Button("EXIT", [222, 500], [238, 0, 0])
exit2 = Button("EXIT", [650, 555], [205, 205, 0])
restart = Button("RESTART", [200, 555], (205, 205, 0))
restart2 = Button("RESTART", [200, 555], (205, 205, 0))
difficulty = Button("DIFFICULTY", [289, 400], (238, 0, 0))
difficulty2 = Button("DIFFICULTY", [450, 555], (205, 205, 0))
easy = Button("EASY", [400, 300], (238, 0, 0))
medium = Button("MEDIUM", [400, 400], (238, 0, 0))
hard = Button("HARD", [400, 500], (238, 0, 0))
back = Button("BACK", [400, 200], (238, 0, 0))
menu = Button("MENU", [450, 555], (205, 205, 0))


run = False
difficultyScreen = False
mode = ""
while True:
    #----------------characters/environment-------------------
    man = Man(4, [40, 40])
    man.haveNothing = True
    zombies = [] 
    robots = []
    stick = Stick([125, 125])
    stick2 = Stick([50, 420])
    stick3 = Stick([660, 120])
    stick4 = Stick([500, 450])
    electricitys = [] 
    maxelectricitys = 2
    pistols = []
    maxPistols = 5
    projectiles = []
    maxProjectiles = 2
    healthBar = HealthBar([695, 2])
    winBlock = WinBlock([790, 560])
    
    if mode == "":
        maxZombies = 15
        maxRobots = 15
        mode = "medium"
        medium.clicked = True;
        medium.select()
        
    while not run and not man.living and not man.win and not difficultyScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if singlePlayer.collidePt(event.pos):
                        man.living = True
                        run = True
                    elif difficulty.collidePt(event.pos):
                        difficultyScreen = True
                    elif exit.collidePt(event.pos):
                        exit.clicked = True
                        sys.exit()
        screen.fill([0, 0, 0])
        banner = GameOver("rsc/Menus/titlebanner.png", [25, 25], screenSize)
        screen.blit(banner.surface, banner.rect)
        screen.blit(singlePlayer.surface, singlePlayer.rect)
        screen.blit(difficulty.surface, difficulty.rect)
        screen.blit(exit.surface, exit.rect)
        pygame.display.flip()

#---------------------Difficulty------------------------------------        
    while not run and not man.living and not man.win and difficultyScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easy.collidePt(event.pos):
                        maxZombies = 5
                        maxRobots = 5
                        mode = "easy"
                        easy.clicked = True
                        medium.clicked = False
                        hard.clicked = False
                    if medium.collidePt(event.pos):
                        maxZombies = 15
                        maxRobots = 15
                        mode = "medium"
                        easy.clicked = False
                        medium.clicked = True
                        hard.clicked = False
                    if hard.collidePt(event.pos):
                        maxZombies = 25
                        maxRobots = 25
                        mode = "hard"
                        easy.clicked = False
                        medium.clicked = False
                        hard.clicked = True
                    elif back.collidePt(event.pos):
                        difficultyScreen = False
        for b in [easy, medium, hard]:
            if b.clicked:
                b.select()
            else:
                b.deselect()
        screen.fill([0, 0, 0])
        banner = GameOver("rsc/Menus/titlebanner.png", [25, 25], screenSize)
        screen.blit(banner.surface, banner.rect)
        screen.blit(easy.surface, easy.rect)
        screen.blit(medium.surface, medium.rect)
        screen.blit(hard.surface, hard.rect)
        screen.blit(back.surface, back.rect)
        pygame.display.flip()

#-------------------------GameStart------------------------------    
    while len(zombies) < maxZombies:
        zombieSpeed = [random.randint(1,6), 
                     random.randint(1,6)]
        zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map. mazeWallSize,screenHeight - map.mazeWallSize)]
        zombies += [Zombie(zombieSpeed, zombiePos, screenSize)]
        collided = True
        while collided:
            collided = False
            for mazeWall in map.mazeWalls:
                if zombies[-1].collideMazeWall(mazeWall):
                    zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                    zombies[-1].place(zombiePos)
                    collided = True
                elif zombies[-1].chase(man):
                    zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                    zombies[-1].place(zombiePos)
                    collided = True
                    
    while len(pistols) < maxPistols:
        pistolSpeed = [0, 0]
        pistolPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
        pistols += [Pistol(pistolSpeed, pistolPos, screenSize)]
        collided = True
        while collided:
            collided = False
            for mazeWall in map.mazeWalls:
                if pistols[-1].collideMazeWall(mazeWall):
                    pistolPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                    pistols[-1].place(pistolPos)
                    collided = True
                    pistols[-1].place(pistolPos)
                    collided = True

    while len(robots) < maxRobots:
        robotSpeed = [random.randint(1,6), 
                     random.randint(1,6)]
        robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map. mazeWallSize,screenHeight - map.mazeWallSize)]
        robots += [Robot(robotSpeed, robotPos, screenSize)]
        collided = True
        while collided:
            collided = False
            for mazeWall in map.mazeWalls:
                if robots[-1].collideMazeWall(mazeWall):
                    robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                    robots[-1].place(robotPos)
                    collided = True
                elif robots[-1].see(man):
                    robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                 random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                    robots[-1].place(robotPos)
                    collided = True
                     
#----------------------Game-----------------------
    man.living = True
    while run and man.living and not man.win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP 
                    or event.key == pygame.K_w):
                        man.direction("up")
                elif (event.key == pygame.K_DOWN 
                    or event.key == pygame.K_s):
                        man.direction("down")
                elif (event.key == pygame.K_RIGHT 
                    or event.key == pygame.K_d):
                        man.direction("right")
                elif (event.key == pygame.K_LEFT 
                    or event.key == pygame.K_a):
                        man.direction("left")
#-------------------------------------------------------------------------------                        
                if (event.key == pygame.K_SPACE):
                    if man.havePistol == True:
                        projectiles += [Projectile(10, man.rect.center, man.heading, screenSize)]
                        if man.ammo > 0:
                            man.ammo -= 1
                        elif man.ammo <= 0:
                            man.ammo += 20
                        if man.ammo == 0 or man.ammo <= 0:
                            man.haveNothing = True
                            man.havePistol = False
                        print "Ammo:", man.ammo

                    

#-----------------------------------------------------------------------------------

                    for zombie in zombies:
                        if man.haveStick:
                            if zombie.distToPoint(man.rect.center) < man.attackRadius:
                                pX = man.rect.center[0]
                                pY = man.rect.center[1]
                                zX = zombie.rect.center[0]
                                zY = zombie.rect.center[1]
                                
                                if pX > zX and (event.key == pygame.K_SPACE):
                                    zombie.life -=10
                                elif pX < zX and (event.key == pygame.K_SPACE):
                                    zombie.life -=10
                            
                                if pY > zY and (event.key == pygame.K_SPACE):
                                    zombie.life -=10
                                elif pY < zY and (event.key == pygame.K_SPACE):
                                    zombie.life -=10
                    for robot in robots:
                         if man.haveStick:
                            if robot.distToPoint(man.rect.center) < man.attackRadius:
                                pX = man.rect.center[0]
                                pY = man.rect.center[1]
                                zX = robot.rect.center[0]
                                zY = robot.rect.center[1]
                                
                                if pX > zX and (event.key == pygame.K_SPACE):
                                    robot.life -=10
                                elif pX < zX and (event.key == pygame.K_SPACE):
                                    robot.life -=10
                            
                                if pY > zY and (event.key == pygame.K_SPACE):
                                    robot.life -=10
                                elif pY < zY and (event.key == pygame.K_SPACE):
                                    robot.life -=10
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP 
                    or event.key == pygame.K_w):
                        man.direction("stop up")
                elif (event.key == pygame.K_DOWN 
                    or event.key == pygame.K_s):
                        man.direction("stop down")
                elif (event.key == pygame.K_RIGHT 
                    or event.key == pygame.K_d):
                        man.direction("stop right")
                elif (event.key == pygame.K_LEFT 
                    or event.key == pygame.K_a):
                        man.direction("stop left")

         
    #------------------------Man----------------------                    
        if man.living:
            man.move()
            man.checkHave()
            man.collideWall(screenWidth, screenHeight)
            man.collideWinBlock(winBlock)
            man.collideStick(stick)
            man.collideStick(stick2)
            man.collideStick(stick3)
            man.collideStick(stick4)
            for robot in robots:
                man.collideRobot(robot)
            for pistol in pistols:
                man.collidePistol(pistol)
            healthBar.downHealth(man)
            man.dead()
    #--------Projectile Stuff-----------------
            for projectile in projectiles:
                if projectile.notBroken:
                    for pistol in pistols:
                        pistol.checkLiving(projectile)
                    projectile.move()
                    projectile.collideWall(screenSize)
                    for zombie in zombies:  
                        projectile.collideAttackZombie(zombie)
                    for robot in robots:
                        projectile.collideAttackRobot(robot)
                if not projectile.notBroken:
                    projectiles.remove(projectile)
    #------------Zombie---------------------
        for zombie in zombies:
            if zombie.unDead:
                zombie.move()
                zombie.collideZombie(zombie)
                zombie.collideMazeWall(mazeWall)
                zombie.collideWall(screenWidth, screenHeight)
                for robot in robots:
                    zombie.collideRobot(robot)
                if zombie.chase(man):
                    zombie.collideWall(screenWidth, screenHeight)
                    zombie.collideMazeWall(mazeWall)
                    for first in range(0,len(zombies)-2):
                        for second in range(first+1, len(zombies)-1):
                            zombies[first].collideZombie2(zombies[second])
                zombie.biteMan(man)
                zombie.dropItem()
                zombie.dead()
                if zombie.unDead == False:
                    zombies.remove(zombie)

        for first in range(0,len(zombies)-2):
            for second in range(first+1, len(zombies)-1):
                zombies[first].collideZombie(zombies[second])
                
    #------------------------Robot-------------------------    
            
        for robot in robots:
            if robot.living:
                robot.checkLiving()
                robot.move()
                robot.collideMazeWall(mazeWall)
                robot.collideRobot(robot)
                robot.collideWall(screenWidth, screenHeight)
                if robot.see(man):
                    electricitys += [Electricity(man.rect.center, robot.rect.center, screenSize)]
                else:
                    robot.move()
                robot.dead()
            if not robot.living:
                robots.remove(robot)
                
        for first in range(0,len(robots)-2):
            for second in range(first+1, len(robots)-1):
                robots[first].collideRobot(robots[second])
    #-----------------Electricity Stuff----------------

        for electricity in electricitys:
            if electricity.notBroken:
                electricity.move()
                electricity.collideWall(screenSize)
                electricity.collideAttackMan(man)
                for mazeWall in map.mazeWalls:
                    electricity.collideMazeWall(mazeWall)
                for zombie in zombies:
                    electricity.collideAttackZombie(zombie)
                if not electricity.notBroken:
                    electricitys.remove(electricity)


    #------------------stick.swing.whack.snapInHalf--------------------------
        if stick.notBroken:
            stick.collideZombie(zombie)
            stick.collideRobot(robot)
            #for mazeWall in map.mazeWalls:
            #    stick.collideMazeWall(mazeWall)
            
   

    #--------------------Blit-------------------    
        for mazeWall in map.mazeWalls:
            if mazeWall.living:
                for zombie in zombies:
                    zombie.collideMazeWall(mazeWall)
                for robot in robots:
                    robot.collideMazeWall(mazeWall)
                for projectile in projectiles:
                    projectile.collideMazeWall(mazeWall)
                man.collideMazeWall(mazeWall)
                screen.blit(mazeWall.surface, mazeWall.rect) 
        
        screen.blit(winBlock.surface, winBlock.rect)
        

        
        if stick.notBroken:
            screen.blit(stick.surface, stick.rect)   
        if stick2.notBroken:
            screen.blit(stick2.surface, stick2.rect)
        if stick3.notBroken:
            screen.blit(stick3.surface, stick3.rect)
        if stick4.notBroken:
            screen.blit(stick4.surface, stick4.rect)
        
        for pistol in pistols:
            if pistol.notBroken:
                screen.blit(pistol.surface, pistol.rect)
            elif pistol.notBroken == False:
                pistols.remove(pistol)
        
        if man.living:
            screen.blit(man.surface, man.rect)
        
        for zombie in zombies:
            if zombie.unDead:
                screen.blit(zombie.surface, zombie.rect)
        for robot in robots:
            if robot.living:
                screen.blit(robot.surface, robot.rect)
                
        for projectile in projectiles:
            if projectile.notBroken:
                screen.blit(projectile.surface, projectile.rect)
        
        for electricity in electricitys:
            if electricity.notBroken:
                screen.blit(electricity.surface, electricity.rect)       
        
        screen.blit(healthBar.surface, healthBar.rect)

        
        pygame.display.flip()
        clock.tick(35)
        screen.fill(bgColor)

#--------------------EndGame--------------

    while run and not man.living and not man.win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart.collidePt(event.pos):
                    man.living = True
                    run = True
                elif exit2.collidePt(event.pos):
                    exit.clicked = True
                    sys.exit()
                elif difficulty2.collidePt(event.pos):
                    run = False
                    man.living = False
                    man.win = False
                    difficultyScreen = True
        gameover = GameOver("rsc/Menus/gameover.png", [0,0], screenSize)
        screen.fill([0, 0, 0])
        screen.blit(gameover.surface, gameover.rect)
        screen.blit(restart.surface, restart.rect)
        screen.blit(exit2.surface, exit2.rect)
        screen.blit(difficulty2.surface, difficulty2.rect)
        gameover.place([400,300])
        pygame.display.flip()
        
#-----------------WinGame----------------------------
    while run and man.living and man.win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart2.collidePt(event.pos):
                    man.win = False
                elif exit2.collidePt(event.pos):
                    exit.clicked = True
                    sys.exit()
                elif difficulty2.collidePt(event.pos):
                    run = False
                    man.living = False
                    man.win = False
                    difficultyScreen = True
        gameover = GameOver("rsc/Menus/win.png", [0,0], screenSize)
        screen.fill([0, 0, 0])
        screen.blit(gameover.surface, gameover.rect)
        screen.blit(restart2.surface, restart2.rect)
        screen.blit(exit2.surface, exit2.rect)
        screen.blit(difficulty2.surface, difficulty2.rect)
        gameover.place([400,300])
        pygame.display.flip()