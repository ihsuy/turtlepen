import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


# ==== Meta data ==== 
STEPSIZE = 0.01 # distance between each consecutive point

FIGSIZE = (40, 40) # output drawing figure size
MARKERSIZE = 5 # point marker size
MARKERCOLOR = 'k' # point marker color

# ==== Action blocks ====

class Action(ABC):
    # abstract base class for making action blocks
    @abstractmethod
    def __init__(self,):
        # a concrete action block must implement its own initializer
        # in order to recieve the proper parameters to perform the action
        pass
    
    @abstractmethod
    def apply(self, tt):
        # a concrete action block must implement its own apply method
        # that defines the action that will be applied on a Turtle
        pass
    
    def __call__(self, tt):
        self.apply(tt)

class Repeat(Action):
    # repeats given $actions for $n times
    def __init__(self, n, actions):
        self.n = n
        self.actions = actions
    
    def apply(self, tt):
        for _ in range(self.n):
            for action in self.actions:
                action(tt)

class Forward(Action):
    # move turtle forward (along turtle's current direction) 
    # for $steps steps. When $steps is negative, 
    # moves Turtle backward.
    def __init__(self, steps):
        self.steps = steps
    
    def apply(self, tt):
        sine, cosine = np.sin(tt.dr), np.cos(tt.dr)
        dx, dy = sine*STEPSIZE, cosine*STEPSIZE

        direction = 1 if self.steps>=0 else -1
        for _ in range(abs(self.steps)):
            tt.move(direction*dx,direction*dy)

class Rotate(Action):
    # changes the direction that the turtle moves toward
    def __init__(self, degrees):
        self.degrees = degrees
    
    def apply(self, tt):
        tt.rotate(self.degrees)
        
class BackToCenter(Action):
    # resets Turtle's coordinate to (0,0), 
    # leaves Turtle's direction unchanged
    def __init__(self):
        pass
    
    def apply(self, tt):
        tt.reset()
        
class PenUp(Action):
    # pauses Turtle from leaving any trace when moving
    def __init__(self):
        pass
    
    def apply(self, tt):
        tt.pen_up()

class PenDown(Action):
    # reverses the active effects of PenUp
    def __init__(self):
        pass
    
    def apply(self, tt):
        tt.pen_down()
        
# ==== turtle ====
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

        
def visualize_trace(tt):
    # given Turtle $tt, this method visualize its trace
    xs, ys = list(zip(*tt.trace))
    plt.figure(figsize=FIGSIZE)
    plt.plot(xs, ys, '.', markersize=MARKERSIZE, color=MARKERCOLOR)
    plt.axis('off')
    plt.show()