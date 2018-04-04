import appex
import ui
import random
from time import time

startTime = 0
isRunning = False


def start(sender):
	global isRunning
	global startTime

	if isRunning:
		now = time() - startTime
		secs = now % 60.0
		lightSpeed = 340
		distance = secs * lightSpeed

		sender.superview['button_label'].title = "►"
		sender.superview['result_label'].title = str(int(distance)) + "m"
		isRunning = False

	else:
		sender.superview['button_label'].title = "◼"
		sender.superview['result_label'].title = "Counting"

		startTime = time()
		isRunning = True


def reset(sender):
	global startTime
	global isRunning

	startTime = 0
	isRunning = False
	sender.superview['result_label'].title = ""


v = ui.View(frame=(0, 0, 300, 110))

label = ui.Button(
	frame=(150, 0, 150, 100),
	flex='lwh',
	font=('<System>', 24),
	alignment=ui.ALIGN_RIGHT,
	action=reset,
	name='result_label')
v.add_subview(label)

button = ui.Button(
	title='►',
	font=('<System>', 24),
	flex='rwh',
	action=start,
	name='button_label')
button.frame = (20, 25, 50, 50)
v.add_subview(button)

appex.set_widget_view(v)
