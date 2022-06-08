from random import *
from tkinter import *
import os

root = Tk()
root.title('WordCraft')
root.attributes('-fullscreen', True)

# Functions
def click(letter):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, (current + letter))

def caps(event):
    enteredText.set(enteredText.get().upper())

def limit(*args):
    value = enteredText.get()
    if len(value) > 7: enteredText.set(value[:7])

def nextLevel():
    pass
    # os.system("py WordCraft/Source_Code/--FILLER--.py")

def toQuotes():
    pass
    # os.system("py WordCraft/Source_Code/--FILLER--.py")

def submitValues():
    entered = enteredText.get()
    if entered == "PALAZZO":
        pop = Tk()
        root.destroy()
        pop.attributes('-fullscreen', True)
        pop['bg'] = '#ebf8ff'
        pop.title(" ")
        greet = Label(pop, text="CONGRATULATIONS!!!", font=("", 40), width=44, bg="#ebf8ff")
        greet.grid(row=1, column=1, columnspan=2, pady=100)
        Label(pop, text="You've completed the level!", font=("", 18), bg="#ebf8ff").grid(row=2, column=0, columnspan=3, rowspan=2, pady=90)
        Button(pop, text="To Hidden Quote", font=("", 17), bg="#38b6ff", fg="white" ,width=18, height=2, command=nextLevel).grid(row=4,column=1, pady=20)
        Button(pop, text="Next Level", font=("", 17), bg="#38b6ff", fg="white" ,width=18, height=2, command=toQuotes).grid(row=4, column=2, pady=20)

    else:
        pop = Tk()
        pop.title(" ")
        pop.attributes('-fullscreen', True)
        pop.after(2500, pop.destroy)
        message = Label(pop, text="Please try again", font=("", 50))
        message1 = Label(pop, text="You will be back in a few seconds")
        message.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        message1.place(relx=0.5, rely = 0.6, anchor= CENTER)

def backspace():
    currentText = e1.get()
    e1.delete(0,END)
    last = len(currentText)
    last = last - 1
    words = list(currentText)
    words.pop(last)
    new = ''.join(words)
    e1.insert(0, new)   

def shuffles():
    remain = e1.get()
    root.destroy()
    os.system("py WordCraft/Source_Code/Main_Game.py")
    e1.insert(0, remain)

def howTo():
    os.system("py WordCraft/Source_Code/How_To_Play.py")

# Just fillers
filler1 = Label(root, text=" ", height=4)
filler2 = Label(root, text=" ")
filler3 = Label(root, text=" ")
filler4 = Label(root, text=" ")
filler5 = Label(root, text=" ")

# Assets
hintImage = PhotoImage(file='WordCraft/Assets/Hint_Icon.png')
reshuffleImage = PhotoImage(file='WordCraft/Assets/Reshuffle_Icon.png')
bg = PhotoImage(file = "WordCraft/Assets/Background.png")

# Content
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
level = Label(          root, text="Level 37",                                           font=("", 35),  height=4,                                   bg="#ebf8ff")
hintButton = Button(    root, image=hintImage,                                          borderwidth=0,  height=150,                                 bg="#ebf8ff")
reshuffle = Button(     root, image=reshuffleImage,                                     borderwidth=0,  height=150,             command=shuffles,   bg="#ebf8ff")
toLevels = Button(      root, text="To levels",                                         font=("", 18),              width=15,                       bg="white"  )
howToPlay = Button(     root, text="How to play",                                       font=("", 18),              width=15,   command=howTo,      bg="white"  )
question = Label(       root, text="An impressive public building \n or private residence", font=("", 25),                                              bg="#cce9f8")

# Input
enteredText = StringVar()
enteredText.trace('w', limit)
e1 = StringVar()
e1 = Entry(root, width=30, borderwidth=5, font=("", 25), justify=CENTER, textvariable=enteredText)
e1.bind("<KeyRelease>", caps)

root.bind("<BackSpace>",lambda event: backspace())
root.bind("<Return>", lambda event: submitValues())

# Letters
randomNumbers = sample(range(5,12), 7)
e = Button(root, text="P", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("P"))
m = Button(root, text="A", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("A"))
p = Button(root, text="L", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("L"))
a = Button(root, text="A", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("A"))
t = Button(root, text="Z", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("Z"))
h = Button(root, text="Z", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("Z"))
y = Button(root, text="O", font=("Time", 15), fg="#F3F3F3", bg="#38b6ff", height=2, width=5, command=lambda: click("O"))

#========================== Screen location ==========================#

filler1.grid(   row=0, column=0,    padx=50)
filler2.grid(   row=0, column=1,                            columnspan=2)
level.grid(     row=1, column=1,                            columnspan=2)
hintButton.grid(row=2, column=1)
reshuffle.grid( row=2, column=2)
toLevels.grid(  row=4, column=1,                pady=25,    columnspan=2)
howToPlay.grid( row=5, column=1,                            columnspan=2)
filler3.grid(   row=0, column=3,    padx=100)
filler4.grid(   row=0, column=4,    padx=25)
question.grid(  row=0, column=5,                            columnspan=7, rowspan=2)
filler5.grid(   row=0, column=12,   padx=25)
e1.grid(        row=2, column=5,                            columnspan=7)

e.grid(         row=5 ,column=randomNumbers[0])
m.grid(         row=5 ,column=randomNumbers[1])
p.grid(         row=5 ,column=randomNumbers[2])
a.grid(         row=5 ,column=randomNumbers[3])
t.grid(         row=5 ,column=randomNumbers[4])
h.grid(         row=5 ,column=randomNumbers[5])
y.grid(         row=5 ,column=randomNumbers[6])

root.mainloop()