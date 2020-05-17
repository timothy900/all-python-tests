#neural network

import random

class NeuralNetwork:
	
	def __init__(self, layer1,layer2,layer3):
		# Parameters : layer1 is amount of neurons in the first layer etc.

		l1 = [] # layer 1 is the input layer
		self.l1 = l1
		l2 = [] # layer 2 is the hidden layer
		self.l2 = l2
		l3 = [] # layer 3 is the output layer
		self.l3 = l3

		# set random weights to each neuron
		for n in range(layer1):
			l1.append(random.randint(-10, 10))
		for n in range(layer2):
			l2.append(random.randint(-10, 10))
		for n in range(layer3):
			l3.append(random.randint(-10, 10))

'''
	def feedforward(self, feed):
		sums = []
		# the length of the imput must equal the length of the input layer
		for neuron in self.l1:
			for inp in feed: 
				s = neuron * inp
				sums.append(s)
		return sums
'''


nn = NeuralNetwork(5, 5, 1)

feed = [0, 1, 1, 0, 1]

#print(nn.feedforward(feed))

print(nn.l1, nn.l2, nn.l3)
