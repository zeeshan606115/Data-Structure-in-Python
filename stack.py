class Stack:
	def __init__(self):
		self.items = []

	def size(self):
		print()
		print("Size of stack is: ",len(self.items))
		print()

	def push(self, item):
		print()		
		self.items.append(item)
		print()

	def pop(self):
		print()
		print("Popped element is: ",self.items.pop())
		print()

	def peek(self):
		x = self.items[-1]
		print()
		print("Top element in stack is: ",x)
		print()

	

s1 = Stack()
while True:
	x = int(input(" Press 1 for push\n Press 2 for pop\n Press 3 for Peek\n Press 4 for size:\n "))
	if (x == 1):
		item = input("Enter Element: ")
		s1.push(item)
	elif(x == 2):
		s1.pop()
	elif (x == 3):
		s1.peek()
	elif (x == 4):
		s1.size()
	else:
		print("Wrong Input!!")