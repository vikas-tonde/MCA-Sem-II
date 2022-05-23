import random
from tkinter import *
guess = 0
money=0
guessInput =None
checkButton=None
lbl3 = None
def check(number, guess):
    nLen = len(number)
    gLen = len(guess)
    if number == guess:
        return 100
    if number[0] in guess or number[1] in guess:
        return 10
    return 0

def checkClickHandler(turn):
    global guess, money
    guess=guessInput.get()
    n = str(random.randint(1, 99))
    money = money + check(n, guess)
    lbl3["text"]=f'Number was {n} \n Your current score is {money} RS'
    turn=turn-1
    guessInput.delete(0,END)
    if turn==0:
        checkButton["state"]=DISABLED


def createFrame(turn):
    global guessInput, money, lbl3, checkButton
    startButton["state"]=DISABLED
    frame = Frame(window)
    frame.grid(column=0, row=2)
    lbl2 = Label(frame, text="What is your guess :")
    lbl2.pack()
    lbl3= Label(frame,text="")
    lbl3.pack()
    guessInput = Entry(frame)
    guessInput.pack()
    checkButton= Button(frame, text="Check", command=lambda: checkClickHandler(turn))
    checkButton.pack()
    


window = Tk()
window.title("Lottery")
lbl1 = Label(window, text="How many times you want to play: ")
lbl1.grid(column=0, row=0)
turns = Entry(window)
turns.grid(column=1, row=0)
startButton = Button(window, text="Start", command=lambda: createFrame(int(turns.get())))
startButton.grid(column=0, row=1)
startButton.grid_anchor("center")


window.mainloop()
