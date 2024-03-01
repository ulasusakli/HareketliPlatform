"""
** GÖRÜNTÜ İŞLEME MODÜLÜ **

sudo apt-get update
sudo apt install python3-dev python3-pip
sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y
sudo apt-get install python3-opencv
sudo apt install python3-numpy

"""
import cv2
import numpy as np

def find_red_object_position(image_path):
    # Resmi oku
    image = cv2.imread(image_path)

    # Resmi HSV formatına çevir
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirle
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Kırmızı renk alanlarını maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Kırmızı nesne konturunu bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Eğer kontur bulunduysa
    if contours:
        # En büyük konturu bul (en geniş alanlı)
        max_contour = max(contours, key=cv2.contourArea)

        # Konturun merkezini bul
        M = cv2.moments(max_contour)
        cx = int(M['m10'] / M['m00'])

        # Resmin genişliği ve merkez noktasına göre konumu belirle
        image_width = image.shape[1]
        position_threshold = image_width // 3

        if cx < position_threshold:
            position = "Left"
        elif cx < 2 * position_threshold:
            position = "Mid"
        else:
            position = "Right"

        return position
    else:
        return "Kirmizi nesne bulunamadi"

"""
#*******************************TEST************************************
# Resim dosyasının yolu
image_path = "src\piphototest\poz3.png"

# Kırmızı nesnenin konumunu bul
red_object_position = find_red_object_position(image_path)

# Konumu ekrana yazdır
print("Kirmizi nesnenin konumu:", red_object_position)
#*******************************TEST************************************
"""

# Elde ettiğiniz konumu başka Python kodlarında kullanabilirsiniz.
# Örneğin:
# if red_object_position == "Sol":
#     # Sol konumda bir şey yap
# elif red_object_position == "Orta":
#     # Orta konumda bir şey yap
# elif red_object_position == "Sağ":
#     # Sağ konumda bir şey yap

