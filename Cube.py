import math
class Cube():
    def __init__(self):
        self.centre = [0,0,0]
        self.position = [0,0,0]
        self.points = [[1,1,1],[1,1,-1],[-1,1,-1],[-1,1,1],
                      [1,-1,1],[1,-1,-1],[-1,-1,-1],[-1,-1,1]]
        self.edges = [[1-1,2-1],[2-1,3-1],[3-1,4-1],[4-1,8-1],[8-1,7-1],[7-1,6-1],[6-1,5-1],[5-1,8-1],[5-1,1-1],[6-1,2-1],[7-1,3-1],[4-1,1-1]]
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

    def posX(self, step):
        self.position[0] += step

    def posY(self, step):
        self.position[1] += step

    def posZ(self, step):
        self.position[2] += step

    def pos(self):
        return self.position

    def abs_pos(self):
        points = []
        for point in range(len(self.points)):
            tmp_point = []
            tmp_point.append(self.points[point][0] + self.position[0])
            tmp_point.append(self.points[point][1] + self.position[1])
            tmp_point.append(self.points[point][2] + self.position[2])
            points.append(tmp_point)
        return points