from tkinter import *
from random import randint
win = Tk()
win.title(" winner ")
win.geometry("500x500")


def pick():
    participant = ["sahar rezayi","ali faezi","sara ghafouri","sara roostayi", "ali faezi", "mehdi soloki", "ali dayi"]
    participant_set = set(participant)
    unique_participant = list(participant_set)
    our_number = len(unique_participant)-1
    rando = randint(0, our_number)
    winnerlabel = Label(win, text=unique_participant[rando], font=("mincho", 40, "bold"))
    winnerlabel.config(fg="red")
    winnerlabel.pack(pady=70)


toplabel = Label(win, text="who is the winner!", font=("Helvetica", 15))
toplabel.pack(pady=20)

winbutton = Button(win, text="pick a winner please", font=("Helvetica", 25), command=pick)
winbutton.pack(pady=10)

win.mainloop()
