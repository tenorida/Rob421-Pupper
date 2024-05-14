#!/usr/bin/env python3

from src.MovementGroup import MovementGroups
from src.MovementScheme import MovementScheme

def move():
    move = MovementGroups()
    
    move.move_forward()
    print("move forward")
    MovementLib = move.MovementLib
    print("I don't work")
    movementCtl = MovementScheme(MovementLib)
    print("this sucks")
    movementCtl.runMovementScheme()
    print("why")
if __name__ == "__main__":
    move()
    print("done")
