## IMPORTS
import time

## MODULS
from motorModule import RobotController

## FUNCTIONS
def moveRobot(position):
    robot = RobotController()
    
    if position ==1:
        # Uç efektörü [1. Bölgeye] hareket ettir.
        commands1_1 = {
            1: ('cw', 30),   # Motor 1, rotate cw,  degrees 
            2: ('cw', 30),  #  Motor 2, rotate cw,  degrees
            3: ('cw', 30)   #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_1)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 1. Konumda")
        
        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands1_2 = {
            1: ('ccw', 30),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 30),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 30)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_2)

        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

    else:
        print("Robot Hareketi Gerçekleştirilemedi...")

