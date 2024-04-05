import cv2
import matplotlib.pyplot as plt

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
def onMouseMove(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Fare imlecinin konumundaki pikselin BGR değerlerini al
        b, g, r = image[y, x]
        # RGB değerlerini ekrana yazdır
        print("RGB değerleri (x, y): ({}, {}) -> R: {}, G: {}, B: {}".format(x, y, r, g, b))

# Matplotlib penceresine fare olaylarını bağlama
plt.connect('motion_notify_event', onMouseMove)

# Matplotlib penceresini göster
plt.show()
