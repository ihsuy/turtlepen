import numpy as np

class Turtle:
    # an object that keeps track of its position
    # while being moved by action blocks
    def __init__(self, x=0, y=0, d=0):
        self.trace = [(x,y)]
        self.x = x # x and y coordinate
        self.y = y
        self.d = d # degree
        self.dr = np.deg2rad(d)
        self._pen_down = True
    
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        if self._pen_down:
            self.trace.append((self.x, self.y))
    
    def rotate(self,dd):
        self.d += dd
        self.dr = np.deg2rad(self.d)
    
    def pen_up(self,):
        self._pen_down = False
    
    def pen_down(self,):
        self._pen_down = True
    
    def reset(self,):
        self.x, self.y = 0,0
