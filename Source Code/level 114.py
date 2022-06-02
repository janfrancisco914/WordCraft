from random import *
from tkinter import *

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

def limitSizeDay(*args):
    value = enteredText.get()
    if len(value) > 7: enteredText.set(value[:7])

def submitValues():
    entered = enteredText.get()
    if entered == "TANKFUL":
        global pop
        pop = Tk()
        pop.attributes('-fullscreen', True)
        pop.title(" ")
        pop.eval('tk::PlaceWindow . center')
        greet = Label(pop, text="CONGRATULATIONS", font=("", 40))
        greet.pack(pady=40)
    else:
        pop = Tk()
        pop.title(" ")
        pop.attributes('-fullscreen', True)
        pop.after(3000, pop.destroy)
        message = Label(pop, text="Please try again", font=("", 50))
        message1 = Label(pop, text="You will be back in a few seconds")
        message.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        message1.place(relx=0.5, rely = 0.6, anchor= CENTER)

# Just fillers
filler1 = Label(root, text=" ", height=4)
filler2 = Label(root, text=" ")
filler3 = Label(root, text=" ")
filler4 = Label(root, text=" ")
filler5 = Label(root, text=" ")

# Assets
hintImage = PhotoImage(file='WordCraft/Assets/Hint Icon.png')
reshuffleImage = PhotoImage(file='WordCraft/Assets/Reshuffle Icon.png')

# Content
level = Label(          root, text="Level 114",                                           font=("", 35),  height=4)
hintButton = Button(    root, image=hintImage,                                          borderwidth=0,  height=150)
reshuffle = Button(     root, image=reshuffleImage,                                     borderwidth=0,  height=150)
toLevels = Button(      root, text="To levels",                                         font=("", 18),              width=15)
howToPlay = Button(     root, text="How to play",                                       font=("", 18),              width=15)
question = Label(       root, text="The amount a tank can hold", font=("", 25))

# Input
enteredText = StringVar()
enteredText.trace('w', limitSizeDay)
e1 = Entry(root, width=30, borderwidth=5, font=("", 25), justify=CENTER, textvariable=enteredText)
e1.bind("<KeyRelease>", caps)

# Button
root.bind("<Return>", lambda event: submitValues())

# Buttons
randomNumbers = sample(range(5,12), 7)
e = Button(root, text="T", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("T"))
m = Button(root, text="A", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("A"))
p = Button(root, text="N", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("N"))
a = Button(root, text="K", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("K"))
t = Button(root, text="F", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("F"))
h = Button(root, text="U", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("U"))
y = Button(root, text="L", font=("Time", 15), fg="#F3F3F3", bg="#5b5b5b", height=2, width=5, command=lambda: click("L"))

#========================== Screen location ==========================#

filler1.grid(   row=0, column=0,    padx=50)
filler2.grid(   row=0, column=1,                            columnspan=2)
level.grid(     row=1, column=1,                            columnspan=2)
hintButton.grid(row=2, column=1)
reshuffle.grid( row=2, column=2)
toLevels.grid(  row=4, column=1,                pady=25,    columnspan=2)
howToPlay.grid( row=5, column=1,                            columnspan=2)
filler3.grid(   row=0, column=3,    padx=50)
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