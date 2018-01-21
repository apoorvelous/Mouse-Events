#To record mouse events


from pynput.mouse import Listener
import time

flag_move = 0
flag_scroll = 0

mouse_events = {
	'moves':0,
	'clicks':0,
	'scrolls':0
}

#To record moves
def on_move(x, y):
	global flag_move
	flag_move = 1
	global flag_scroll
	if flag_scroll == 1:
		data = open("Mouse_Events.txt", 'a+')
		mouse_events['moves'] = mouse_events['moves'] + 1
		mouse_events['scrolls'] = mouse_events['scrolls'] + 1
		data.write("\nMoves - %d" %mouse_events['moves'])
		data.write("\nscrolls - %d" %mouse_events['scrolls'])
		data.close()
		flag_scroll = 0

#To record clicks		
def on_click(x, y, button, pressed):
	global flag_move
	if flag_move == 1 and pressed == 1:
		data = open("Mouse_Events.txt", 'a+')
		mouse_events['clicks'] = mouse_events['clicks'] + 1
		mouse_events['moves'] = mouse_events['moves'] + 1
		data.write("\nMoves - %d" %mouse_events['moves'])
		data.write("\nclicks - %d" %mouse_events['clicks'])
		data.close()
		flag_move = 0
		
	elif pressed == 1:
		data = open("Mouse_Events.txt", 'a+')
		mouse_events['clicks'] = mouse_events['clicks'] + 1
		data.write("\nclicks - %d" %mouse_events['clicks'])
		data.close()
		time.sleep(1)
		
#To record scrolls
def on_scroll(x, y, dx, dy):
	global flag_scroll
	flag_scroll = 1

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
	listener.join()
