"""
*********** FOTOĞRAF ÇEKME MODÜLÜ*************
sudo apt-get update
sudo apt-get install python-picamera python3-picamera

sudo apt-get update
sudo apt-get upgrade
"""

import time
import picamera

# Görüntü işleme modülünü import et
from colorDetectionv1 import find_red_object_position

def capture_and_process_image():
    # Kamera örneğini oluştur
    with picamera.PiCamera() as camera:
        # Kamerayı 1 saniye beklet (ışığın düzenlenmesi için)
        time.sleep(1)

        # Resmi çek ve kaydet
        image_path_test = "captured_image.jpg"
        image_path_real = "src\piphoto\captured_image.jpg"
        camera.capture(image_path_test)

        # Kırmızı nesnenin konumunu tespit et
        red_object_position = find_red_object_position(image_path_test)

        # Elde edilen konumu ekrana yazdır
        print("Hedeflenen Nesnenin Konumu:", red_object_position)
    
        return red_object_position

# Fonksiyonu çağır
capture_and_process_image()
