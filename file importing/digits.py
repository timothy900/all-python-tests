# testing how to use 'import'

class Digit:

	def __init__(self, x):
		self.x = x
		self.a = 10
		for i in range(self.x):
			self.a += 1

	def showIt(self):
		print(self.a)
