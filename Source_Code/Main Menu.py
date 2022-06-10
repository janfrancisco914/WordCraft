from cgi import test
from ctypes import resize
from email.mime import image
from tkinter import *
import tkinter as tk
# from winsound import PlaySound
from PIL import ImageTk, Image
# from PIL.Image import LANCZOS


w = 600
h = 400
x = w/2
y = h/2

root = Tk()
root.title('WordCraft')
root.geometry("1080x720")

icon = PhotoImage(file='c:/images/icon.png')
root.iconphoto(True,icon)



my_pic = ImageTk.PhotoImage(file='./images/menu_background.png')

my_label = Label(root, image=my_pic)
my_label.grid(row=0, column=1)

play = Image.open('./images/play.png')
settings = Image.open('./images/settings.png')
reminders = Image.open('./images/reminders.png')
market = Image.open('./images/market.png')
gift = Image.open('./images/gift.png')

play_resize = play.resize((350, 200))
settings_resize = settings.resize((150, 100))
reminders_resize = reminders.resize((52, 56))
market_resize = market.resize((150, 100))
gift_resize = gift.resize((150, 100))

play_converted = ImageTk.PhotoImage(play_resize)
settings_converted = ImageTk.PhotoImage(settings_resize)
reminders_converted = ImageTk.PhotoImage(reminders_resize)
market_converted = ImageTk.PhotoImage(market_resize)
gift_converted = ImageTk.PhotoImage(gift_resize)

play_block = Button(root,
                   image = play_converted,
                   borderwidth=0)
play_block.grid(row= 2, column= 1)

settings_block = Button(root,
                   image = settings_converted, borderwidth=0)
settings_block.grid(row= 2, column= 0)


market_block = Button(root,
                   image = market_converted, borderwidth=0)
market_block.grid(row= 2, column= 2)

gift_block = Button(root,
                   image = gift_converted, borderwidth=0)
gift_block.grid(row= 3, column= 1)



root.mainloop()