import tkinter as tk
from tkinter import filedialog, messagebox


# ------------------------
# 함수
# ------------------------

current_file = None


def new_file():
    global current_file
    text.delete("1.0", tk.END)
    current_file = None
    window.title("새 메모 - 메모장")


def open_file():
    global current_file

    filename = filedialog.askopenfilename(
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )

    if filename:
        current_file = filename

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        text.delete("1.0", tk.END)
        text.insert(tk.END, content)

        window.title(filename)


def save_file():
    global current_file

    if current_file is None:
        save_as()
        return

    with open(current_file, "w", encoding="utf-8") as file:
        file.write(text.get("1.0", tk.END))

    messagebox.showinfo("저장", "저장되었습니다.")


def save_as():
    global current_file

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("텍스트 파일", "*.txt")]
    )

    if filename:
        current_file = filename
        save_file()


def exit_program():
    if messagebox.askyesno("종료", "메모장을 종료하시겠습니까?"):
        window.destroy()


# ------------------------
# 메인 창
# ------------------------

window = tk.Tk()
window.title("메모장")
window.geometry("800x600")

# 창이 커지면 같이 늘어나도록
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# 메뉴
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="파일", menu=file_menu)

file_menu.add_command(label="새로 만들기", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="다른 이름으로 저장", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="종료", command=exit_program)

# 편집 메뉴
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=edit_menu)

edit_menu.add_command(
    label="잘라내기",
    command=lambda: text.event_generate("<<Cut>>")
)

edit_menu.add_command(
    label="복사",
    command=lambda: text.event_generate("<<Copy>>")
)

edit_menu.add_command(
    label="붙여넣기",
    command=lambda: text.event_generate("<<Paste>>")
)

# 텍스트 영역
text = tk.Text(
    window,
    font=("맑은 고딕", 12),
    undo=True,
    wrap="word"
)

text.grid(row=0, column=0, sticky="nsew")

# 스크롤바
scroll = tk.Scrollbar(window, command=text.yview)
scroll.grid(row=0, column=1, sticky="ns")

text.config(yscrollcommand=scroll.set)

window.mainloop()