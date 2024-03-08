import RPi.GPIO as GPIO
import time

from test_motorController import MotorController

# Kullanım örneği
robot = MotorController()
robot.move_motor_cw(1, 180)  # Motor 1'i 60 derece saat yönünde döndür
time.sleep(0.5)
robot.move_motor_ccw(1, 180)  # Motor 2'yi 120 derece saat yönünün tersine döndür
time.sleep(0.5)