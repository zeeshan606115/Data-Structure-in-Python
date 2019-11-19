class DecimalToBinary:

	def __init__(self):
		self.items = []

	def push(self, item):	
		self.items.append(item)
		
	def isEmpty(self):
		return self.items == []

	def pop(self):
		self.items.pop()

	def baseConvertor(self, num):
		while num > 0:
			rem = num % 2
			self.push(rem)
			num = num // 2

		binString = ""
		while not self.isEmpty():
			binString = binString + str(self.items.pop())

		print "Binary Value is: ",binString

c  = DecimalToBinary()
decimalValue = int(input("Enter decimal value to convert: "))
c.baseConvertor(decimalValue)