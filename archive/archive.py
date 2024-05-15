from time import sleep
import RPi.GPIO as GPIO

class MotorControl:
    def __init__(self):
        # Motor Pins
        self.motor_pins = {
            1: {'DIR':21, 'STEP':20},
            2: {'DIR':6, 'STEP':5},
            3: {'DIR':24, 'STEP':23}
        }
        
        # Constants
        self.CW = 1  # Clockwise
        self.CCW = 0  # Counter-clockwise
        self.SPR = 200  # Steps per revolution
        self.delay = 0.0085  # Motor speed

        # Setup
        GPIO.setmode(GPIO.BCM)
        for pins in self.motor_pins.values():
            GPIO.setup(pins['DIR'], GPIO.OUT)
            GPIO.setup(pins['STEP'], GPIO.OUT)
            GPIO.output(pins['DIR'], self.CW)

    def move_motor(self, motor_num, direction, steps):
        pins = self.motor_pins[motor_num]
        
        # Hareket profili parametreleri
        acceleration_percent = 0.1  # Hızlanma süresi yüzdesi
        constant_speed_percent = 0.8  # Sabit hız süresi yüzdesi
        deceleration_percent = 0.1  # Yavaşlama süresi yüzdesi

        # Adım sayısı hesaplanıyor
        step_count = steps
        acceleration_steps = int(step_count * acceleration_percent)
        constant_speed_steps = int(step_count * constant_speed_percent)
        deceleration_steps = int(step_count * deceleration_percent)

        # Hızlanma ve yavaşlama parametreleri
        initial_speed = 0.01     # Başlangıç hızı (saniyede adım aralığı)
        max_speed = 0.008        # Maksimum hız (saniyede adım aralığı)

        # Hareket başlangıcı
        if direction == 'cw':
            GPIO.output(pins['DIR'], self.CW)
        elif direction == 'ccw':
            GPIO.output(pins['DIR'], self.CCW)
        
        # Hızlanma
        current_speed = initial_speed
        for _ in range(acceleration_steps):
            current_speed += (max_speed - initial_speed) / acceleration_steps
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(current_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(current_speed)

        # Sabit hız
        for _ in range(constant_speed_steps):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(max_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(max_speed)

        # Yavaşlama
        for _ in range(deceleration_steps):
            current_speed -= (max_speed - initial_speed) / deceleration_steps
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(current_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(current_speed)

        # Son konumu döndür
        return step_count

    def control_motors(self, commands):
        final_positions = {}
        for motor_num, (direction, steps) in commands.items():
            final_positions[motor_num] = self.move_motor(motor_num, direction, steps)
        
        return final_positions

# Örnek kullanım:
# controller = MotorControl()
# final_positions = controller.control_motors({1: ('cw', 200), 2: ('ccw', 400)})
# print(final_positions)
