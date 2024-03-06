import RPi.GPIO as GPIO
import time

from controlTutorialv1 import RobotControllerDeneme

# Kullanım örneği
robot = RobotControllerDeneme()
robot.move_motor_cw(1, 180)  # Motor 1'i 60 derece saat yönünde döndür
time.sleep(0.5)
robot.move_motor_ccw(1, 180)  # Motor 2'yi 120 derece saat yönünün tersine döndür
time.sleep(0.5)