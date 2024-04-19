## IMPORTS
import time

## MODULS
from motorModule_v2.motorModule_v2 import RobotController

## FUNCTIONS
def moveRobot(position):
    robot = RobotController()
    if position ==1:
        # Uç efektörü [1. Bölgeye] hareket ettir.
        commands1_1 = {
            1: ('cw', 58),   # Motor 1, rotate cw,  degrees 
            2: ('cw', 30),  #  Motor 2, rotate cw,  degrees
            3: ('cw', 32)   #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_1)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 1. Konumda")
        
        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands1_2 = {
            1: ('ccw', 31),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 6),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 15)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_2)

        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        commands1_3 = {
            1: ('cw', 31),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 6),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 15)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_3)

        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform İlk Konumda")

    elif position ==2:
        # Uç efektörü [2. Bölgeye] hareket ettir.
        commands2_1 = {
            1: ('cw', 50),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 39),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 25)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands2_1)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 2. Konumda")

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands2_2 = {
            1: ('ccw', 23),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 3),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 22)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands2_2)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        commands2_3 = {
            1: ('cw', 23),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 3),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 22)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands2_3)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform İlk Konumda")

    elif position ==3:
        # Uç efektörü [3. Bölgeye] hareket ettir.
        commands3_1 = {
            1: ('cw', 48),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 52),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 21)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands3_1)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 3. Konumda")

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands3_2 = {
            1: ('ccw', 21),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 16),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 26)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands3_2)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        commands3_3 = {
            1: ('cw', 21),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 16),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 26)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands3_3)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform İlk Konumda")

    else:
        print("Robot Hareketi Gerçekleştirilemedi...")

