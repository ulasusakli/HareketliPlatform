import random
from robot_controller import RobotController #Güncellencek
from time import sleep

# Create an instance of RobotController
controller = RobotController() #Güncellencek

def test_move():

    test_move = {'motor1': 43, 'motor2': 65, 'motor3': 30}
    print("TEST MOVE")
    controller.control_motors({1: ('cw', test_move['motor1']),
                            2: ('cw', test_move['motor2']),
                            3: ('cw', test_move['motor3'])})
    sleep(1)  # Delay for 2 seconds

    controller.control_motors({1: ('ccw', test_move['motor1']),
                            2: ('ccw', test_move['motor2']),
                            3: ('ccw', test_move['motor3'])})
    sleep(1)  # Delay for 2 seconds


def position_move():

    initial_to_object = {'motor1': 43, 'motor2': 65, 'motor3': 30}
    object_to_final  = {'motor1': 43, 'motor2': 65, 'motor3': 30}

    print("******Position Move********")
    controller.control_motors({1: ('cw', initial_to_object['motor1']),
                            2: ('cw', initial_to_object['motor2']),
                            3: ('cw', initial_to_object['motor3'])})
    sleep(1)  # Delay for 2 seconds

    # Activate the relay when the platform reaches Pos1, Pos2, or Pos3
    print("Activating the relay...")
    controller.relay_on(2)

    print("Second Move")
    controller.control_motors({1: ('ccw', object_to_final['motor1']),
                            2: ('ccw', object_to_final['motor2']),
                            3: ('ccw', object_to_final['motor3'])})
    sleep(1)  # Delay for 2 seconds

    # Deactivate the relay when the platform reaches the target position
    print("Deactivating the relay...")
    controller.relay_off(2)

#****Main File****

test_move()
#position_move()