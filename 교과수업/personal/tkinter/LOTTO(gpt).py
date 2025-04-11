import tkinter as tk
import random as rd

win = tk.Tk()
win.title('lotto')
win.geometry('500x500')
win.resizable(True, True)

lli = []
entries = []

# Entry 위젯 생성
for i in range(7):
    entry = tk.Entry(win, width=3)
    entry.grid(row=0, column=i)
    entries.append(entry)

# 랜덤 정답 번호
loli = range(1, 100)
bli = rd.sample(loli, 7)
print("정답 번호:", bli)  # 디버깅용

# 레이블: 결과 출력
label1 = tk.Label(win)
label1.place(x=70, y=70)

# 버튼 클릭 시 Entry 값 저장 + 정답 비교 + 출력
def check_answers():
    lli.clear()
    for entry in entries:
        value = entry.get()
        if value.isdigit():
            lli.append(int(value))
        else:
            lli.append(None)  # 숫자가 아니면 None 처리
    
    print("입력값 리스트:", lli)

    # 정답과 비교
    count = 0
    for i in range(len(lli)):
        if isinstance(lli[i], int) and lli[i] == bli[i]:
            count += 1

    label1.config(text=f"정답 개수: {count}")

# 확인 버튼
btn = tk.Button(win, text="확인", command=check_answers)
btn.grid(row=1, column=0, columnspan=7)

win.mainloop()
#이코드의 핵심은 반복문을 사용해 엔트리 7개를 간단하게 만드는 것과 각 엔트리의 값을 리스트에 넣는 것이다.

# 중복 입력 제한
# 리스트를 세트화해 중복된 값을 하나만 남긴다
# 만약 리스트가 세트화한 리스트와 같다면 중복이 없음
# 만약 차이가 있을 시 중복이 있다 판단, 오류 문장 출력

# def check_lotto():
#     user_nums = []

#     for entry in entries:
#         val = entry.get()
#         if val.isdigit():
#             num = int(val)
#             if 1 <= num <= 99:
#                 user_nums.append(num)

#     # 중복 체크
#     if len(user_nums) != len(set(user_nums)):
#         label_result.config(text="⚠️ 중복된 숫자가 있습니다. 다시 입력해주세요.")
#         return

#     user_nums = list(set(user_nums))  # 중복 제거 (예외처리 대신 이 줄만 써도 OK)

#     matched = [num for num in user_nums if num in bli]
#     count = len(matched)

#     result_text = f"당첨 번호: {sorted(bli)}\n입력한 번호: {sorted(user_nums)}\n맞춘 개수: {count}개"
#     label_result.config(text=result_text)
