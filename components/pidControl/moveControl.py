import random
from robot_controller import RobotController
from time import sleep

# Create an instance of RobotController
controller = RobotController()

def move_to_position(position):
    # Define the initial position and target position
    initial_position = {'motor1': 0, 'motor2': 0, 'motor3': 0}
    target_position = {'motor1': 32, 'motor2': 44, 'motor3': 55}

    # Define the positions for Pos1, Pos2, and Pos3
    pos1_position = {'motor1': 49, 'motor2': 56, 'motor3': 23}
    pos2_position = {'motor1': 50, 'motor2': 40, 'motor3': 27}
    pos3_position = {'motor1': 61, 'motor2': 31, 'motor3': 36}

    # Calculate the target position relative to Pos1, Pos2, or Pos3
    if position == 1:
        target_position_relative = {'motor1': 49, 'motor2': 56, 'motor3': 23}
    elif position == 2:
        target_position_relative = {'motor1': 49, 'motor2': 56, 'motor3': 23}
    elif position == 3:
        target_position_relative = {'motor1': 49, 'motor2': 56, 'motor3': 23}

    # Move from the initial position to the specified position
    print(f"Moving from initial position to position {position}...")
    controller.control_motors({1: ('cw', pos1_position['motor1']),
                               2: ('cw', pos1_position['motor2']),
                               3: ('cw', pos1_position['motor3'])})
    sleep(2)  # Delay for 2 seconds

    # Activate the relay when the platform reaches Pos1, Pos2, or Pos3
    print("Activating the relay...")
    controller.relay_on(2)
    
    # Move from the specified position to the target position
    print(f"Moving from position {position} to target position...")
    controller.control_motors({1: ('cw', target_position_relative['motor1']),
                               2: ('cw', target_position_relative['motor2']),
                               3: ('cw', target_position_relative['motor3'])})
    sleep(2)  # Delay for 2 seconds

    # Deactivate the relay when the platform reaches the target position
    print("Deactivating the relay...")
    controller.relay_off(2)


    # Move from the target position back to the initial position
    print("Moving back to the initial position...")
    controller.control_motors({1: ('ccw', target_position['motor1']),
                               2: ('ccw', target_position['motor2']),
                               3: ('ccw', target_position['motor3'])})
    sleep(2)  # Delay for 2 seconds

def reset_platform():
    print("Platform is resetting... Please Wait.")
    commands4_01 = {
        1: ('ccw', 15),
        2: ('ccw', 15),
        3: ('ccw', 15)  
        }
    controller.control_motors(commands4_01)
    time.sleep(1)
    
    # Motor 1 RESET
    print("Resetting motor 1...")
    commands4_11 = {
        1: ('ccw', 60)   
        }
    controller.control_motors(commands4_11)
    time.sleep(1)

    commands4_21 = {
        1: ('cw', 30)   
    }
    controller.control_motors(commands4_21)
    time.sleep(1)  

    # Motor 2 RESET
    print("Resetting motor 2...")
    commands4_12 = {
        2: ('ccw', 60) 
    }
    controller.control_motors(commands4_12)
    time.sleep(1)

    commands4_22 = {
        2: ('cw', 30)
    }
    controller.control_motors(commands4_22)
    time.sleep(1)

    # Motor 3 RESET
    print("Resetting motor 3...")
    commands4_13 = {  
        3: ('ccw', 60)   
    }
    controller.control_motors(commands4_13)
    time.sleep(1)  

    commands4_23 = {    
        3: ('cw', 30)     
    }
    controller.control_motors(commands4_23)
    time.sleep(1) 

    print("Platform is Ready!")


