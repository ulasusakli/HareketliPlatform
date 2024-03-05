
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

        #Kamerayı aktifleştir ?
        camera_config = camera.create_preview_configuration()
        camera.configure(camera_config)
        camera.start_preview(Preview.DRM)
        camera.start()

        time.sleep(2)

        # Resmi çek ve kaydet
        image_path_test = "captured_image.jpg"
        image_path_test1 = "captured_image1.jpg"

        image_path_real = "src\piphoto\captured_image.jpg"

        camera.start_and_capture(image_path_test)
        camera.capture_file(image_path_test1)
        # Kırmızı nesnenin konumunu tespit et
        red_object_position1 = find_red_object_position(image_path_test)
        red_object_position2 = find_red_object_position(image_path_test1)

        # Elde edilen konumu ekrana yazdır
        print("Hedeflenen Nesnenin Konumu 1:", red_object_position1)
        print("Hedeflenen Nesnenin Konumu 2:", red_object_position2)
    
        return red_object_position1

# Fonksiyonu çağır
capture_and_process_image()



