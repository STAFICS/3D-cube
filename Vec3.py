import math
class Vec3():
	"""Homogeneous point, vector"""
	def __init__(self, x, y, z, w = 1):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	def __str__(self):
		return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.w)
 
	def mulS(self, scalar):
		self.x = x * scalar
		self.y = y * scalar
		self.z = z * scalar

	def add(self, v1, v2):
		return Vec3(v1.x + v2.x,
					v1.y + v2.y,
					v1.z + v2.z)

	def getLen(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def norm(self):
		self.x /= getLen(self.x)
		self.y /= getLen(self.y)
		self.z /= getLen(self.z)

	def vec(self):
		return [[self.x], [self.y], [self.z], [self.w]] 