import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

fps = 60			#frames per second variable

def main():
	pygame.init()
	print("Starting asteroids!")
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()   #player update position
	drawable = pygame.sprite.Group()	#player draw shape
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0
	

	while True:
		
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill((0, 0, 0))  				#color of screen
		
		for obj in drawable:
			obj.draw(screen)

		for obj in updatable:
			obj.update(dt)

		for ast in asteroids:
			if Player.collision_check(player, ast) == True:
				print("Game over!")
				return
			
			for shot in shots: 
				if Asteroid.collision_check(ast, shot) == True:
					ast.split(), shot.kill()

		pygame.display.flip()
	
		dt = (clock.tick(fps)/1000)  # limit to fps variable



if __name__=="__main__":
	main()

