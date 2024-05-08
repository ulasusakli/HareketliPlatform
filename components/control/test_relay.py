## IMPORTS
import time
from motorModule import RobotController

# Create an instance of the RobotController
controller = RobotController()

# Turn on the relay for 2 seconds
controller.relay_on(2)

time.sleep(2)

# Turn off the relay for 2 seconds
controller.relay_off(2)

time.sleep(2)