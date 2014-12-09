from pyglet import window, app, clock, graphics, event
from entities import Player, Enemy
import resources

class Game(window.Window):
	mainbatch = graphics.Batch()
	entities = []
	bpm = 70.0
	def __init__(self, w, h):
		super(Game, self).__init__(w, h)

	def initialize(self):
		self.entities.append(Player(100, 100, resources.playerSprite, self.mainbatch))
		self.addEnemy(0.0)

	def addEnemy(self, dt):
		enemy = Enemy(50, 50, resources.enemySprite, self.mainbatch)
		enemy.initialize(self.bpm)
		self.entities.append(enemy)
		clock.schedule_once(self.addEnemy, 60.0 / self.bpm)
		self.bpm += 1.0

	def update(self, dt):
		for e in self.entities:
			e.update(dt)

	def on_draw(self):
		self.clear()
		self.mainbatch.draw()
		return event.EVENT_HANDLED

	def on_key_press(self):
		return event.EVENT_HANDLED

	def on_key_release(self):
		return event.EVENT_HANDLED

