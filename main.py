###### KÜTÜPHANELER
import RPi.GPIO as GPIO
import time

###### Kamera Modülü
from colorDetectionv1 import find_red_object_position
from captureModule import capture_and_process_image

###### Platform Kontrol Modülü
from moveRobotModule import moveRobot

### Configuration
GPIO.setmode(GPIO.BCM)

# Hedeflenen renkteki nesnenin konumunu al
position_result = capture_and_process_image()

time.sleep(1) # Hareketlerin tamamlanması için bir süre bekle

# Hedef Nesnenin Pozisyonuna göre Uç Efektörü Hareket Ettir.
if position_result == "Left":
    print("Nesne Birinci Pozisyonda")
    moveRobot("Left")
elif position_result == "Mid":
    print("Nesne İkinci Pozisyonda")
    moveRobot("Mid")
elif position_result == "Right":
    print("Nesne Üçüncü Pozisyonda")
    moveRobot("Right")
else:
    print("Nesne Bulunamadi.")




