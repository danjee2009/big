
import tkinter as tk

# 회원 정보를 저장할 딕셔너리
infodic = {}

# 회원가입 창 열기
def open_signup_window():
    signup_win = tk.Toplevel(win)
    signup_win.title("회원가입")
    signup_win.geometry("300x200")

    # ID/PW 입력 필드
    tk.Label(signup_win, text="아이디 입력").pack()
    id_entry = tk.Entry(signup_win)
    id_entry.pack()

    tk.Label(signup_win, text="비밀번호 입력").pack()
    pw_entry = tk.Entry(signup_win, show="*")
    pw_entry.pack()

    # 가입 처리 함수 (내부 함수로 정의)
    def register():
        eid = id_entry.get()
        epw = pw_entry.get()
        if eid and epw:
            infodic[eid] = epw
            status_label.config(text=f"{eid}님 가입 완료!")
            signup_win.destroy()
        else:
            status_label.config(text="ID와 PW를 모두 입력하세요.")

    tk.Button(signup_win, text="가입", command=register).pack(pady=10)

# 메인 창
win = tk.Tk()
win.title("메인 창")
win.geometry("300x200")

# 회원가입 버튼
signup_button = tk.Button(win, text="회원가입", command=open_signup_window)
signup_button.pack(pady=30)

# 상태 메시지 표시
status_label = tk.Label(win, text="")
status_label.pack()

win.mainloop()
