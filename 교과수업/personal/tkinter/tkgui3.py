import tkinter as tk
window=tk.Tk()
window.title('ha')
window.geometry('500x500')

def math():
    label.config(text="result=" + listbox.get())
    
entry=tk.Entry(window)
entry.pack()

label=tk.Label(window, text='hallo')
label.pack()

button=tk.Button(text='hihi', command=math)
button.pack()

listbox=tk.Listbox(window, selectmode='extended')
listbox.insert(0, '1번')
listbox.insert(1, '2번')
listbox.insert(2, '3번')
listbox.pack()




check=tk.Checkbutton(window, text='1')

window.mainloop()