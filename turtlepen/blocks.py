import numpy as np
from abc import ABC, abstractmethod

from turtlepen import configs

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
        dx, dy = sine*configs.STEPSIZE, cosine*configs.STEPSIZE

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
        

