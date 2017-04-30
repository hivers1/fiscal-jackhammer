import sys
from pygame import *
import random

class Ship:
	def __init__(self, xpos, ypos, pic)
		self.y = ypos
		self.bitmap = image.load(pic)
	def set_position(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

def Intersect(s1_x, s1_y, s2_x, s2_y):
	if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
		return 1
	else:
		return 0
def Play():
        enemies = []
        x = 0
        for count in range(10):
                enemies.append(Ship(50 * x + 50, 50, 'pic_data/enemy.gif'))
                x += 1
        quit = 0
        enemyspeed = 3
        while quit == 0:
                screen.blit(backdrop,(0,0))
                for count in range(len(enemies)):
                        enemies[count].x += + enemyspeed
                        enemies[count].render()
                if enemies[len(enemies)-1].x > 590:
                        enemyspeed = -3
                        for count in range(len(enemies)):
                                enemies[count].y += 5
                if enemies[0].x < 10:
                        enemyspeed = 3
                        for count in range(len(enemies)):
                                enemies[count].y += 5
                if h_missile.y < 479 and h_missile.y > 0:
                        h_missile.render()
                        h_missile.y -= 5
                if e_missile.y >= 480 and len(enemies) > 0:
                	e_missile.x = enemies[random.randint(0, len(enemies) - 1)].x
                        e_missile.y = enemies[0].y
        	if Intersect(hero.x, hero.y, e_missile.x, e_missile.y):
                        quit = 1
        	for count in range(0, len(enemies)):
                	if Intersect(h_missile.x, h_missile.y, enemies[count].x, enemies[count].y):
                        	del enemies[count]
                                break
        	if len(enemies) == 0:
                	quit = 1

def kInput():
        for event in event.get():
		if event.type == QUIT:
			quit = 1
		if event.type == KEYDOWN:
			if event.key == K_RIGHT and hero.x < 590:
				hero.x += 5
			if event.key == K_LEFT and hero.x > 10:
				hero.x -= 5
			if event.key == K_SPACE:
				h_missile.x = hero.x
				h_missile.y = hero.y

def main():
	init()
	screen = display.set_mode((640,480))
	key.set_repeat(1, 1)
	display.set_caption('Spacey in Space')
	backdrop = image.load('pic_data/bdrop.jpg')
	hero = Ship(20, 400, 'pic_data/hero.png')
	h_missile = Ship(0, 480, 'pic_data/h_missile.png')
	e_missile = Ship(0, 480, 'pic_data/e_missile.png')
	e_missile.render()
	e_missile.y += 5
	hero.render()
	Play()
	kInput()
	display.update()
	time.delay(5)
	
main()
