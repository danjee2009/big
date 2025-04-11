import tkinter as tk
from tkinter import ttk

# 메인 윈도우
win = tk.Tk()
win.title("메인 창")
win.geometry("300x200")

def plus_user_window():
    # 새로운 윈도우 생성
    plsu_window = tk.Toplevel(win)
    plsu_window.title("새 창")
    plsu_window.geometry("200x150")
    
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

# 버튼으로 새 창 열기
open_btn = ttk.Button(win, text="회원 가입하기", command=plus_user_window)
open_btn.pack(pady=50)

win.mainloop()
