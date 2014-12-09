from pyglet import resource
import os

resource.path.extend(os.path.dirname(os.path.abspath(__file__)))
resource.reindex()
playerSprite = resource.image('player.png')
enemySprite = resource.image('enemy.png')
enemySFX = resource.media('bass.wav', streaming=False)