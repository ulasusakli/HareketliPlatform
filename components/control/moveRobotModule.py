## IMPORTS
import time

## MODULS
from motorModule import RobotController

## FUNCTIONS
def moveRobot(position):
    robot = RobotController()

    if position ==1:
        # Uç efektörü [1. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 58)
        robot.move_motor_cw(2, 30)
        robot.move_motor_cw(3, 32)
        print("Platform 1. Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        print("Electromagnet Aktif")
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_ccw(1, 31)
        robot.move_motor_cw(2, 6)
        robot.move_motor_cw(3, 15)
        print("Platform Hedef Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        print("Electromagnet Pasif")
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_cw(1, 31)
        robot.move_motor_ccw(2, 6)
        robot.move_motor_ccw(3, 15)
        print("Platform İlk Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle


    elif position ==2:
        # Uç efektörü [2. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 50)
        robot.move_motor_cw(2, 39)
        robot.move_motor_cw(3, 25)
        print("Platform 2. Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        print("Electromagnet Aktif")
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_ccw(1, 23)
        robot.move_motor_ccw(2, 3)
        robot.move_motor_cw(3, 22)
        print("Platform Hedef Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        print("Electromagnet Pasif")
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_cw(1, 23)
        robot.move_motor_cw(2, 3)
        robot.move_motor_ccw(3, 22)
        print("Platform İlk Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle


    elif position ==3:
        # Uç efektörü [3. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 48)
        robot.move_motor_cw(2, 52)
        robot.move_motor_cw(3, 21)
        print("Platform 3. Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        print("Electromagnet Aktif")
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_ccw(1, 21)
        robot.move_motor_ccw(2, 16)
        robot.move_motor_cw(3, 26)
        print("Platform Hedef Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        print("Electromagnet Pasif")
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_cw(1, 21)
        robot.move_motor_cw(2, 16)
        robot.move_motor_ccw(3, 26)
        print("Platform İlk Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
    
    else:
        print("Robot Hareketi Gerçekleştirilemedi...")


moveRobot(1)