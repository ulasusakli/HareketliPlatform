from time import sleep
import RPi.GPIO as GPIO
import threading
import math

class RobotController:
    def __init__(self):
        # Motor Pins
        self.motor_pins = {
            1: {'DIR':21, 'STEP':20, 'current_step': 0},
            2: {'DIR':6, 'STEP':5, 'current_step': 0},
            3: {'DIR':24, 'STEP':23, 'current_step': 0}
        }
        # Other Pins
        self.relayPin = 13  # Relay Pin

        # Constants
        self.CW = 1  # Clockwise
        self.CCW = 0  # Counter-clockwise
        self.SPR = 200  # Steps per revolution
        #self.delay = 0.0085  # Ideal Motor Hızı Değerimiz

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

        # Hareket profili parametreleri
        acceleration_percent = 0.1  # Hızlanma süresi yüzdesi
        constant_speed_percent = 0.8  # Sabit hız süresi yüzdesi
        deceleration_percent = 0.1  # Yavaşlama süresi yüzdesi
        
        # Adım sayaçlarını sıfırla
        pins['current_step'] = 0

        # Adım sayısı hesaplanıyor
        acceleration_steps = int(step_count * acceleration_percent)
        constant_speed_steps = int(step_count * constant_speed_percent)
        deceleration_steps = int(step_count * deceleration_percent)

        # Hızlanma ve yavaşlama parametreleri
        initial_speed = 0.01     # Başlangıç hızı (saniyede adım aralığı)
        max_speed = 0.0080       # Maksimum hız (saniyede adım aralığı)

        # Hareket başlangıcı
        GPIO.output(pins['DIR'], self.CW)

        # Hızlanma
        current_speed = initial_speed
        for _ in range(acceleration_steps):
            current_speed += (max_speed - initial_speed) / acceleration_steps
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(current_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(current_speed)
            # Adım sayacını güncelle
            pins['current_step'] += 1

        # Sabit hız
        for _ in range(constant_speed_steps):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(max_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(max_speed)
            # Adım sayacını güncelle
            pins['current_step'] += 1

        # Yavaşlama
        for _ in range(deceleration_steps):
            current_speed -= (max_speed - initial_speed) / deceleration_steps
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(current_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(current_speed)
            # Adım sayacını güncelle
            pins['current_step'] += 1

        print(f"Motor {motor_num} son konumu: {pins['current_step']}")
        step_value = pins['current_step']
        return step_value

    def move_motor_ccw(self, motor_num, angle):
        step_count = int((self.SPR / 360) * angle)
        pins = self.motor_pins[motor_num]

        # Hareket profili parametreleri
        acceleration_percent = 0.1  # Hızlanma süresi yüzdesi
        constant_speed_percent = 0.8  # Sabit hız süresi yüzdesi
        deceleration_percent = 0.1  # Yavaşlama süresi yüzdesi
        
        # Adım sayaçlarını sıfırla
        pins['current_step'] = 0

        # Adım sayısı hesaplanıyor
        acceleration_steps = int(step_count * acceleration_percent)
        constant_speed_steps = int(step_count * constant_speed_percent)
        deceleration_steps = int(step_count * deceleration_percent)

        # Hızlanma ve yavaşlama parametreleri
        initial_speed = 0.01     # Başlangıç hızı (saniyede adım aralığı)
        max_speed = 0.0080       # Maksimum hız (saniyede adım aralığı)

        # Hareket başlangıcı
        GPIO.output(pins['DIR'], self.CCW)

        # Hızlanma
        current_speed = initial_speed
        for _ in range(acceleration_steps):
            current_speed += (max_speed - initial_speed) / acceleration_steps
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(current_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(current_speed)
            # Adım sayacını güncelle
            pins['current_step'] += 1

        # Sabit hız
        for _ in range(constant_speed_steps):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(max_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(max_speed)
            # Adım sayacını güncelle
            pins['current_step'] += 1

        # Yavaşlama
        for _ in range(deceleration_steps):
            current_speed -= (max_speed - initial_speed) / deceleration_steps
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(current_speed)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(current_speed)
            # Adım sayacını güncelle
            pins['current_step'] += 1

        print(f"Motor {motor_num} son konumu: {pins['current_step']}")
        step_value = pins['current_step']
        return step_value

    def relay_on(self, dtime):
        sleep(0.5)
        GPIO.output(self.relayPin, GPIO.HIGH)
        print("Elektro Magnet Aktif Durumda")
        sleep(dtime)

    def relay_off(self, dtime):
        sleep(0.5)
        GPIO.output(self.relayPin, GPIO.LOW)
        print("Elektro Magnet Pasif Durumda")
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

# Örnek kullanım:
# controller = RobotController()
# controller.control_motors({1: ('cw', 90), 2: ('ccw', 180)})
