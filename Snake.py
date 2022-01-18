import pygame as pg
import random

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

#main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")

class Snake:
	def __init__(self):
		self.positions = [[0,1],[1,1],[2,1],[3,1],[4,1]]
		self.snake_length = len(self.positions)
		self.x_speed = 1
		self.y_speed = 0
		
	def move(self, surface):
		#print(self.positions)
		#print(self.snake_length)
		
		for x in range(self.snake_length):
			if x == self.snake_length - 1:
				if self.positions[x][0] > surface.get_width() - 1:
					self.positions[x][0] = 0
				elif self.positions[x][1] > surface.get_height() - 1:
					self.positions[x][1] = 0
				elif self.positions[x][0] < 0:
					self.positions[x][0] = surface.get_width() - 1
				elif self.positions[x][1] < 0:
					self.positions[x][1] = surface.get_height() - 1
				else:
					self.positions[x][0] = self.positions[x][0] + (1 * self.x_speed)
					self.positions[x][1] = self.positions[x][1] + (1 * self.y_speed)
			else:
				self.positions[x][0] = self.positions[x + 1][0]
				self.positions[x][1] = self.positions[x + 1][1]
				
	def add_to_length(self):
		self.positions.append([self.positions[self.snake_length - 1][0] + (1 * self.x_speed), self.positions[self.snake_length - 1][1] + (1 * self.y_speed)])
		self.snake_length += 1 
		
class Food:
	def __init__(self):
		self.pos = [0,0]
		
	def move(self,surface):
		self.pos = [random.randrange(0,surface.get_width() - 1),random.randrange(0,surface.get_height() - 1)]

def main():
	#Initialise Pygame and screen
	pg.init()
	screen = pg.display.set_mode((30, 30), pg.SCALED)
	pg.display.set_caption("Snake")
	
	background = pg.Surface(screen.get_size())
	background = background.convert()
	background.fill((255,179,230))
	
	snake = Snake()
	food = Food()
	food.move(screen)
	
	clock = pg.time.Clock()
	going = True
	
	snake_move_event = pg.event.custom_type()
	pg.time.set_timer(snake_move_event, 40)
	
	while going:
		clock.tick(60)
		
		for event in pg.event.get():
			if event.type == snake_move_event:
				snake.move(screen)
			if event.type == pg.QUIT:
				going = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					food.move(screen)
				elif event.key == pg.K_DOWN:
					if snake.y_speed != -1:
						snake.x_speed = 0
						snake.y_speed = 1
				elif event.key == pg.K_UP:
					if snake.y_speed != 1:
						snake.x_speed = 0
						snake.y_speed = -1
				elif event.key == pg.K_LEFT:
					if snake.x_speed != 1:
						snake.x_speed = -1
						snake.y_speed = 0
				elif event.key == pg.K_RIGHT:
					if snake.x_speed != -1:
						snake.x_speed = 1
						snake.y_speed = 0
		
		if snake.positions[snake.snake_length - 1] == food.pos:
			food.move(screen)
			snake.add_to_length()
		
		#Clear screen
		screen.blit(background, (0, 0))
		
		for x in range(snake.snake_length):
			screen.set_at(snake.positions[x],(0,0,0))
			if x != snake.snake_length - 1:
				if snake.positions[snake.snake_length - 1] == snake.positions[x]:
					return
		
		screen.set_at(food.pos,(0,0,0))
		#Update display surface to screen
		pg.display.flip()
		
	pg.quit()
	
	
if __name__ == "__main__":
    main()