from Vec3 import Vec3
import math

class Matrix():
	def __init__(self):
		pass

	def __str__(self):
		pass

	def mul(a, b):
		for i in range(0,4):
			for j in range(0,4):
				a[i][j] = (a[i][0] * b[0][j] +
									a[i][1] * b[1][j] +
									a[i][2] * b[2][j] +
									a[i][3] * b[3][j])

	def mulVec(matrix, vec):
		return Vec3(	matrix[0][0] * vec.x + matrix[0][1] * vec.y + matrix[0][2] * vec.z + matrix[0][3] * vec.w,
						matrix[1][0] * vec.x + matrix[1][1] * vec.y + matrix[1][2] * vec.z + matrix[1][3] * vec.w,
						matrix[2][0] * vec.x + matrix[2][1] * vec.y + matrix[2][2] * vec.z + matrix[2][3] * vec.w,
						matrix[3][0] * vec.x + matrix[3][1] * vec.y + matrix[3][2] * vec.z + matrix[3][3] * vec.w)

	def getRotationX(self, angle):
		rad = math.pi / 180 * angle
		return 	[
				[1, 0, 0, 0],
				[0, math.cos(rad), -math.sin(rad), 0],
				[0, math.sin(rad), math.cos(rad), 0],
				[0, 0, 0, 1],
				]

	def getRotationY(self, angle):
		rad = math.pi / 180 * angle;
		return 	[
				[math.cos(rad), 0, math.sin(rad), 0],
				[0, 1, 0, 0],
				[-math.sin(rad), 0, math.cos(rad), 0],
				[0, 0, 0, 1],
	    		]

	def getRotationZ(self, angle):
		rad = math.pi / 180 * angle;
		return 	[
				[math.cos(rad), -math.sin(rad), 0, 0],
				[math.sin(rad), math.cos(rad), 0, 0],
				[0, 0, 1, 0],
				[0, 0, 0, 1],
				]

	def getTranslation(self, dx, dy, dz):
		return 	[
				[1, 0, 0, dx],
				[0, 1, 0, dy],
				[0, 0, 1, dz],
				[0, 0, 0, 1],
				]

	def getScale(self, sx, sy, sz):
		return 	[
				[sx, 0, 0, 0],
				[0, sy, 0, 0],
				[0, 0, sz, 0],
				[0, 0, 0, 1],
				]
