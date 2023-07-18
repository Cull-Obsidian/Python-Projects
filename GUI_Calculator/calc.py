from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)

root = Tk()
root.geometry("350x500")
root.title("Calculator")
root.config(bg="#3b5998")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="Roboto 40 bold", justify=RIGHT, bd=0, bg="#ffffff", fg="#000000")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

button_frame = Frame(root, bg="#3b5998")

buttons = [
    ("C", "#D44638"),
    ("7", "#CCCCCC"),
    ("8", "#CCCCCC"),
    ("9", "#CCCCCC"),
    ("/", "#4267B2"),
    ("4", "#CCCCCC"),
    ("5", "#CCCCCC"),
    ("6", "#CCCCCC"),
    ("*", "#4267B2"),
    ("1", "#CCCCCC"),
    ("2", "#CCCCCC"),
    ("3", "#CCCCCC"),
    ("-", "#4267B2"),
    ("0", "#CCCCCC"),
    ("00", "#CCCCCC"),
    (".", "#CCCCCC"),
    ("+", "#4267B2"),
    ("=", "#168ACB")
]

row = 0
column = 0

for button in buttons:
    text = button[0]
    bg_color = button[1]
    btn = Button(button_frame, text=text, font="Roboto 20 bold", padx=20, pady=10, bd=0, bg=bg_color, fg="#ffffff")
    btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)
    column += 1
    if column > 3:
        column = 0
        row += 1

button_frame.pack(pady=10)

root.mainloop()
