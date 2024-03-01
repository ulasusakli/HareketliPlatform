"""
MOTOR KONTROL KÜTÜPHANESİ

ÖNEMLİ NOT !
Current Limit = VRef x 2.5
Olarak motor sürücü üzerinde konfigüre edilmeli
Örneğin, Step Motor 350mA olarak derecelendirilmişse 
referans voltajını 0,14V'a ayarlamamız gerekir. 
Küçük bir tornavida alın ve nominal akıma ulaşana kadar 
akım sınırını bir potansiyometre ile ayarlayın.

** Bizde 0,6 = VRef * 2.5 **
VRef = 0.24 V olarak ayarlanacak

"""

import RPi.GPIO as GPIO
import time

class StepperMotor:
    def __init__(self, step_pin, dir_pin, steps_per_rev):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.steps_per_rev = steps_per_rev

        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

    def rotate(self, direction, steps, delay=0.001):
        GPIO.output(self.dir_pin, direction)

        for _ in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(delay)

    def cleanup(self):
        GPIO.cleanup([self.step_pin, self.dir_pin])

class RobotController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        # Motor pinleri ve devir başına adım sayısı tanımlanır.
        self.motor1_pins = {'step_pin': 17, 'dir_pin': 18, 'steps_per_rev': 200}
        self.motor2_pins = {'step_pin': 22, 'dir_pin': 23, 'steps_per_rev': 200}
        self.motor3_pins = {'step_pin': 5, 'dir_pin': 6, 'steps_per_rev': 200}

        # Her bir motor için bir StepperMotor örneği oluşturulur.
        self.motor1 = StepperMotor(**self.motor1_pins)
        self.motor2 = StepperMotor(**self.motor2_pins)
        self.motor3 = StepperMotor(**self.motor3_pins)

    def move_motor(self, motor_number, angle):
        if motor_number == 1:
            self.motor1.rotate(GPIO.HIGH, int(angle / 360 * self.motor1.steps_per_rev))
        elif motor_number == 2:
            self.motor2.rotate(GPIO.HIGH, int(angle / 360 * self.motor2.steps_per_rev))
        elif motor_number == 3:
            self.motor3.rotate(GPIO.HIGH, int(angle / 360 * self.motor3.steps_per_rev))
    
    def move_motor_ccw(self, motor_number, angle):
        if motor_number == 1:
            self.motor1.rotate(GPIO.LOW, int(angle / 360 * self.motor1.steps_per_rev))
        elif motor_number == 2:
            self.motor2.rotate(GPIO.LOW, int(angle / 360 * self.motor2.steps_per_rev))
        elif motor_number == 3:
            self.motor3.rotate(GPIO.LOW, int(angle / 360 * self.motor3.steps_per_rev))

    def cleanup(self):
        self.motor1.cleanup()
        self.motor2.cleanup()
        self.motor3.cleanup()

# Örnek Kullanım:
# robot = RobotController()
# robot.move_motor(1, 90)  # Motor 1'i 90 derece döndür
# robot.move_motor(2, 180)  # Motor 2'yi 180 derece döndür
# robot.cleanup()
