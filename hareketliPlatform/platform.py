#### Imports
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

#### Modules
from platformCapture import capture_and_process_image
from platformMove import moveRobot

class RobotControlUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Platform Kontrol Sistemi")

        self.start_button = ttk.Button(root, text="Platformu Başlat", command=self.platform_initial)
        self.start_button.pack(pady=10)

        # Video gösterimi için bir frame
        self.video_frame = tk.Frame(root)
        self.video_frame.pack(padx=10, pady=10)

        # Video görüntüsünü göstermek için bir canvas
        self.canvas = tk.Canvas(self.video_frame)
        self.canvas.pack()

    def platform_initial(self):

        # Kırmızı nesne pozisyonunu al
        position_result = capture_and_process_image()

        #print("Nesne Pozisyonu", position_result)
        #moveRobot(position_result)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotControlUI(root)
    root.mainloop()
