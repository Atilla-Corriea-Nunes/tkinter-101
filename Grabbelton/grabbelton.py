import tkinter
import random

actionhasrun = False
wonitem = ""


def updateWindow():
    global wonitem, x, actionhasrun
    randomchoice = random.choice(grabbelton)
    for x in grabbelton:
        if x == randomchoice:
            grabbelton.remove(x)
            print(grabbelton)
            label = len(grabbelton)
            l.config(text=str("er zijn nog "+ str(label) + " item(s) in de grabbelton over"))
            wonitem.config(text=str("Gefeliciteerd, je hebt een '"+ str(x) +"' gegrabbeld!"))
            


grabbelton = ["Shrek", "Package of Dietz and wattson's Dietz nuts","The litteral sun","You get nothing, you lose, good day sir", "a picture of medusa (you turn to stone when you look at it)","a bottle of what looks like water but is actually an extremely deadly poison", "T H E  V O I D", "a picture proving that the flat earth is real", "a machine that automatically disintegrates any human babies in a 10 meter radius", "a clown that will follow you around and laugh hysterically at you every couple of hours"]

label = len(grabbelton)

window = tkinter.Tk()



l = tkinter.Label(text="er zijn nog "+ str(label) + " item(s) in de grabbelton over",fg='#FFB81C', font=("Comic Sans MS", 20))
l.pack()
l.configure(bg='#000080')

button = tkinter.Button(window)
button.configure(text="Grabbelen",command=updateWindow)
button.pack(padx=20, pady=20)

wonitem = tkinter.Label(text="",fg='#FFB81C', font=("Comic Sans MS", 20))
wonitem.pack()

window.title("Grabbelton")

window.mainloop()