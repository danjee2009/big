import tkinter as tk
win=tk.Tk()
win.title('after')
win.geometry('500x500')
win.resizable(True,True)
count=0
def time():
    count+=1
    label.config(text=count)

def time2():
    win.after(1000,time)

label=tk.Label(win,text='0sec')
label.pack()

button=tk.Button(win,command=time2)
button.pack()

win.mainloop()