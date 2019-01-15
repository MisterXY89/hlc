
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
import time
import pickle
from selenium import webdriver
# END IMPORT #


# the code is pretty much self-explaining
class HLC():
	""" hlc = HigherLower Crack"""
	def __init__(self):		
		self.driver = webdriver.Firefox()
		self.valueDict = {}
		self.dataFile = "hlc.data"
		self.termsSelector = "term-keyword__keyword"
		self.valuesSelector = "term-volume__volume"
		self.higherButtonSelector = "term-actions__button--higher"
		self.lowerButtonSelector = "term-actions__button--lower"
		self.startButtonSelector = "game-button--start"
		self.valueLeft = 0
		self.termRight = ""
		self.termLeft = ""
		self.score = 0
		self.load()


	def start(self):
		self.driver.set_window_position(0, 0)
		self.driver.set_window_size(600, 600)
		self.driver.get("https://www.higherlowergame.com/")
		assert "The Higher Lower Game" in self.driver.title
		startButton = self.driver.find_elements_by_class_name(self.startButtonSelector)[0]
		startButton.click()

	# get value and term from the left side
	def left(self):
		terms = []
		values = []		
		time.sleep(2) # need to pause, because of the javascript animations
		terms = self.driver.find_elements_by_class_name(self.termsSelector)		
		self.termLeft = str(terms[0].text)[1:][:-1]
		self.termRight = str(terms[1].text)[1:][:-1]
		values = self.driver.find_elements_by_class_name(self.valuesSelector)
		self.valueLeft = int(values[0].text.replace(",",""))
		self.update()
		self.score += 1

	def update(self,right=False):
		if not right:
			if not self.termLeft in self.valueDict.keys():
				updateDict = {self.termLeft: self.valueLeft}
				self.valueDict.update(updateDict)
				self.store()
				print("updating: %s"%updateDict)
		elif right:
			if not self.termRight in self.valueDict.keys():
				updateDict = {self.termRight: self.valueRight}
				self.valueDict.update(updateDict)
				self.store()
				print("updating: %s"%updateDict)


	# get value and term from the right side
	# important in the learning phase -> even if the programm guessed wrong,
	# it stil learns the correct value
	def right(self):
		values = []
		time.sleep(1) # need to pause, because of the javascript animations
		values = self.driver.find_elements_by_class_name(self.valuesSelector)
		self.valueRight = int(values[1].text.replace(",",""))
		self.update(True)

	def triggerHigher(self):
		higherButton = self.driver.find_elements_by_class_name(self.higherButtonSelector)[0]	
		higherButton.click()
		self.right()

	def triggerLower(self):
		lowerButton = self.driver.find_elements_by_class_name(self.lowerButtonSelector)[0]	
		lowerButton.click()
		self.right()

	def store(self):
		try: 
			pickle_out = open(self.dataFile,"wb")
			pickle.dump(self.valueDict, pickle_out)
			pickle_out.close()
			return True
		except Exception as e:
			print(e)
			return False

	def load(self):
		try:
			pickleIn = open(self.dataFile, "rb")
			self.valueDict = pickle.load(pickleIn)
			pickleIn.close()
		except Exception as e:
			print(e)
			return False

	# !IMPORTANT! exec only if knowsBoth() == True 
	def next(self):
		print("%s vs %s" %(self.termLeft, self.termRight))
		if (self.valueLeft 	<= self.valueDict[self.termRight]):			
			self.triggerHigher()
		else:
			self.triggerLower()

	# if program does not know value of both terms call this method
	# it will trigger an action depending on the known left value
	def guess(self):		
		print("%s vs %s" %(self.termLeft, self.termRight))
		if self.valueLeft > 350000:
			self.triggerLower()
		else:
			self.triggerHigher()

	def knowsBoth(self):
		if self.termRight in self.valueDict.keys():
			return True
		return False

	# stops selenium driver and stores again the dict. 
	# the storing is not really necessary but safety first :D
	def stop(self):
		print("Score: %s"%self.score)
		self.store()
		self.driver.close()
