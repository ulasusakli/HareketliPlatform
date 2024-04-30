import cv2
import numpy as np

# Rengin HSV değerlerini tanımla
# hue range is [0,179], saturation range is [0,255], and value range is [0,255]

#Lower 
hl = 175
sl = 138
vl = 75

#Higher 
hh = 179
sh = 255
vh = 255

# HSV değerlerini kullanarak Lower rengi oluştur
color_hsv_low = np.uint8([[[hl, sl, vl]]])
color_bgr_low = cv2.cvtColor(color_hsv_low, cv2.COLOR_HSV2BGR)

# HSV değerlerini kullanarak Higher rengi oluştur
color_hsv_high = np.uint8([[[hh, sh, vh]]])
color_bgr_high = cv2.cvtColor(color_hsv_high, cv2.COLOR_HSV2BGR)

# Lower Rengi daha büyük bir alanda göstermek için beyaz bir resim oluştur
image_low = np.full((200, 200, 3), (255, 255, 255), dtype=np.uint8)
image_low[50:150, 50:150] = color_bgr_low  # Kırmızı rengi ortaya yerleştir

# Higher Rengi daha büyük bir alanda göstermek için beyaz bir resim oluştur
image_high = np.full((200, 200, 3), (255, 255, 255), dtype=np.uint8)
image_high[50:150, 50:150] = color_bgr_high  # Kırmızı rengi ortaya yerleştir

# Rengi göster
cv2.imshow('Low Color', image_low)
cv2.imshow('High Color', image_high)
cv2.waitKey(0)
cv2.destroyAllWindows()
