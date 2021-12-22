import tkinter as tk
from datetime import datetime
now = datetime.now()
current_Time = now.strftime("%H:%M:%S")
def update():
    now = datetime.now()
    current_Time = now.strftime("%H:%M:%S")
    l.config(text=str(current_Time))
    root.after(1000, update)

root = tk.Tk()
l = tk.Label(text=current_Time,fg='#FFB81C', font=("Comic Sans MS", 30))
l.pack()
l.configure(bg='#000080')
root.after(1000, update)
root.mainloop()