import tkinter as tk
import random as rd

win = tk.Tk()
win.title('lotto')
win.geometry('500x500')
win.resizable(True, True)

lli = []

# Entry 위젯들을 리스트로 저장
entries = []

for i in range(7):
    entry = tk.Entry(win, width=3)
    entry.grid(row=0, column=i)
    entries.append(entry)

# 버튼 클릭 시 Entry값을 lli에 저장하는 함수
def get_values():
    lli.clear()  # 기존 데이터 초기화 (필요하다면)
    for entry in entries:
        value = entry.get()
        if value.isdigit():
            lli.append(int(value))
        else:
            lli.append(value)  # 숫자가 아닐 경우 그냥 문자열로 저장
    print("입력값 리스트:", lli)

# 저장 버튼 추가
btn = tk.Button(win, text="저장", command=get_values)
btn.grid(row=1, column=0, columnspan=7)

win.mainloop()
