import RPi.GPIO as GPIO
import time

class SimpleStepperMotorControl:
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

if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)

        motor_pins = {'step_pin': 17, 'dir_pin': 18, 'steps_per_rev': 200}
        motor = SimpleStepperMotorControl(**motor_pins)

        # 60 derece saat yönünde döndür
        motor.rotate(GPIO.HIGH, int(60 / 360 * motor.steps_per_rev))

        # Bekleme süresi
        time.sleep(1)

        # 60 derece saat yönünün tersine çevir
        motor.rotate(GPIO.LOW, int(60 / 360 * motor.steps_per_rev))

        motor.cleanup()
        
    except KeyboardInterrupt:
        GPIO.cleanup()
