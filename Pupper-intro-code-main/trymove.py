from MovementScheme import Movements
from MovementGroup import MovementGroups  # Import MovementGroups class from your module

# Create an instance of MovementGroups
movement_controller = MovementGroups()

# Call the move_forward method to make the Mini Pupper move forward
movement_controller.move_forward()

# Optionally, you can print a message to confirm the movement
print("Mini Pupper is moving forward.")