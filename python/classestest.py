class ye:
	def __init__(self, num):
		self.x = num

	def kick(self):
		print(self.x)

yeye = []
for i in range(3):
	yeye.append(ye(i))

for i in range(len(yeye)):
	yeye[i].kick()
