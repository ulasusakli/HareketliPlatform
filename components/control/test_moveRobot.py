## IMPORTS
import time
from motorModule import RobotController


# Create an instance of the RobotController
controller = RobotController()

# Define commands for each motor
commands_cw = {
    1: ('cw', 45),   # Motor 1, rotate clockwise 45 degrees
    2: ('cw', 45),  # Motor 2, rotate counterclockwise 90 degrees
    3: ('cw', 45)   # Motor 3, rotate clockwise 180 degrees
}

# Execute the motor commands
controller.control_motors(commands_cw)
print("Saat Yönünde Döndü")

# Turn on the relay for 2 seconds
controller.relay_on(2)

time.sleep(2)

# Define commands for each motor
commands_ccw = {
    1: ('ccw', 45),   # Motor 1, rotate clockwise 45 degrees
    2: ('ccw', 45),  # Motor 2, rotate counterclockwise 90 degrees
    3: ('ccw', 45)   # Motor 3, rotate clockwise 180 degrees
}

# Execute the motor commands
controller.control_motors(commands_ccw)
print("Saat Yönünün Tersine Döndü")

# Turn off the relay for 2 seconds
controller.relay_off(2)

time.sleep(2)