import cv2
import matplotlib.pyplot as plt
import numpy as np  # NumPy kütüphanesini ekleyin

# Görüntüyü yükle
image_path = "src\piphototest\cropped_image.jpg"  # Kullanmak istediğiniz görüntünün yolunu belirtin
image = cv2.imread(image_path)

# Görüntünün genişliği ve yüksekliği
height, width = image.shape[:2]

# Matplotlib penceresini oluştur
plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Image with RGB values")

# Fare olaylarını dinleme fonksiyonu
def onMouseMove(event):
    if event.xdata is not None and event.ydata is not None:
        x = int(event.xdata)
        y = int(event.ydata)
        
        # Fare imlecinin konumundaki pikselin BGR değerlerini al
        b, g, r = image[y, x]
        
        # RGB değerlerini ekrana yazdır
        print("RGB values (x, y): ({}, {}) -> R: {}, G: {}, B: {}".format(x, y, r, g, b))
        
        # HSV renk uzayına dönüştür
        hsv_pixel = cv2.cvtColor(np.uint8([[image[y, x]]]), cv2.COLOR_BGR2HSV)
        h, s, v = hsv_pixel[0][0]
        
        # HSV değerlerini ekrana yazdır
        print("HSV values (x, y): ({}, {}) -> H: {}, S: {}, V: {}".format(x, y, h, s, v))

# Matplotlib penceresine fare olaylarını bağlama
plt.connect('motion_notify_event', onMouseMove)

# Matplotlib penceresini göster
plt.show()
