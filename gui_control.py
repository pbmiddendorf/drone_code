# -*- coding: utf-8 -*-
import Tkinter as tk
import cv2
from PIL import Image, ImageTk
from ctypes import windll, Structure, c_long, byref

def return_to_home():
    print "return to home"
    # TODO return to home functions
    
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def location_init():
    location_label = tk.Label(root, text="Location:")
    location_label.pack()
    location_value = tk.Label(root, text="40.446°N 79.982°W")
    location_value.pack()

def button_init():
    b = tk.Button(root, text="Return To Home", command=return_to_home, background="#ff0000")
    b.pack()
    
def heading_init():
    heading_label = tk.Label(root, text="Heading:")
    heading_label.pack()
    heading.set(0)
    heading_value = tk.Label(root, textvariable = heading)
    heading_value.pack()
    
if __name__ == "__main__" :

    width, height = 800, 600
    cap = cv2.VideoCapture(0)
    # TODO replace webcam capture with wifi camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    root = tk.Tk()
    root.bind('<Escape>', lambda e: root.quit())
    lmain = tk.Label(root)
    lmain.pack()
    heading = tk.IntVar()
    heading_init()
    location_init()
    button_init()
    
    show_frame()

    while 1:
    # main gui update loop
        heading.set(100)
        root.update()
