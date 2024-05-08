import tkinter as tk
import cv2
from PIL import Image, ImageTk

#### Modules
from platformCapture import capture_and_process_image
from platformMove import moveRobot

class PlatformControlUI:
    def __init__(self, root):
        self.root = root
        self.root.title("3 SERBESTLİK DERECELİ HAREKETLİ PLATFORM")

        # Başlık etiketi
        title_label = tk.Label(root, text="3 SERBESTLİK DERECELİ HAREKETLİ PLATFORM", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Butonlar
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        button1 = tk.Button(button_frame, text="Platformu Başlat", command=self.funcStart, width=40)
        button1.grid(row=0, column=0, columnspan=12, pady=5)

        button2 = tk.Button(button_frame, text="Platformu Sıfırla", command=lambda: self.funcPos(4), width=40)
        button2.grid(row=1, column=0, columnspan=12, pady=5)

        button5 = tk.Button(button_frame, text="Poz 1", command=lambda: self.funcPos(1))
        button5.grid(row=2, column=0, padx=5, pady=5)

        button6 = tk.Button(button_frame, text="Poz 2", command=lambda: self.funcPos(2))
        button6.grid(row=2, column=1, padx=5, pady=5)

        button7 = tk.Button(button_frame, text="Poz 3", command=lambda: self.funcPos(3))
        button7.grid(row=2, column=2, padx=5, pady=5)

        # Kamera görüntüsü
        self.camera_label = tk.Label(root)
        self.camera_label.pack(side=tk.RIGHT, padx=10)

        # Kamera görüntüsünün başlatılması
        self.start_camera()

    def start_camera(self):
        # Kamerayı başlatmak için cv2 kullanımı
        cap = cv2.VideoCapture(0)

        def show_frame():
            ret, frame = cap.read()
            if ret:
                # OpenCV'den PIL formatına dönüşüm
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                self.camera_label.imgtk = imgtk
                self.camera_label.config(image=imgtk)
            self.camera_label.after(10, show_frame)

        show_frame()

    # Buton fonksiyonları
    def funcStart(self):
        print("Platform İlk Pozisyona Getiriliyor...")
        moveRobot(5)
        moveRobot(4)

        # Kırmızı nesne pozisyonunu al
        position_result = capture_and_process_image()

        # Nesnenin pozisyonuna göre robotu kontrol et
        if position_result == 1:
            print("Nesne 1. Pozisyonda")
            moveRobot(1)
        elif position_result == 2:
            print("Nesne 2. Pozisyonda")
            moveRobot(2)
        elif position_result == 3:
            print("Nesne 3. Pozisyonda")
            moveRobot(3)
        else:
            print("Nesne Bulunamadi.")

        # 10 milisaniye beklet
        self.root.after(10)

    def funcPos(self, posNo):
        # İşlev 2
        if posNo == 1: #Pos1
            print("Hareket 1. Konuma göre gerçekleştiriliyor. ")
            moveRobot(1)

        elif posNo == 2: #Pos2
            print("Hareket 2. Konuma göre gerçekleştiriliyor. ")
            moveRobot(2)

        elif posNo == 3: #Pos3
            print("Hareket 3. Konuma göre gerçekleştiriliyor. ")
            moveRobot(3)

        elif posNo == 4: #Reset
            print("Platform Sifirlaniyor...")
            moveRobot(4)

        else:
            print("Komut Giriniz.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlatformControlUI(root)
    root.mainloop()
