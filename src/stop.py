#Objective of this project is to implement 20 20 20 rule for better vision.
#We are not using notification methods here because , coders like me usually ignore them
#This can have poor effects on your vision and eyesight

import time,sys
import pythoncom, pyHook 
import pyglet


COUNTDOWN = int(sys.argv[1]) 
# COUNTDOWN = 5 

window = pyglet.window.Window(fullscreen=True)
class Timer(object):
    def __init__(self):
        m,s = divmod(COUNTDOWN,60)
        self.start =  '%02d:%02d' % (m, s) 
        self.label = pyglet.text.Label(self.start, font_size=60,
                                       x=window.width//2, y=window.height//2,
                                       anchor_x='center', anchor_y='center')
        self.reset()

    def reset(self):
        self.time = COUNTDOWN
        self.running = True
        self.label.text = self.start
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time -= dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            # print m,s
            if s < 5:
                self.label.color = (180, 0, 0, 255)
            if int(m)==0.0 and int(s)==0:
                window.clear()
                window.close()

timer = Timer()

@window.event
def on_draw():
    window.clear()
    timer.label.draw()


def close(event):
    window.close()
	
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE:
        return pyglet.event.EVENT_HANDLED


def blackwindow():
	pyglet.clock.schedule_interval(timer.update, 1)
	pyglet.app.run()

def uMad(event):
  return False

def stopworking():

	hm = pyHook.HookManager()
	hm.MouseAll = uMad
	hm.KeyAll = uMad
	hm.HookMouse()
	hm.HookKeyboard()
	t0 = time.clock()
	blackwindow()
	while time.clock()-t0 < COUNTDOWN:
		pythoncom.PumpWaitingMessages()

# blackwindow()
stopworking()


