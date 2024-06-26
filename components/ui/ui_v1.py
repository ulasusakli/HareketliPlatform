#### Imports
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

#### Modules
from components.archived.camera_archived.captureModule import capture_and_process_image
from components.archived.control_archived.moveRobotModule import moveRobot

class RobotControlUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Platform Kontrol Sistemi")
        self.start_button = ttk.Button(root, text="Platformu Başlat", command=self.start_platform)
        self.start_button.pack(pady=10)
        self.video_frame = tk.Frame(root)
        self.video_frame.pack(padx=10, pady=10)
        self.canvas = tk.Canvas(self.video_frame)
        self.canvas.pack()

    def start_platform(self):
        # Kamerayı başlat
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            # USB kameradan görüntüyü al
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = ImageTk.PhotoImage(img)
                # Canvas'a yeni görüntüyü yerleştir
                self.canvas.config(width=img.width(), height=img.height())
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
                # GUI'yi güncelle
                self.root.update()
                # Kırmızı nesne pozisyonunu al
                position_result = capture_and_process_image()
                # Nesnenin pozisyonuna göre robotu kontrol et
                if position_result == 1:
                    print("Nesne Birinci Pozisyonda")
                    moveRobot(1)
                elif position_result == 2:
                    print("Nesne İkinci Pozisyonda")
                    moveRobot(2)
                elif position_result == 3:
                    print("Nesne Üçüncü Pozisyonda")
                    moveRobot(3)
                else:
                    print("Nesne Bulunamadi.")
            self.root.after(10)
        cap.release()
if __name__ == "__main__":
    root = tk.Tk()
    app = RobotControlUI(root)
    root.mainloop()
