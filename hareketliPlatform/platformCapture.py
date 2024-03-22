
from picamera2 import Picamera2, Preview
import time

# Görüntü işleme modülünü import et
from platformColorDetection import find_object_position

def capture_and_process_image():
    # Kamera örneğini oluştur
    with Picamera2() as camera:
        # Kamerayı 1 saniye beklet (ışığın düzenlenmesi için)
        time.sleep(1)

        # Fotoğraf Konumları
        image_path_real = "/home/m2labteam/Desktop/platform/HareketliPlatform/src/piphoto/captured_image.jpg"

        # Create a dummy photo
        image_path_test = "/home/m2labteam/Desktop/platform/HareketliPlatform/src/piphototest/poz1.png"
        
        # Fotoğrafı Çek ve Hedeflenen Konuma Kaydet
        camera.start_and_capture_file(image_path_real)

        # Hedeflenen Renkteki nesnenin konumunu tespit et
        object_position = find_object_position(image_path_test)

        # Elde edilen konumu ekrana yazdır
        print("Hedeflenen Nesnenin Konumu:", object_position)
    
        return object_position

# Fonksiyonu çağır



