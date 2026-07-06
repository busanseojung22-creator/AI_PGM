import tkinter as tk
from tkinter import messagebox

# 버튼 클릭
def click(value):
    entry.insert(tk.END, value)

# 초기화
def clear():
    entry.delete(0, tk.END)

# 계산
def calculate():
    try:
        expression = entry.get()
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except ZeroDivisionError:
        messagebox.showerror("오류", "0으로 나눌 수 없습니다.")
        clear()

    except Exception:
        messagebox.showerror("오류", "잘못된 식입니다.")
        clear()


# -----------------------
# 메인 창
# -----------------------

window = tk.Tk()
window.title("계산기")
window.geometry("350x500")

# 창 크기 변경 허용
window.resizable(True, True)

# 행과 열이 함께 늘어나도록 설정
for i in range(6):
    window.rowconfigure(i, weight=1)

for j in range(4):
    window.columnconfigure(j, weight=1)


# 입력창
entry = tk.Entry(
    window,
    font=("맑은 고딕", 24),
    justify="right"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
)

# C 버튼
clear_btn = tk.Button(
    window,
    text="C",
    font=("맑은 고딕", 18),
    command=clear
)

clear_btn.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
)

buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# 버튼 생성
for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = calculate
        else:
            cmd = lambda t=text: click(t)

        btn = tk.Button(
            window,
            text=text,
            font=("맑은 고딕", 18),
            command=cmd
        )

        btn.grid(
            row=r+2,
            column=c,
            sticky="nsew",   # 셀 전체를 채움
            padx=5,
            pady=5
        )

window.mainloop()