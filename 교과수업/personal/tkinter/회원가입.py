import tkinter as tk

win=tk.Tk()
win.title('회원 가입')
win.geometry('500x500')
win.resizable(True,True)

infodic={}

def idpw():
    eid=identry.get()
    epw=pwentry.get()
    infodic[eid]=epw
    show.config(text=infodic)

idlabel=tk.Label(win, text='아이디 입력')
idlabel.pack()

identry=tk.Entry(win)
identry.pack()

pwlabel=tk.Label(win,text='비밀번호를 입력하세요')
pwlabel.pack()

pwentry=tk.Entry(win)
pwentry.pack()

button=tk.Button(win,text='회원 가입',command=idpw)
button.pack()

show=tk.Label(win)
show.pack()
win.mainloop()