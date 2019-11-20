class DequeueImplementation:

	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.insert(0, item)

	def addRear(self, item):
		self.items.append(item)

	def removeFront(self):
		x = self.items.pop(0)
		print("Removed item is: ",x)

	def removeRear(self):
		x = self.items.pop()
		print("Removed item is: ",x)

	def isEmpty(self):
		return self.items == []

	def size(self):
		print"Size of Dequeue is: ",len(self.items)
		print ''


s1 = DequeueImplementation()

while True:
	x = int(input(" Press 1 for insert at front\n Press 2 for insert at rear\n Press 3 for remove from front\n Press 4 for remove from front\n\
	Press 5 to check dequeue is empty or not\n Press 6 for size of dequeue:\n "))
	if (x == 1):
		item = input("Enter Element: ")
		s1.addFront(item)
	elif(x == 2):
		item = input("Enter Element: ")
		s1.addRear(item)
	elif (x == 3):
		s1.removeFront()
	elif (x == 4):
		s1.removeRear()
	elif(x == 5):
		print(s1.isEmpty())

	elif(x ==6):
		s1.size()
	else:
		print("Wrong Input!!")