import math
from Vec3 import Vec3
import numpy as np

class Cube():
    def __init__(self):
        self.centre = Vec3(0,0,0)
        self.position = Vec3(0,0,0)
        self.points =  [Vec3(1,1,1),
                        Vec3(1,1,-1),
                        Vec3(-1,1,-1),
                        Vec3(-1,1,1),
                        Vec3(1,-1,1),
                        Vec3(1,-1,-1),
                        Vec3(-1,-1,-1),
                        Vec3(-1,-1,1)]
        self.world = self.points
        self.camera = []
        self.edges = [[0,1],[1,2],[2,3],[3,7],[7,6],[6,5],[5,4],[4,7],[4,0],[5,1],[6,2],[3,0]]
        self.perspective = []

    def rotZ(self, angle):
        radian = angle * math.pi / 180
        cosa = math.cos(radian)
        sina = math.sin(radian)
        for point in range(len(self.points)):
            x = self.points[point][0] * cosa - self.points[point][1] * sina
            y = self.points[point][0] * sina + self.points[point][1] * cosa
            self.points[point][0] = x
            self.points[point][1] = y

    def rotX(self, angle):
        radian = angle * math.pi / 180
        cosa = math.cos(radian)
        sina = math.sin(radian)
        for point in range(len(self.points)):
            y = self.points[point][1] * cosa - self.points[point][2] * sina
            z = self.points[point][1] * sina + self.points[point][2] * cosa
            self.points[point][1] = y
            self.points[point][2] = z

    def rotY(self, angle):
        radian = angle * math.pi / 180
        cosa = math.cos(radian)
        sina = math.sin(radian)
        for point in range(len(self.points)):
            z = self.points[point][2] * cosa - self.points[point][0] * sina
            x = self.points[point][2] * sina + self.points[point][0] * cosa
            self.points[point][2] = z
            self.points[point][0] = x

    def pos(self, dx, dy, dz):
        self.position.x += dx 
        self.position.y += dy 
        self.position.z += dz
        trans = np.array(  [[1, 0, 0, self.position.x],
                            [0, 1, 0, self.position.y],
                            [0, 0, 1, self.position.z],
                            [0, 0, 0, 1],]
                        )
        self.world = []
        for point in self.points:
            dot = np.array(point.vec())
            dot = trans.dot(dot)
            self.world.append(Vec3(dot[0][0],dot[1][0],dot[2][0],))


    def getPos(self):
        return self.position

    def abs_pos(self):
        points = []
        for point in range(len(self.points)):
            points.append(Vec3(self.points[point].x + self.position.x, self.points[point].y + self.position.y, self.points[point].z + self.position.z))
        return points


        # points = []
        # for point in range(len(self.points)):
        #     tmp_point = []
        #     tmp_point.append(self.points[point][0] + self.position[0])
        #     tmp_point.append(self.points[point][1] + self.position[1])
        #     tmp_point.append(self.points[point][2] + self.position[2])
        #     points.append(tmp_point)
        # return points
