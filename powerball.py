"""
Program: Powerball.py
Author: Robert 4/26/2021

"""

from breezypythongui import EasyFrame

import random

class PowerBall(EasyFrame):

	def __init__(self):
		EasyFrame.__init__(self, title = "Powerball FIVE", width = 300, height = 300, background = "lightblue")
		self.addLabel(text = "Powerball FIVE", row = 0, column = 0, columnspan = 5, sticky = "NSEW", background = "lightblue")

		self.numOne = self.addLabel(text = "First draw", row = 1, column = 0, background = "red")
		self.numOne = self.addIntegerField(value = 0, row = 1, column = 1)

		self.numTwo = self.addLabel(text = "Second draw", row = 2, column = 0, background = "red")
		self.numTwo = self.addIntegerField(value = 0, row = 2, column = 1)

		self.numThree = self.addLabel(text = "Third draw", row = 3, column = 0, background = "red")
		self.numThree = self.addIntegerField(value = 0, row = 3, column = 1)

		self.numFour = self.addLabel(text = "Fourth draw", row = 4, column = 0, background = "red")
		self.numFour = self.addIntegerField(value = 0, row = 4, column = 1)

		self.numFive = self.addLabel(text = "Fifth draw", row = 5, column = 0, background = "red")
		self.numFive = self.addIntegerField(value = 0, row = 5, column = 1)

		self.powerNum = self.addLabel(text = "POWERBALL DRAWS!!!", row = 6, column = 0, sticky = "NSEW", background = "green")
		self.powerNum = self.addIntegerField(value = 0, row = 6, column = 1, sticky = "NSEW")

		self.addButton(text = "Draws!", row = 7, column = 0, columnspan = 2, command = self.drawNum)

	def drawNum(self):
		"""Draws the numbers for the powerball"""
		numOne = random.randint(1, 69)		
		numTwo = random.randint(1, 69)
		numThree = random.randint(1, 69)
		numFour = random.randint(1, 69)
		numFive = random.randint(1, 69)
		powerNum = random.randint(1, 26)

		self.numOne.setNumber(numOne)
		self.numTwo.setNumber(numTwo)	
		self.numThree.setNumber(numThree)
		self.numFour.setNumber(numFour)
		self.numFive.setNumber(numFive)
		self.powerNum.setNumber(powerNum)

	
def main():
	PowerBall().mainloop()

main()
