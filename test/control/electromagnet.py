import RPi.GPIO as GPIO
import time

# GPIO modunu BCM olarak ayarla
GPIO.setmode(GPIO.BCM)

# Röle kontrol pini 
relay_pin = 16

# Röle kontrol pini çıkış olarak ayarla
GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        # Röleyi aç
        GPIO.output(relay_pin, GPIO.HIGH)
        print("Röle açık")
        time.sleep(2)  # 2 saniye beklet

        # Röleyi kapat
        GPIO.output(relay_pin, GPIO.LOW)
        print("Röle kapalı")
        time.sleep(2)  # 2 saniye beklet

except KeyboardInterrupt:
    print("Program kapatıldı")
    GPIO.cleanup()
