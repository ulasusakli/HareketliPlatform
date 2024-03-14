
#** GÖRÜNTÜ İŞLEME MODÜLÜ **
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
image_path = "src\piphototest\poz3.png"

# Kirmizi nesnenin konumunu bul
red_object_position = find_red_object_position(image_path)

# Konumu ekrana yazdir
print("Kirmizi nesnenin konumu:", red_object_position)
#*******************************TEST************************************
"""


