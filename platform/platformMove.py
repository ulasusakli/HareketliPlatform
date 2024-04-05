## Kütüphaneler
import time

## Modüller
from platform_motorModule import RobotController

## Fonksiyonlar
def moveRobot(position):
    robot = RobotController()

    if position ==1:
        # Uç efektörü [1. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 30)
        robot.move_motor_cw(3, 30)
        print("Platform 1. Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        print("Electromagnet Aktif")
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 20)
        robot.move_motor_cw(2, 20)
        robot.move_motor_cw(3, 20)
        print("Platform Hedef Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        print("Electromagnet Pasif")
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_ccw(1, 50)
        robot.move_motor_ccw(2, 50)
        robot.move_motor_ccw(3, 50)
        print("Platform İlk Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle


    elif position ==2:
        # Uç efektörü [2. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 30)
        robot.move_motor_cw(3, 30)
        print("Platform 2. Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        print("Electromagnet Aktif")
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 20)
        robot.move_motor_cw(2, 20)
        robot.move_motor_cw(3, 20)
        print("Platform Hedef Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        print("Electromagnet Pasif")
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_ccw(1, 50)
        robot.move_motor_ccw(2, 50)
        robot.move_motor_ccw(3, 50)
        print("Platform İlk Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle


    elif position ==3:
        # Uç efektörü [3. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 30)
        robot.move_motor_cw(3, 30)
        print("Platform 3. Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        robot.relay_on(3)
        print("Electromagnet Aktif")
        time.sleep(0.5)

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 20)
        robot.move_motor_cw(2, 20)
        robot.move_motor_cw(3, 20)
        print("Platform Hedef Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        robot.relay_off(3)
        print("Electromagnet Pasif")
        time.sleep(0.5)

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_ccw(1, 50)
        robot.move_motor_ccw(2, 50)
        robot.move_motor_ccw(3, 50)
        print("Platform İlk Konumda")
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
    
    else:
        print("Robot Hareketi Gerçekleştirilemedi...")


