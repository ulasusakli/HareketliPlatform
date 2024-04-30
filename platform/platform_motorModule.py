from time import sleep
import RPi.GPIO as GPIO
import threading

class RobotController:
    def __init__(self):
        # Motor Pins
        self.motor_pins = {
            1: {'DIR':21, 'STEP':20},
            2: {'DIR':6, 'STEP':5},
            3: {'DIR':24, 'STEP':23}
        }
        # Other Pins
        self.relayPin = 13  # Relay Pin

        # Constants
        self.CW = 1  # Clockwise
        self.CCW = 0  # Counter-clockwise
        self.SPR = 200  # Steps per revolution
        self.delay = 0.0085  # Motor speed

        # Setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relayPin, GPIO.OUT)
        GPIO.output(self.relayPin, GPIO.LOW)

        for motor_num, pins in self.motor_pins.items():
            GPIO.setup(pins['DIR'], GPIO.OUT)
            GPIO.setup(pins['STEP'], GPIO.OUT)
            GPIO.output(pins['DIR'], self.CW)

    def move_motor_cw(self, motor_num, angle):
        step_count = int((self.SPR / 360) * angle)
        pins = self.motor_pins[motor_num]

        GPIO.output(pins['DIR'], self.CW)
        for _ in range(step_count):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(self.delay)

    def move_motor_ccw(self, motor_num, angle):
        step_count = int((self.SPR / 360) * angle)
        pins = self.motor_pins[motor_num]

        GPIO.output(pins['DIR'], self.CCW)
        for _ in range(step_count):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(self.delay)

        GPIO.output(pins['DIR'], self.CW)

    def relay_on(self, dtime):
        sleep(0.5)
        GPIO.output(self.relayPin, GPIO.HIGH)
        print("Electromagnet Aktif")
        sleep(dtime)

    def relay_off(self, dtime):
        sleep(0.5)
        GPIO.output(self.relayPin, GPIO.LOW)
        print("Electromagnet Pasif")
        sleep(dtime)

    def control_motors(self, commands):
        threads = []
        for motor_num, (direction, angle) in commands.items():
            if direction == 'cw':
                t = threading.Thread(target=self.move_motor_cw, args=(motor_num, angle))
                threads.append(t)
            elif direction == 'ccw':
                t = threading.Thread(target=self.move_motor_ccw, args=(motor_num, angle))
                threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()
