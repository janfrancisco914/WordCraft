from tkinter import *

new = Tk()
new.title('WordCraft')
new.attributes('-fullscreen', True)
new['bg'] = '#ebf8ff'

def refresh():
    new.destroy()

text = Label(new, text="How to play", font=("", 20), height=4, width=85, bg="#ebf8ff")
text.grid(row=1,column=1, columnspan=2)

# Parts of the screen
Label(new, text="Parts of the screen", font=("", 15), height=2, bg="#ebf8ff").grid(row=2, column=1)
screenSample = PhotoImage(file='WordCraft/Assets/Levels_Screen.png')
image1 = Label(new, image=screenSample, pady=10)
image1.grid(row=3, column=1, rowspan=6)

# Mechanics
Label(new, text="Mechanics", font=("", 15), height=2, bg="#ebf8ff").grid(row=2, column=2)
Label(new, text="1. You need to answer the question/statement displayed in the screen", font=("", 12), bg="#ebf8ff").grid(row=3, column=2)
Label(new, text="2. There are boxes at the bottom which you can choose the letters to get the correct answer", font=("", 12), bg="#ebf8ff").grid(row=4, column=2)
Label(new, text="3. Your answer will be displayed at the entry field", font=("", 12), bg="#ebf8ff").grid(row=5, column=2)
Label(new, text="4. If you find it hard to get the answer, you can get help at the two buttons in the side bar which is the hint or reshuffle button", font=("", 12), wraplength=500, bg="#ebf8ff").grid(row=6, column=2, rowspan=2)
Label(new, text="5. To submit your answer, you just need to press Enter key", font=("", 12), bg="#ebf8ff").grid(row=8, column=2)

# Go back button
b = Button(new, text="Go Back", command=refresh, height=2, width=20, bg="#5189FF", fg="white", font=("", 12))
b.grid(row=9, column=1, columnspan=2 ,pady=40)

new.mainloop()