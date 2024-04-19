#### Imports
import tkinter as tk
from tkinter import ttk

#### Modules
from platformCapture import capture_and_process_image
from platformMove import moveRobot

class RobotControlUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Platform Kontrol Sistemi")

        self.start_button = ttk.Button(root, text="Platformu Başlat", command=self.platform_start)
        self.start_button.pack(pady=10)

    def platform_start(self):

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

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotControlUI(root)
    root.mainloop()
