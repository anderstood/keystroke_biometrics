# identification of how is typing (requires of course having run "learning.py" before!)

import os
import numpy as np
import pickle
import getInput

def main():
	data2check = np.matrix(getInput.getinput())

	list_of_files = [file for file in os.listdir("./users/") if file.lower().endswith(".pickle")]
	user = []
	userData = []
	userDiff = [list([]) for _ in xrange(len(list_of_files))]

	for file in list_of_files:
		username = file[:-7]
		user.append(username)
		data = pickle.load(open('./users/' + file,'r'))
		userData.append(np.matrix(data))

	for userI in range(len(user)):
		for test in userData[userI]:
			#print user[userI]
			#print np.sum(np.power(abs(test-data2check),2))
			#print test
			userDiff[userI].append(np.sum(np.power(abs(test-data2check),2)))

	userDiffSum = []
	for userI in range(len(user)):
		userDiffSum.append(np.sum(userDiff[userI]))
	userDiffSumNorm = userDiffSum/min(userDiffSum)

	userDiffSumNormSorted = userDiffSumNorm[:]
	userDiffSumNormSorted.sort()
	top3 = userDiffSumNormSorted[:3]
	for i in range(3):
		pos = list(userDiffSumNorm).index(top3[i])
		print user[pos] + '\t' + str(1/userDiffSumNorm[pos])

	print "__________________\nhey, i know who you are! you're " + user[np.argmin(userDiffSum)] + " ;)"
