import RPi.GPIO as GPIO
import time

from motorModule import RobotController

def moveRobot(position):
    robot = RobotController()
    relay_pin = 17
    GPIO.setup(relay_pin, GPIO.OUT) # Mıknatıs pinini çıkış olarak ayarladık
    GPIO.output(relay_pin, GPIO.HIGH) # Mıknatısı başlangıçta aktif hale getirdik

    # Motorların başlangıç açıları 0,0,0 olarak ayarlanmıştır.
    # Motoru Saat yönünde sürmek için robot.move_motor_cw(i,a) komutunu kullanın
    # Motoru Saat yönünün tersinde sürmek için robot.move_motor_ccw(i,a) komutunu kullanın

    if position =="Left":
        # Uç efektörü [1. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 60)
        robot.move_motor_cw(2, 60)
        robot.move_motor_cw(3, 120)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        GPIO.setup(relay_pin, GPIO.OUT)
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(3)  # Mıknatıs 3 saniye boyunca aktif kalsın

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 120)
        robot.move_motor_cw(3, 0)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(3)  # Mıknatıs 3 saniye boyunca pasif kalsın

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 120)
        robot.move_motor_cw(3, 0)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle


    if position =="Mid":
        # Uç efektörü [2. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 60)
        robot.move_motor_cw(2, 60)
        robot.move_motor_cw(3, 120)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        GPIO.setup(relay_pin, GPIO.OUT)
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(3)  # Mıknatıs 3 saniye boyunca aktif kalsın

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 120)
        robot.move_motor_cw(3, 0)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(3)  # Mıknatıs 3 saniye boyunca pasif kalsın

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 120)
        robot.move_motor_cw(3, 0)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle


    if position =="Right":
        # Uç efektörü [3. Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 60)
        robot.move_motor_cw(2, 60)
        robot.move_motor_cw(3, 120)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini aktif et
        GPIO.setup(relay_pin, GPIO.OUT)
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(3)  # Mıknatıs 3 saniye boyunca aktif kalsın

        # Uç efektörü [Hedef Bölgeye] hareket ettir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 120)
        robot.move_motor_cw(3, 0)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle

        # Mıknatıs pinini pasif et
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(3)  # Mıknatıs 3 saniye boyunca pasif kalsın

        # Uç efektörü [Başlangıç Pozisyonuna] getir.
        robot.move_motor_cw(1, 30)
        robot.move_motor_cw(2, 120)
        robot.move_motor_cw(3, 0)
        time.sleep(1)  # Hareketlerin tamamlanması için bir süre bekle
    
    else:
        print("Robot Hareketi Gerçekleştirilemedi...")
