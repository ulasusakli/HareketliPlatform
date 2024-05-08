## IMPORTS
import time

## MODULS
from motorModule import RobotController

## FUNCTIONS
def moveRobot(position):
    robot = RobotController()
    
    if position ==1:
        # Motor 1 RESET
        commands1_11 = {
            1: ('ccw', 60)   
            }
        robot.control_motors(commands1_11)
        time.sleep(1)
        commands1_21 = {
            1: ('cw', 30)   
            }
        robot.control_motors(commands1_21)
        time.sleep(1)  

        # Motor 2 RESET
        commands1_12 = {
            2: ('ccw', 60) 
            }
        robot.control_motors(commands1_12)
        time.sleep(1)
        commands1_22 = {
            2: ('cw', 30)
            }
        robot.control_motors(commands1_22)
        time.sleep(1)

        # Motor 3 RESET
        commands1_13 = {  
            3: ('ccw', 60)   
            }
        robot.control_motors(commands1_13)
        time.sleep(1)  

        commands1_23 = {    
            3: ('cw', 30)     
            }
        robot.control_motors(commands1_23)
        time.sleep(1)  

        
          
        



    else:
        print("Robot Hareketi Gerçekleştirilemedi...")

