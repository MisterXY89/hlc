############################################# 
# 
# @author Tilman Kerl
# @version 2019.01.15
#
# Crack higher lower game via selenium 
# and brute force learning.
# For further informations see:
# https://github.com/MisterXY89/hlc
# 
############################################# 


# START IMPORT #
import pickle
from hlc import *
# END IMPORT #


def main():
	# i know it's dump, but it works
	for x in range(0,100000):		
		learn()	
		# nice to know output, not necessary
		print("length: %s @x: %s"%(len(pickle.load(open("hlc.data","rb"))),x))
		print(30*("-"))


def learn():
	print("start")
	hlc = HLC()
	hlc.start()
	# the while loop gets interrupted when the game ends 
	# and an error is thrown, because the program cannot 
	# find any of the necessary html elements
	# HLC methods are explained in hlc.py
	while True:
		try:
			hlc.left()
		except Exception as e:
			hlc.stop()
			return 'exit'
		if hlc.knowsBoth():
			hlc.next()
		else:
			hlc.guess()

if __name__ == '__main__':
	main()
