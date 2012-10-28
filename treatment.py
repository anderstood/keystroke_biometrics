# identification of how is typing (requires of course having run "learning.py" before!)

import os
import numpy as np
import pickle
import getInput

def main():
	data2check = np.matrix(getInput.getinput())

	list_of_files = [file for file in os.listdir("./") if file.lower().endswith(".pickle")]
	user = []
	userData = []
	userDiff = [list([]) for _ in xrange(len(list_of_files))]

	for file in list_of_files:
		username = file[:-7]
		user.append(username)
		data = pickle.load(open(file,'r'))
		userData.append(np.matrix(data))

	for userI in range(len(user)):
		for test in userData[userI]:
			#print user[userI]
			#print np.sum(np.power(abs(test-data2check),2))
			#print test
			userDiff[userI].append(np.sum(np.power(abs(test-data2check),2)))
	print user
	print userDiff

	userDiffSum = []
	for userI in range(len(user)):
		userDiffSum.append(np.sum(userDiff[userI]))

	print "__________________\nhey, i know who you are! you're " + user[np.argmin(userDiffSum)] + " ;)"
