import tkinter
import time
colorslist = ["white","yellow", "orange", "red", "purple", "black"]
size = 150
y = 0
z = len (colorslist)


def updateTheScreen():
    global size, window, y, z
    if z != 0:
        window.geometry(str(size) +"x"+ str(size))
        size = int(size) + 50
        window.configure(bg=colorslist[y])
        y = y + 1
        print(z)
        z = z - 1
    else:
        print("BOOM!")
        window.destroy()


window = tkinter.Tk()

window.title("My first window")



for x in range(0,len(colorslist) + 1):
    window.after(x* 1000, updateTheScreen)




window.mainloop()