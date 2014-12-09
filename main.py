from game import Game
from pyglet import clock, app

gamerun = Game(800, 600)
gamerun.initialize()

if __name__ == "__main__":
	clock.schedule_interval(gamerun.update, 1/120.0)
	app.run()

