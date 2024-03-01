import RPi.GPIO as GPIO
import time

from motorModule import RobotController



if __name__ == "__main__":
    try:
        robot = RobotController()
        
        # Örnek kullanım
        robot.move_motor(1, 60)  # Motor 1'i 60 derece döndür
        robot.move_motor(1, -60)  # Motor 1'i 60 derece saat yönünün tersine çevir

        # Motorları temizle
        robot.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()
