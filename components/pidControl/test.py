import random
from robot_controller import RobotController
from time import sleep

# Create an instance of RobotController
controller = RobotController()

print("First Move")
controller.control_motors({1: ('cw', 30),
                           2: ('cw', 30),
                           3: ('cw', 30)})
sleep(2)  # Delay for 2 seconds

# Activate the relay when the platform reaches Pos1, Pos2, or Pos3
print("Activating the relay...")
controller.relay_on(2)
    
print("Second Move")
controller.control_motors({1: ('ccw', 30),
                           2: ('ccw', 30),
                           3: ('ccw', 30)})
sleep(2)  # Delay for 2 seconds

# Deactivate the relay when the platform reaches the target position
print("Deactivating the relay...")
controller.relay_off(2)