from time import sleep
import RPi.GPIO as GPIO

class RobotController:
    def __init__(self):
        # ----Motor Pinleri----
        self.motor_pins = {
            1: {'DIR':21, 'STEP':20},
            2: {'DIR':6, 'STEP':5},
            3: {'DIR':24, 'STEP':23}
        }
        # --------Diğer Pinler----------
        self.relayPin = 13 # Relay Pini

        # ------------------------------

        # -----Tanımlar-----
        self.CW = 1 # Saat Yönü
        self.CCW = 0 # Saat yönünün tersi
        self.SPR = 200 # 1 tur için atılan adım
        self.delay = 0.0085  # Motorun Hızı 

        # --------Ayarlar---------------
        GPIO.setmode(GPIO.BCM)

        # ------------------------------

        # ----Pin Konfigürasyonu----
        #Relay Pin
        GPIO.setup(self.relayPin, GPIO.OUT) # Röle Tetik Pini
        GPIO.output(self.relayPin, GPIO.LOW) # Başlangıçta Kapalı 

        #Motor 1
        GPIO.setup(21, GPIO.OUT)  #Direction Pini
        GPIO.setup(20, GPIO.OUT)  #Step Pini
        GPIO.output(21, self.CW)  #Başlangıçta Saat Yönünde (direction pini)

        #Motor 2
        GPIO.setup(6, GPIO.OUT)  #Direction Pini
        GPIO.setup(5, GPIO.OUT)  #Step Pini
        GPIO.output(6, self.CW)  #Başlangıçta Saat Yönünde (direction pini)

        #Motor 3
        GPIO.setup(24, GPIO.OUT)  #Direction Pini
        GPIO.setup(23, GPIO.OUT)  #Step Pini
        GPIO.output(24, self.CW)  #Başlangıçta Saat Yönünde (direction pini)
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

    # Röle pinini aktifleştiren fonksiyon
    def relay_on(self, dtime):
        sleep(0.5)
        GPIO.output(self.relayPin, GPIO.HIGH)
        sleep(dtime)

    # Röle pinini pasif hale getiren fonksiyon
    def relay_off(self, dtime):
        sleep(0.5)
        GPIO.output(self.relayPin, GPIO.LOW)
        sleep(dtime)

