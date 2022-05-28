from random import *
from tkinter import *

root = Tk()
root.title('WordCraft')
root.geometry('1300x690')

# Functions
def click(letter):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, (current + letter))

def caps(event):
    v.set(v.get().upper())

# Just fillers
filler1 = Label(root, text=" ")
filler2 = Label(root, text=" ", height=4)
filler3 = Label(root, text=" ")
filler4 = Label(root, text=" ")
filler5 = Label(root, text=" ")

# Assets
hintImage = PhotoImage(file='WordCraft/Assets/Hint Icon.png')
reshuffleImage = PhotoImage(file='WordCraft/Assets/Reshuffle Icon.png')

# Content
level = Label(          root, text="Level 1",                                           font=("", 35),  height=4)
hintButton = Button(    root, image=hintImage,                                          borderwidth=0,  height=150)
reshuffle = Button(     root, image=reshuffleImage,                                     borderwidth=0,  height=150)
toLevels = Button(      root, text="To levels",                                         font=("", 18),              width=15)
howToPlay = Button(     root, text="How to play",                                       font=("", 18),              width=15)
question = Label(       root, text="Concise and exact use of words in writing", font=("", 25))

v = StringVar()
e1 = Entry(root, width=30, borderwidth=5, font=("", 25), justify=CENTER, textvariable=v)
e1.bind("<KeyRelease>", caps)

b = Button(root, text="B", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("B"))
r = Button(root, text="R", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("R"))
e = Button(root, text="E", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("E"))
v = Button(root, text="V", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("V"))
i = Button(root, text="I", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("I"))
t = Button(root, text="T", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("T"))
y = Button(root, text="Y", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("Y"))

#========================== Screen location ==========================#

filler1.grid(   row=0, column=0,    padx=50)
filler2.grid(   row=0, column=1,                            columnspan=2)
level.grid(     row=1, column=1,                            columnspan=2)
hintButton.grid(row=2, column=1)
reshuffle.grid( row=2, column=2)
toLevels.grid(  row=3, column=1,                pady=25,    columnspan=2)
howToPlay.grid( row=4, column=1,                            columnspan=2)
filler3.grid(   row=0, column=3,    padx=50)
filler4.grid(   row=0, column=4,    padx=25)
question.grid(  row=0, column=5,                            columnspan=7, rowspan=2)
filler5.grid(   row=0, column=12,   padx=25)

e1.grid(         row=2, column=5, columnspan=7)

randomNumbers = sample(range(5,12), 7)
b.grid(         row=4, column=randomNumbers[0])
r.grid(         row=4, column=randomNumbers[1])
e.grid(         row=4, column=randomNumbers[2])
v.grid(         row=4, column=randomNumbers[3])
i.grid(         row=4, column=randomNumbers[4])
t.grid(         row=4, column=randomNumbers[5])
y.grid(         row=4, column=randomNumbers[6])

root.mainloop()