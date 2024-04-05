import cv2
import numpy as np

# Kırmızı rengin HSV değerlerini tanımla
h = 175
s = 150
v = 90

# HSV değerlerini kullanarak kırmızı rengi oluştur
color_hsv = np.uint8([[[h, s, v]]])
color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)

# Kırmızı rengi daha büyük bir alanda göstermek için beyaz bir resim oluştur
image = np.full((200, 200, 3), (255, 255, 255), dtype=np.uint8)
image[50:150, 50:150] = color_bgr  # Kırmızı rengi ortaya yerleştir

# Kırmızı rengi göster
cv2.imshow('Color', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
