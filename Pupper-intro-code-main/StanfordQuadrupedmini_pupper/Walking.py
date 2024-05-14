#!/usr/bin/env python3

from src.MovementGroup import MovementGroups
from src.MovementScheme import MovementScheme

def move():
    move = MovementGroups()
    
    move.move_forward()

    MovementLib = move.MovementLib

    movementCtl = MovementScheme(MovementLib)

    movementCtl.runMovementScheme()
    print("why")
if __name__ == "__main__":
    move()
    print("done")
