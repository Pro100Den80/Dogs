from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def show_image():



window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = Label(text='Загрузить изображение',compound=show_image)
label.pack(pady=10)
