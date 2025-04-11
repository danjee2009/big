import tkinter as tk
import random

win = tk.Tk()
win.title("좌석 자동 배정 + 자리 바꾸기")
win.geometry("500x400")

total_seats = 18
seats_per_row = [4, 4, 4, 4, 2]  # 줄마다 좌석 수
seat_buttons = {}
rows = []
seats_flat = []
clicked_seats = []

current_row = 0
current_seat_idx = 0
numbers_to_assign = list(range(1, total_seats + 1))
random.shuffle(numbers_to_assign)

# 자리 클릭 → 자리 교환 기능
def swap_seats(seat_id):
    if seat_id in clicked_seats:
        return
    clicked_seats.append(seat_id)
    seat_buttons[seat_id].config(bg="yellow")

    if len(clicked_seats) == 2:
        id1, id2 = clicked_seats
        btn1, btn2 = seat_buttons[id1], seat_buttons[id2]
        t1, t2 = btn1["text"], btn2["text"]
        btn1.config(text=t2, bg="lightgreen")
        btn2.config(text=t1, bg="lightgreen")
        clicked_seats.clear()

# 좌석 버튼 생성
seat_index = 1
for row_idx, count in enumerate(seats_per_row):
    row_buttons = []
    for col in range(count):
        seat_id = seat_index
        btn = tk.Button(
            win,
            text="",
            width=6,
            height=2,
            font=("맑은 고딕", 16, "bold"),
            bg="lightgray",
            command=lambda sid=seat_id: swap_seats(sid)
        )
        btn.grid(row=row_idx, column=col, padx=5, pady=5, sticky="nsew")
        seat_buttons[seat_id] = btn
        row_buttons.append(seat_id)
        seats_flat.append(seat_id)
        seat_index += 1
    rows.append(row_buttons)

# 한 줄씩 자동 배정
def assign_row():
    global current_row
    if current_row >= len(rows):
        status_label.config(text="모든 줄에 번호가 배정되었습니다.")
        return
    row = rows[current_row]
    for seat_id in row:
        if numbers_to_assign:
            number = numbers_to_assign.pop()
            btn = seat_buttons[seat_id]
            btn.config(text=str(number), bg="lightgreen", state="normal")
    current_row += 1
    win.after(1000, assign_row)

# 한 자리씩 자동 배정
def assign_next_seat():
    global current_seat_idx
    if current_seat_idx >= len(seats_flat):
        status_label.config(text="모든 좌석에 번호가 배정되었습니다.")
        return
    seat_id = seats_flat[current_seat_idx]
    if numbers_to_assign:
        number = numbers_to_assign.pop()
        btn = seat_buttons[seat_id]
        btn.config(text=str(number), bg="lightgreen", state="normal")
    current_seat_idx += 1
    win.after(1000, assign_next_seat)

# 초기화
def reset():
    global current_row, current_seat_idx, numbers_to_assign, clicked_seats
    current_row = 0
    current_seat_idx = 0
    clicked_seats = []
    numbers_to_assign = list(range(1, total_seats + 1))
    random.shuffle(numbers_to_assign)
    for btn in seat_buttons.values():
        btn.config(text="", bg="lightgray", state="normal")
    status_label.config(text="초기화 완료. 시작 버튼을 누르세요.")

# 버튼 영역
start_row_btn = tk.Button(win, text="한 줄씩 시작", command=assign_row)
start_row_btn.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=10)

start_seat_btn = tk.Button(win, text="한 자리씩 시작", command=assign_next_seat)
start_seat_btn.grid(row=5, column=2, columnspan=2, sticky="nsew", pady=10)

reset_btn = tk.Button(win, text="초기화", command=reset)
reset_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", pady=10)

# 상태 표시
status_label = tk.Label(win, text="좌석 두 개를 클릭하면 숫자가 서로 바뀝니다.")
status_label.grid(row=7, column=0, columnspan=4, pady=10, sticky="nsew")

# 창 반응형 설정
for r in range(8):
    win.grid_rowconfigure(r, weight=1)
for c in range(4):
    win.grid_columnconfigure(c, weight=1)

win.mainloop()
