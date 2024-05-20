import random
from robot_controller import RobotController
from time import sleep

# Create an instance of RobotController
controller = RobotController()

def move_to_position(position):
    # Define the initial position and target position
    initial_position = {'motor1': 0, 'motor2': 0, 'motor3': 0}
    target_position = {'motor1': 100, 'motor2': 100, 'motor3': 100}

    # Calculate the target position relative to Pos1, Pos2, or Pos3
    if position == 1:
        pos_position = {'motor1': 43, 'motor2': 65, 'motor3': 30}
    elif position == 2:
        pos_position = {'motor1': 30, 'motor2': 30, 'motor3': 30}
    elif position == 3:
        pos_position = {'motor1': 40, 'motor2': 40, 'motor3': 40}

    print(f"Position {position} Position: {pos_position}")

    # Calculate target position relative to the current position
    target_position_relative = {
        'motor1': target_position['motor1'] - pos_position['motor1'],
        'motor2': target_position['motor2'] - pos_position['motor2'],
        'motor3': target_position['motor3'] - pos_position['motor3']
    }

    sleep(2)  # Delay for 2 seconds

    # Activate the relay when the platform reaches Pos1, Pos2, or Pos3
    print("Activating the relay...")
    controller.relay_on(2)
    
    # Move from the specified position to the target position
    print(f"Moving from position {position} to target position...")
    controller.control_motors({
        1: ('cw', target_position_relative['motor1']),
        2: ('cw', target_position_relative['motor2']),
        3: ('cw', target_position_relative['motor3'])
    })
    sleep(2)  # Delay for 2 seconds

    # Deactivate the relay when the platform reaches the target position
    print("Deactivating the relay...")
    controller.relay_off(2)

    # Move from the target position back to the initial position
    print("Moving back to the initial position...")
    controller.control_motors({
        1: ('ccw', target_position['motor1']),
        2: ('ccw', target_position['motor2']),
        3: ('ccw', target_position['motor3'])
    })
    sleep(2)  # Delay for 2 seconds

move_to_position(1)
