import pygame
from pygame.locals import*
import random

class Ship: #for ships and missiles
        def __init__(self, xpos, ypos, pic):
                self.x = xpos
                self.y = ypos
                self.bitmap = image.load(pic)
        def render(self):
                screen.blit(self.bitmap, (self.x, self.y))
        def Intersect(s1_x, s1_y, s2_x, s2_y):#checks when a missile and a ship overlap #CollisionDetection
                if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
                        return True
                else:
                        return False
        def Ship_Input(self):
                kinput=pygame.event.get() #handles keyboard input
                for event in kinput:
                        if kinput.type==QUIT: #if the user closes the window, stop the game
                                quit=1
                        if kinput.type==KEYDOWN: #telling the computer to recognize when a key is pressed
                                if kinput.key==K_LEFT and 10 < self.x < 590:
                                        self.x -= 5
                                if kinput.key==K_RIGHT and 590 > self.x > 10:
                                        hero.x += 5
                                if kinput.key==K_SPACE: #add a missile at the players location
                                        h_missile.x = self.x
                                        h_missile.y = self.y
def play(self, xpos, ypos):
        enemies=[] #make a new list of objects(enemies)
        x=0
        for i in range(10):
                enemies.append(Ship(50*x+50, 50, 'spacey.gif'))#add 10 new ship class objects, and positions arre staggered(first x-pos is 50, the next 100...)
                x+=1
        quit=0 #yes or no (as of now, no) for if the game should end(player has killed enemies, or hit by missiles)
        e_speed=3 #enemy speed can be ramped up later for more challenging levels
        while quit==0: 
                screen.blit(backdrop,(0,0))
                for count in range(len(enemies)): #tells how many enemies are still in the list, should decrease as enemies are killed
                        enemies[count].x += e_speed
                        enemies[count].render()
                if enemies[len(enemies)-1].x > 590:#determine direction and vert pos for the enemy row. If the furthest right enemy reaches the edge of the screen, the row goes in the other direction, and enemies move down
                        e_speed=-3
                        for count in range(len(enemies)):
                            enemies[count].y +=5
                if enemies[0].x < 10:
                        e_speed=3
                        for count in range(len(enemies)):
                                enemies[count].y +=5
                if h_missile.y < 478 and h_missile.y > 0: #draws players missile by posting the image and then subtracting 5 pixels for every loop, to make it move up
                        h_missile.render()
                        h_missile.y += -5
                if e_missile.y >= 480 and len(enemies) > 0: #checks to see if the enemy missile isnt shooting, if so, it creates a new one by putting a missile's position on one of the enemies, which is random
                        e_missile.x = enemies[random.randint(0, len(enemies)-1)].x
                        e_missile.y = enemies[0].y
                if Ship.Intersect(hero.x, hero.y, e_missile.x, e_missile.y): #if the players ship collides with enemy ship quit the game
                        quit=1
                for count in range(len(enemies)): #count through the enemy list to see if they intersect with a player missile, and that enemy gets deleted from the list of enemies, and the list shrinks, and when the list of enemies is zero, the player has killed all of the enemies, and the game needs to end
                        if Intersect(h_missile.x, h_missile.y, enemies[count].x, enemies[count].y):
                                del enemies[count]
                                break
                if len(enemies)==0:
                        quit=1
                Ship.Ship_Input(hero)
                e_missile.render()
                e_missile.y += 5
                hero.render()
    
def main():
        hero=Ship(20,400,'hero.png')
        h_missile=Ship(0,480,'h_missile.png')
        e_missile=Ship(0,480,'e_missile.png')
        screen = display.set_mode((640,480))
        key.set_repeat(1, 1)
        display.set_caption('Spacey in Space')
        backdrop = image.load('bdrop.jpg')
        play(self, xpos, ypos)
        display.update()
main()

