from math import floor
from decimal import Decimal
from sys import stdout

class Progressbar:
    def __init__(self, operations: int, width: int = 30, title: None | str = None) -> None:
        
        if operations < 0:
            raise TypeError("width cannot be less than zero")
        
        self.width = width if operations >= width else operations
        
        dec = Decimal(self.width / (operations + 1))
        
        self.stepSize = dec.quantize(Decimal('1e-28'), rounding="ROUND_FLOOR")
        self.place = 0
        self.lastplace = self.place - 1
        self.steps = 0
        
        if title:
            print(title)
        stdout.write("[%s]" % (" " * self.width))
        stdout.flush()
        stdout.write("\b" * (self.width + 1))
        
    def update(self):
        self.place += 1
        self.steps += self.stepSize
        
        if floor(self.steps) > self.lastplace:
            
            stdout.write("-")
            stdout.flush()
            self.lastplace = floor(self.steps)
    
    def done(self):
        stdout.write("\n")
        
"""
# example:
import time
j = 200

bar = Progressbar(j, width=60, title="This is a test bar...")

for i in range(j):
    # do actions here
    time.sleep(.01)
    bar.update()
    
bar.done()
"""