# Nathan Reline
# NESpi CLUI

import curses
import time

#initialize curses ######
stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(1)
#########################

stdscr.addstr(0,0, "Current Mode: Typing mode", curses.A_REVERSE)
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
stdscr.addstr("pretty colors",curses.color_pair(1)) # change 'pretty colors' by changing init_pair(1)
stdscr.refresh()

pad = curses.newpad(100,100)
for y in range(0, 100):
	for x in range(0, 100):
		try:
			pad.addch(y,x,ord('a') + (x*x+y*y) % 26)
		except curses.error:
			pass
pad.refresh(0,0,5,5,20,75)


# user input #############

while 1:
	c = stdscr.getch()
	if c == ord('h'):
		print("hello world")
	elif c == ord('q'):
		break	
	elif c == curses.KEY_HOME:
		x = y = 0

###########################

curses.echo() # enable echoing of characters

##########################

s = stdscr.getstr(0,0,15) # get 15 characters starting from beginning of top line
print(s)

##########################



time.sleep(10) # 1 = one second



# terminate curses ######
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
#########################
