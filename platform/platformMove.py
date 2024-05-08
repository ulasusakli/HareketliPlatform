## IMPORTS
import time

## MODULS
from platform_motorModule import RobotController

## FUNCTIONS
def moveRobot(position):
    robot = RobotController()
    
    if position ==1:
        # Uç efektörü [1. Bölgeye] hareket ettir.
        commands1_1 = {
            1: ('cw', 49),   # Motor 1, rotate cw,  degrees 
            2: ('cw', 56),  #  Motor 2, rotate cw,  degrees
            3: ('cw', 23)   #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_1)
    
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 1. Konumda")
        
        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands1_2 = {
            1: ('ccw', 17),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 12),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 32)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_2)

        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        commands1_3 = {
            1: ('cw', 17),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 12),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 32)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands1_3)

        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform İlk Konumda")
        #end of position=1

    elif position ==2:
        # Uç efektörü [2. Bölgeye] hareket ettir.
        commands2_1 = {
            1: ('cw', 50),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 40),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 27)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands2_1)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 2. Konumda")

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands2_2 = {
            1: ('ccw', 18),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 4),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 28)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands2_2)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        commands2_3 = {
            1: ('cw', 18),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 4),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 28)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands2_3)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform İlk Konumda")
        #end of position=2

    elif position ==3:
        # Uç efektörü [3. Bölgeye] hareket ettir.
        commands3_1 = {
            1: ('cw', 61),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 31),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 36)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands3_1)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform 3. Konumda")

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        commands3_2 = {
            1: ('ccw', 29),   # Motor 1, rotate ccw,  degrees 
            2: ('cw', 13),     #  Motor 2, rotate cw,  degrees
            3: ('cw', 19)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands3_2)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform Hedef Konumda")

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        commands3_3 = {
            1: ('cw', 29),   # Motor 1, rotate ccw,  degrees 
            2: ('ccw', 13),     #  Motor 2, rotate cw,  degrees
            3: ('ccw', 19)     #  Motor 3, rotate cw,  degrees
            }
        robot.control_motors(commands3_3)
        
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
        print("Platform İlk Konumda")
        #end of position=3

    elif position ==4: 
        print("Platform İlk Konuma Getiriliyor...")
        #Platformu resetlemek için yazılan pozisyon numarası
        
        # Motor 1 RESET
        commands4_11 = {
            1: ('ccw', 60)   
            }
        robot.control_motors(commands4_11)
        time.sleep(1)
        commands4_21 = {
            1: ('cw', 30)   
            }
        robot.control_motors(commands4_21)
        time.sleep(1)  

        # Motor 2 RESET
        commands4_12 = {
            2: ('ccw', 60) 
            }
        robot.control_motors(commands4_12)
        time.sleep(1)
        commands4_22 = {
            2: ('cw', 30)
            }
        robot.control_motors(commands4_22)
        time.sleep(1)

        # Motor 3 RESET
        commands4_13 = {  
            3: ('ccw', 60)   
            }
        robot.control_motors(commands4_13)
        time.sleep(1)  

        commands4_23 = {    
            3: ('cw', 30)     
            }
        robot.control_motors(commands4_23)
        time.sleep(1) 
        print("Hareket Bekleniyor...")
        #end of position=4

    elif position ==5:
        print("Platform İlk Konuma Getiriliyor...")
        # Motorları yukarı kaldırmak için yazılan pozisyon numarası
        commands5_1 = {
            1: ('ccw', 15),
            2: ('ccw', 15),
            3: ('ccw', 15)  
            }
        robot.control_motors(commands5_1)
        time.sleep(1)
        #end of position=5
    else:
        print("Robot Hareketi Gerçekleştirilemedi...")

