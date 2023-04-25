from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

tela = tk.Tk()
tela.geometry("1280x720")
tela.resizable(True, True)
tela.maxsize(width=1280, height=720)
tela.minsize(width=1280, height=720)
tela.configure(background="#FFFFFF")

dogImg = Image.open("./img/dogImage.png")
dogImage = ImageTk.PhotoImage(dogImg)

dogImg = tk.Label(tela,image=dogImage )
dogImg.grid(row=0, column=1, rowspan=2, sticky="e",padx=110,pady=10)

nameDog = Entry(tela, width=29)
nameDog.grid(row=0, column=0   )

tela.grid_rowconfigure(0, weight=1)
tela.grid_rowconfigure(1, weight=1)
tela.grid_columnconfigure(0, weight=1)
tela.grid_columnconfigure(1, weight=1)
tela.mainloop()

