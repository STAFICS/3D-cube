from Vec3 import Vec3
from Matrix import Matrix

def p(a):
	for i in a:
		print(i)

basis1 = [Vec3(1,0,0), Vec3(0,1,0), Vec3(0,0,1)]
basis2 = [Vec3(1,0,0), Vec3(0,1,0), Vec3(0,0,1)]
p(basis2)
for i in range(len(basis2)):
	basis2[i] = Matrix.mulVec(Matrix.getRotationX(45), basis2[i])
	basis2[i] = Matrix.mulVec(Matrix.getRotationY(45), basis2[i])
	basis2[i] = Matrix.mulVec(Matrix.getRotationZ(45), basis2[i])
print('')
p(basis2)
print('')
print( Matrix.mulVec([	[0.5000000000000001, 0.5000000000000001, -0.7071067811865476, 0],
						[-0.14644660940672627, 0.853553390593274, 0.5000000000000001, 0],
						[0.853553390593274, -0.14644660940672627, 0.5000000000000001, 0],
						[0,0,0,1]], Vec3(0.50000000000000, 0.500000000000000, -0.7071067811865476)))
