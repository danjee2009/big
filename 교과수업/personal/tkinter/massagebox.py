import tkinter as tk
import tkinter.messagebox as box
win=tk.Tk()
win.title('hi')
win.geometry('500x500')
win.resizable(True,True)

def sb():
    box.showinfo(li)
def tx():
    button.config(text=li)

entry=tk.Entry(win)
entry.pack()

input_list=entry.get()

li=[]

for i in range(len(input_list)):
    li.append(input_list[i])

for i in range(len(input_list)):
    li[i]=int(li[i])

button2=tk.Button(text='hh', command=tx)
button2.pack()
    
button=tk.Button(win,command=sb)
button.pack()


label=tk.Label(win,text='hi')
label.pack()
win.mainloop()