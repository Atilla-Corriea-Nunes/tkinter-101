from tkinter import *
window=Tk()
lbl=Label(window, text="Hello tkinter!", fg='#FFB81C', font=("Comic Sans MS", 30))
lbl.place(x=20, y=50)
lbl.configure(bg='#000080')
window.configure(bg='#4b5320')
window.title('Hello')
window.geometry("300x200+10+10")
window.mainloop()