#!/usr/bin/env python3

from src.MovementGroup import MovementGroups
from src.MovementScheme import MovementScheme

def move():
    move = MovementGroups()
    
    move.move_left()
    print("move left")
    MovementLib = move.MovementLib

    movementCtl = MovementScheme(MovementLib)
    
    movementCtl.runMovementScheme()

if __name__ == "__main__":
    move()
    print("done")
