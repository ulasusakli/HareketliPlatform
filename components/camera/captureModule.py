
#*********** FOTOĞRAF ÇEKME MODÜLÜ*************

from picamera2 import Picamera2, Preview
import time

# Görüntü işleme modülünü import et
from colorDetectionv1 import find_red_object_position

def capture_and_process_image():
    # Kamera örneğini oluştur
    with Picamera2() as camera:
        # Kamerayı 1 saniye beklet (ışığın düzenlenmesi için)
        time.sleep(1)

        # Fotoğraf Konumları
        image_path_test = "captured_image.jpg"
        image_path_real = "/home/m2labteam/Desktop/platform/3DOFPlatform/src/piphototest/captured_image.jpg"

        # Fotoğrafı Çek ve Hedeflenen Konuma Kaydet
        camera.start_and_capture_file(image_path_real)

        # Hedeflenen Renkteki nesnenin konumunu tespit et
        red_object_position = find_red_object_position(image_path_real)

        # Elde edilen konumu ekrana yazdır
        print("Hedeflenen Nesnenin Konumu:", red_object_position)
    
        return red_object_position

# Fonksiyonu çağır
capture_and_process_image()



