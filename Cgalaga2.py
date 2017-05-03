import os
import sys
import pygame
import pygame.image
import random

hitbox = 25

#Initialzes object images and positions in game
class Ship:
    def __init__(self, xpos, ypos, pic):
        self.x = xpos
        self.y = ypos
        self.image = pic
    #method recognizes intersection of missiles and hero/enemy
    def Intersect(self, s1_x, s1_y, s2_x, s2_y):
        if (s1_x > s2_x - hitbox) and (s1_x < s2_x + hitbox) and (s1_y > s2_y - hitbox) and (s1_y < s2_y + hitbox):
            return True
        else:
            return False
#class with main game method
class run:

#constants used in program
    enemyspeed = 1
    hits = 0
    missile_speed = 10
    h_speed = 5

    def Play(self, hero, h_missile, enemies, screen, backdrop, missiles):
        screen.blit(backdrop, (10,10))
        if len(enemies) == 0:
            return self.hits*100, False
        for event in pygame.event.get():  #actions performed with keyboard
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and hero.x < 590:
                    hero.x += self.h_speed
                if event.key == pygame.K_LEFT and hero.x > 10:
                    hero.x -= self.h_speed
                if event.key == pygame.K_SPACE:
                    h_missile.x = hero.x
                    h_missile.y = hero.y
        max_x = enemies[0].x
        min_x = enemies[0].x
        for x in enemies:
            if x.x < min_x:
                min_x = x.x
            if x.x > max_x:
                max_x = x.x
        if max_x > 590:
            self.enemyspeed = -self.enemyspeed
            for count in range(len(enemies)):
                enemies[count].y += 5
        if min_x < 10:
            self.enemyspeed = -self.enemyspeed
            for count in range(len(enemies)):
                enemies[count].y += 5
        for m in missiles:  #makes missile image disapear when off screen
            m.y += self.missile_speed
            if m.y >= 480:
                missiles.remove(m)
            if Ship.Intersect(self, hero.x, hero.y, m.x, m.y):
                return self.hits*100, False
        if h_missile.y < 479 and h_missile.y > -100:
            h_missile.y -= self.missile_speed
        for e in enemies:
            e.x += self.enemyspeed
            if random.randint(0,100) == 1:
                missiles.append(Ship(e.x, e.y, pygame.image.load('e_missile.png')))
            if Ship.Intersect(self, h_missile.x, h_missile.y, e.x, e.y):  #removes enemies after intersection
                enemies.remove(e)
                self.hits += 1
                h_missile.y = -100
            screen.blit(e.image, (e.x, e.y))

        screen.blit(h_missile.image, (h_missile.x, h_missile.y))
        for m in missiles:
            screen.blit(m.image, (m.x, m.y))
        screen.blit(hero.image, (hero.x, hero.y))
        pygame.display.update()
        return self.hits*100, True

    def main(self, num_en):
        screen = pygame.display.set_mode((640,480))
        pygame.key.set_repeat(1, 1)
        pygame.display.set_caption('Spacey in Space')
        backdrop = pygame.image.load('bdrop.jpg')
        hero = Ship(20, 400, pygame.image.load('hero.png'))
        enemies = []
        x = 0
        row = 1
        for count in range(num_en): #adds on new enemies properly spaced each roumd
          enemies.append(Ship(50 * (x%10) + 50, 50*row, pygame.image.load('spacey.gif')))
          if (count+1)%10 == 0:
              row += 1
          x += 1
        missiles = []
        h_missile = Ship(0, 480, pygame.image.load('h_missile.png'))

        sc = 0
        r = True
        while(r): #main game loop
          sc, r = run.Play(self, hero, h_missile, enemies, screen, backdrop, missiles)
          pygame.time.Clock().tick(75)
        return sc

if __name__ == '__main__':
    run().main()
