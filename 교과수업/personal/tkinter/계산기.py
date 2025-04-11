import tkinter as tk
win=tk.Tk()
win.title('new window')
win.geometry('500x500')
win.resizable(True,True)
 
label=tk.Label(win, text='계산 입력')
label.pack()
buttonc=tk.Button(win,text='c',width=5,height=4)
buttonc.place(x=50,y=150)

button1=tk.Button(win,text='1',width=5,height=4)
button1.place(x=150,y=150)

button2=tk.Button(win,text='2',width=5,height=4)
button2.place(x=250,y=150)

button3=tk.Button(win,text='3',width=5,height=4)
button3.place(x=350,y=150)

button4=tk.Button(win,text='4',width=5,height=4)
button4.place(x=150,y=250)

button5=tk.Button(win,text='5',width=5,height=4)
button5.place(x=250,y=250)

button6=tk.Button(win,text='6',width=5,height=4)
button6.place(x=350,y=250)

button7=tk.Button(win,text='7',width=5,height=4)
button7.place(x=150,y=350)

button8=tk.Button(win,text='8',width=5,height=4)
button8.place(x=250,y=350)

button9=tk.Button(win,text='9',width=5,height=4,)
button9.place(x=350,y=350)

button0=tk.Button(win,text='0',width=5,height=4)
button0.place(x=250,y=450)

buttonp=tk.Button(win,text='+',width=5,height=4)
buttonp.place(x=450,y=150)

buttonn=tk.Button(win,text='-',width=5,height=4)
buttonn.place(x=450,y=250)

buttonm=tk.Button(win,text='X',width=5,height=4)
buttonm.place(x=450,y=350)

buttond=tk.Button(win,text='/',width=5,height=4)
buttond.place(x=450,y=450)

win.mainloop()