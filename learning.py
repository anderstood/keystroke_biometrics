# learns how you type

import pickle
import numpy as np
import getInput


username = raw_input("your name:\t")

data = []
for i in range(3):
	data.append(getInput.getinput())

pickleName = username + '.pickle'
pickle.dump(data,file(pickleName,'w'))
