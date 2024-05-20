import random
from robot_controller import RobotController #Burası Güncellencek
from time import sleep

# Create an instance of RobotController
controller = RobotController() #Burası Güncellencek

def move_to_position(position):

    # Determine the Object Position and Target Position for each position number
    if position == 1:
        object_position = {'motor1': 43, 'motor2': 65, 'motor3': 30} #Obje Konumuna olan Hareket
        target_position_relative = {'motor1': 30, 'motor2': 30, 'motor3': 30} # Obje Konumundan Hedefe Olan Hareket

    elif position == 2:
        object_position = {'motor1': 30, 'motor2': 30, 'motor3': 30}#Obje Konumuna olan Hareket
        target_position_relative = {'motor1': 30, 'motor2': 30, 'motor3': 30}# Obje Konumundan Hedefe Olan Hareket

    elif position == 3:
        object_position = {'motor1': 40, 'motor2': 40, 'motor3': 40}#Obje Konumuna olan Hareket
        target_position_relative = {'motor1': 30, 'motor2': 30, 'motor3': 30}# Obje Konumundan Hedefe Olan Hareket
    
    # Calculate the position to return from target to initial
    calculated_position = {
        'motor1': object_position['motor1'] + target_position_relative['motor1'],
        'motor2': object_position['motor2'] + target_position_relative['motor2'],
        'motor3': object_position['motor3'] + target_position_relative['motor3']
    }
    print(calculated_position)
    
    # Move from the Initial position to the object position
    print(f"Moving from the initial position to the position {position} ")
    controller.control_motors({
        1: ('cw', object_position['motor1']),
        2: ('cw', object_position['motor2']),
        3: ('cw', object_position['motor3'])
    })
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
        1: ('ccw', calculated_position['motor1']),
        2: ('ccw', calculated_position['motor2']),
        3: ('ccw', calculated_position['motor3'])
    })
    sleep(2)  # Delay for 2 seconds

    # Reset Platform
    

move_to_position(1)