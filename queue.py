class QueueImplementation:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		x = self.items == []
		if x == True:
			print "Queue is Empty\n"

		else:
			print "Queue is not Empty\n"

	def enqueue(self, item):
		return self.items.insert(0, item)

	def dequeue(self):
		x = self.items.pop()
		print"Removed element was: ",x
		print""

	def size(self):
		x = len(self.items)
		print "Size of queue is: ",x
		print""

s1 = QueueImplementation()

while True:
	x = int(input(" Press 1 for insert\n Press 2 for remove\n Press 3 for check\n Press 4 for size:\n "))
	if (x == 1):
		item = input("Enter Element: ")
		s1.enqueue(item)
	elif(x == 2):
		s1.dequeue()
	elif (x == 3):
		s1.isEmpty()
	elif (x == 4):
		s1.size()
	else:
		print("Wrong Input!!")