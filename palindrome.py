class DequeueImplementation:

	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.insert(0, item)

	def addRear(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop(0)
	
	def removeRear(self):
		return self.items.pop()
		 

	def size(self):
		return len(self.items)


	def palindrome(self, astring):

		for ch in astring:
			self.addRear(ch)

		stillEqual = True

		while self.size() > 1 and stillEqual:
			first = self.removeFront()
			last = self.removeRear()

			if first != last:
				stillEqual = False

		return stillEqual



s2 = DequeueImplementation()

s = raw_input("Enter string: ")
x = s2.palindrome(s)
if (x == True):
	print "Given string is palindrome"

else:
	print "Given string is not palindrome"


