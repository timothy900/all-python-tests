import numpy as np

inputs = [1, 2, 3]

weights = [ [3, 2, .5],
			[.5, 6, 1],
			[2.5, 1, 2] ]

biases = [2.5, 1, .5]

output = np.dot(weights, inputs) #+ biases

print(output)
			