from time import sleep
import RPi.GPIO as GPIO

class RobotControllerDeneme:
    def __init__(self):
        # ----Motor Pinleri----
        self.motor_pins = {
            1: {'DIR': 21, 'STEP': 20},
            2: {'DIR': 23, 'STEP': 24},
            3: {'DIR': 16, 'STEP': 12}
        }
        # ---------------------

        # -----Tanım ve Ayarlar-----
        self.CW = 1 # Saat Yönü
        self.CCW = 0 # Saat yönünün tersi
        self.SPR = 200 # 1 tur için atılan adım
        self.delay = 0.00085  # Motorun Hızı 

        GPIO.setmode(GPIO.BCM)
        # --------------------------

        # ----Pin Konfigürasyonu----
        #Motor 1
        GPIO.setup(21, GPIO.OUT)  #Direction Pini
        GPIO.setup(20, GPIO.OUT)  #Step Pini
        GPIO.output(21, self.CW)  #Başlangıçta Saat Yönünde (direction pini)

        #Motor 2
        GPIO.setup(23, GPIO.OUT)  #Direction Pini
        GPIO.setup(24, GPIO.OUT)  #Step Pini
        GPIO.output(23, self.CW)  #Başlangıçta Saat Yönünde (direction pini)

        #Motor 3
        GPIO.setup(16, GPIO.OUT)  #Direction Pini
        GPIO.setup(12, GPIO.OUT)  #Step Pini
        GPIO.output(16, self.CW)  #Başlangıçta Saat Yönünde (direction pini)
        # -------------------------

    # Motoru saat yönünde döndürme fonksiyonu
    def move_motor_cw(self, motor_num, angle):

        # Saat yönünde motoru belirtilen açıda döndür
        step_count = int((self.SPR / 360) * angle)
        pins = self.motor_pins[motor_num]

        # Saat yönünde döndürme komudu
        GPIO.output(pins['DIR'], self.CW) 

        for _ in range(step_count):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(self.delay)

    # Motoru saat yönünün tersine döndürme fonksiyonu
    def move_motor_ccw(self, motor_num, angle):
        # Saat yönünün tersine motoru belirtilen açıda döndür
        step_count = int((self.SPR / 360) * angle)
        pins = self.motor_pins[motor_num]

        # Saat yönünün tersine döndürme komudu
        GPIO.output(pins['DIR'], self.CCW)

        for _ in range(step_count):
            GPIO.output(pins['STEP'], GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(pins['STEP'], GPIO.LOW)
            sleep(self.delay)

        GPIO.output(pins['DIR'], self.CW)  # Saat yönüne geri döndür

# Kullanım örneği
robot = RobotControllerDeneme()
robot.move_motor_cw(1, 60)  # Motor 1'i 60 derece saat yönünde döndür
robot.move_motor_ccw(2, 120)  # Motor 2'yi 120 derece saat yönünün tersine döndür

