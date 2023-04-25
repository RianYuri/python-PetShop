from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as font 

tela = tk.Tk()
tela.geometry("1280x720")
tela.resizable(True, True)
tela.maxsize(width=1280, height=720)
tela.minsize(width=1280, height=720)
tela.configure(background="#FFFFFF")

caminho_fonte = "./fonts/Londrina_Shadow/LondrinaShadow-Regular.ttf"


fontePetshop = tk.font.Font(family="Londrina Shadow", size=84)
texto_label = tk.Label(tela, text="PetShop Dog’s", font=fontePetshop)
texto_label.configure(background='white')
texto_label.grid(row=0, column=0, rowspan=2,columnspan=2, sticky="nw", pady=181, padx=61)
 
topImge = Image.open("./img/topImage.png")
imagem_tk = ImageTk.PhotoImage(topImge)
topImageDog = tk.Label(tela, image=imagem_tk)

dogImge = Image.open("./img/dogImage.png")
dogImage = ImageTk.PhotoImage(dogImge)
dogImg = tk.Label(tela,image=dogImage )

bottomImge = Image.open("./img/bottomImg.png")
dog_bottom = ImageTk.PhotoImage(bottomImge)
bottomImageDog = tk.Label(tela, image=dog_bottom)

dogImg.grid(row=0, column=1, rowspan=2, sticky="e",padx=110,pady=10)
topImageDog.grid(row=0, column=0, columnspan=2, sticky="n")
bottomImageDog.grid(row=1, column=1, sticky="se", padx=0, pady=10)

tela.grid_rowconfigure(0, weight=1)
tela.grid_rowconfigure(1, weight=1)
tela.grid_columnconfigure(0, weight=1)
tela.grid_columnconfigure(1, weight=1)

tela.mainloop()
