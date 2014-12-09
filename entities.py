from pyglet import sprite, clock
import resources

class Player(sprite.Sprite):
	def __init__(self, x, y, img, batch):
		super(Player, self).__init__(img, x=x, y=y, batch=batch)

	def update(self, dt):
		pass



class Enemy(sprite.Sprite):
	speed = 0.0
	activated = False
	def __init__(self, x, y, img, batch):
		super(Enemy, self).__init__(img, x=x, y=y, batch=batch)

	def update(self, dt):
		if self.activated:
			self.x += self.speed * dt
			self.y += self.speed * dt

	def activate(self, dt):
		self.activated = True

	def initialize(self, bpm):
		self.speed = 10.0 + bpm / 10.0
		resources.enemySFX.play()
		clock.schedule_once(self.activate, (60.0/bpm) / 2.0)