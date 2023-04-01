# class book:

# 	def __init__(self,price):
# 		self.price = price

# 	def __add__(self,other):
# 		return self.price + other.price

# b1 = book(200)
# b2 = book(300)

# print(b1 + b2)



class demo:

	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __add__(self,other):
		n = self.a + self.b
		m = other.a + other.b
		print(n)
		print(m)
		return n + m

	def __gt__(self,other):
		n = self.a + self.b
		m = other.a + other.b
		if n<m:
			return True
		else:
			return False
			
	def __str__(self):
		return '{} {}'.format(self.a, self.b)
		# return self.a, self.b  # non string type tuple


b1 = demo(2,8)
# b2 = demo(3,5)
# b3 = b1+b2
# print(b3)

print(b1)



