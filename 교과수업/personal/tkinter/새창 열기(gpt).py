import tkinter as tk
from tkinter import ttk

# 메인 윈도우
root = tk.Tk()
root.title("메인 창")
root.geometry("300x200")

def open_new_window():
    # 새로운 윈도우 생성
    new_window = tk.Toplevel(root)
    new_window.title("새 창")
    new_window.geometry("200x150")
    
    label = ttk.Label(new_window, text="이것은 새 창입니다!")
    label.pack(pady=20)

    close_btn = ttk.Button(new_window, text="닫기", command=new_window.destroy)
    close_btn.pack()

# 버튼으로 새 창 열기
open_btn = ttk.Button(root, text="새 창 열기", command=open_new_window)
open_btn.pack(pady=50)

root.mainloop()
