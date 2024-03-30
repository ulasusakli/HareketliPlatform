
#*********** FOTOĞRAF ÇEKME MODÜLÜ*************
from picamera2 import Picamera2, Preview
import time

# Görüntü işleme modülünü import et
from visionAlgorithm import crop_and_save, divide_and_save, detect_object

def capture_and_process_image():
    # Kamera örneğini oluştur
    with Picamera2() as camera:
        # Kamerayı 1 saniye beklet (ışığın düzenlenmesi için)
        time.sleep(1)

        # Fotoğraf Konumları
        image_path_test = "/home/m2labteam/Desktop/platform/3DOFPlatform/src/piphototest/captured_test_image.jpg"
        image_path_real = "/home/m2labteam/Desktop/platform/3DOFPlatform/src/piphoto/captured_image.jpg"

        # Fotoğrafı Çek ve Hedeflenen Konuma Kaydet
        camera.start_and_capture_file(image_path_real)

        # Çekilen Fotoğrafı Kırp ve Kaydet
        crop_image_path = "/home/m2labteam/Desktop/platform/3DOFPlatform/src/piphoto/crop_image.jpg"
        crop_and_save(image_path_real, crop_image_path)

        # Kırpılan Fotoğrafı Bölgelere Ayır ve Kaydet
        divide_image_path = "/home/m2labteam/Desktop/platform/3DOFPlatform/src/piphoto/divide_image.jpg"
        divide_and_save(crop_image_path, divide_image_path)

        # Bölgelere Ayrılmış Fotoğraftaki İstenilen Renkteki Nesnenin Pozisyonunu Belirle
        final_image_path = "/home/m2labteam/Desktop/platform/3DOFPlatform/src/piphoto/Final_Image.jpg"
        region = detect_object(divide_image_path, final_image_path)

        # Elde edilen konumu ekrana yazdır
        print("Object is in:", region)
    
        return region

# Fonksiyonu çağır
capture_and_process_image()



