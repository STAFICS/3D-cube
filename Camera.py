from Vec3 import Vec3
import numpy as np

class Camera():
	def __init__(self):
		self.position = Vec3(0,0,-1)
		self.left = 	Vec3(1,0,0)
		self.up = 		Vec3(0,1,0)
		self.forward = 	Vec3(0,0,1)

	def pos(self, dx, dy, dz):
		self.position.x += dx
		self.position.y += dy 
		self.position.z += dz


	def rotX(self, angle):
		rad = np.pi / 180 * angle;
		T = np.array([[1, 0, 0, 0],
				[0, np.cos(rad), -np.sin(rad), 0],
				[0, np.sin(rad), np.cos(rad), 0],
				[0, 0, 0, 1]])
		forward = 	T.dot(np.array(self.forward.vec()))
		up = 	T.dot(np.array(self.up.vec()))	
		self.forward = Vec3(forward[0][0], forward[1][0], forward[2][0])
		self.up = Vec3(up[0][0], up[1][0], up[2][0])


	def rotY(self, angle):
		rad = np.pi / 180 * angle;
		T = np.array([[np.cos(rad), 0, np.sin(rad), 0],
				[0, 1, 0, 0],
				[-np.sin(rad), 0, np.cos(rad), 0],
				[0, 0, 0, 1]])
		forward = 	T.dot(np.array(self.forward.vec()))
		left = 	T.dot(np.array(self.left.vec()))	
		self.forward = Vec3(forward[0][0], forward[1][0], forward[2][0])
		self.left = Vec3(left[0][0], left[1][0], left[2][0])


	def rotZ(self, angle):
		rad = np.pi / 180 * angle;
		T = np.array([[np.cos(rad), -np.sin(rad), 0, 0],
				[np.sin(rad), np.cos(rad), 0, 0],
				[0, 0, 1, 0],
				[0, 0, 0, 1]])
		left = 	T.dot(np.array(self.left.vec()))
		up = 	T.dot(np.array(self.up.vec()))	
		self.left = Vec3(left[0][0], left[1][0], left[2][0])
		self.up = Vec3(up[0][0], up[1][0], up[2][0])


	def cam_pos(self, obj):
		T = np.array(	[[self.left.x,		self.left.y,	self.left.z,	self.position.x],
						 [self.up.x,		self.up.y,		self.up.z,		self.position.y],
						 [self.forward.x,	self.forward.y,	self.forward.z,	self.position.z],
						 [0,				0,				0,				1]]
					)
		Tinv = np.linalg.inv(T)
		obj.camera = []
		for point in obj.world:
			coord_cam = Tinv.dot(np.array(point.vec()))
			obj.camera.append(Vec3(coord_cam[0][0], coord_cam[1][0], coord_cam[2][0]))
		