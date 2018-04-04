import appex, ui
import random

min = 1
max = 20

def roll(sender):
		val = random.randint(min, max)
		sender.superview['result_label'].text = str(val)

def reset(sender):
	sender.superview['result_label'].text = ""


v = ui.View(frame=(0, 0, 300, 110))

label = ui.Label(
	frame=(150, 0, 140, 100),
	flex='lwh',
	font=('<System>', 50),
	alignment=ui.ALIGN_CENTER,
	name='result_label')
v.add_subview(label)

button = ui.Button(
	title='Roll d20',
	font=('<System>', 24),
	flex='lwh',
	action=roll,
	name='button_label')
button.frame = (20, 25, 70, 50)
v.add_subview(button)

appex.set_widget_view(v)
