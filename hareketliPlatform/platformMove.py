import RPi.GPIO as GPIO
import time

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Import the platform module
from platform_motorModule import RobotController

def moveRobot(position):
    # Define the Platform as a robot
    robot = RobotController()

    # Define the GPIO pin controlled the relay
    relay_pin =13
    GPIO.setmode(GPIO.BCM) # Set the GPIO mode (BCM or BOARD)
    GPIO.setup(relay_pin, GPIO.OUT) # Röle pinini çıkış olarak ayarladık
    GPIO.output(relay_pin, GPIO.HIGH) # Röleyi başlangıçta aktif hale getirdik

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
