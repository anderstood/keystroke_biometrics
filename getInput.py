# you type "once upon a time", it returns the duration between strokes

import Tkinter
from time import time

sample = "once upon a time"
sample_length = len(sample)
stroke_times = [x for x in [range(sample_length)]][0] #init
delta_times = stroke_times #init
boolType = True #False if user made a mistake
i=0

def key(event):
	global i 
	global e, master
	global boolType
	if event.char == '\r':
		e.unbind("<Key>")
		return
	end_time = time()
	if str(event.char)<>sample[i]:
		boolType = False
		print "poor looser! PRESS Enter"	
	stroke_times[i]=end_time-start_time #date of stroke
	i+=1

def quit(event):
	global i
	global e, master
	global stroke_times, delta_times
	e.destroy()
	master.destroy()
	delta_times = [x-y for x,y in zip(stroke_times[1:],stroke_times[:-1])]
	i = 0
	stroke_times = [x for x in [range(sample_length)]][0]
	if len(delta_times)<>sample_length-1:
		print "you FAILED!! go back to school"
	#return delta_times

start_time = end_time = 0


def getinput():
	global e, master
	global boolType
	master = Tkinter.Tk()
	e = Tkinter.Entry(master)
	e.pack()
	e.focus_set()		
	e.bind("<Key>", key)
	e.bind("<Return>",quit)
	print "___________________________________________"
	print "TYPE : 'once upon a time'"
	start_time = time()
	Tkinter.mainloop()

	if delta_times.count(1)<>0 or boolType == False :
		boolType = True
		return getinput()
	else:
		return delta_times



