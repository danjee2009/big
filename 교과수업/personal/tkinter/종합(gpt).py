import tkinter as tk

# 회원 정보를 저장할 딕셔너리
infodic = {}

# 회원가입 창 열기
def open_signup_window():
    signup_win = tk.Toplevel(win)
    signup_win.title("회원가입")
    signup_win.geometry("300x200")

    tk.Label(signup_win, text="아이디 입력").pack()
    id_entry = tk.Entry(signup_win)
    id_entry.pack()

    tk.Label(signup_win, text="비밀번호 입력").pack()
    pw_entry = tk.Entry(signup_win, show="*")
    pw_entry.pack()

    def register():
        eid = id_entry.get()
        epw = pw_entry.get()
        if eid and epw:
            if eid in infodic:
                status_label.config(text="이미 존재하는 아이디입니다.")
            else:
                infodic[eid] = epw
                status_label.config(text=f"{eid}님 가입 완료!")
                signup_win.destroy()
        else:
            status_label.config(text="ID와 PW를 모두 입력하세요.")

    tk.Button(signup_win, text="가입", command=register).pack(pady=10)

# 로그인 처리
def login():
    lid = login_id_entry.get()
    lpw = login_pw_entry.get()
    if lid in infodic and infodic[lid] == lpw:
        status_label.config(text=f"{lid}님 로그인 성공!")
    else:
        status_label.config(text="로그인 실패: 아이디 또는 비밀번호 오류")

# 메인 창
win = tk.Tk()
win.title("로그인/회원가입")
win.geometry("300x300")

# 로그인 입력창
tk.Label(win, text="로그인 아이디").pack()
login_id_entry = tk.Entry(win)
login_id_entry.pack()

tk.Label(win, text="로그인 비밀번호").pack()
login_pw_entry = tk.Entry(win, show="*")
login_pw_entry.pack()

tk.Button(win, text="로그인", command=login).pack(pady=10)

# 회원가입 버튼
tk.Button(win, text="회원가입", command=open_signup_window).pack()

# 상태 메시지
status_label = tk.Label(win, text="")
status_label.pack(pady=20)

win.mainloop()
