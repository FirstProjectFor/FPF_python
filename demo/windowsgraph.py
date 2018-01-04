from tkinter import *

import win32com.client as win


def read():
    text = e.get()
    # 调用语音控件
    speak = win.Dispatch("SAPI.SpVoice")
    speak.Speak(text)


# 窗口配置 标题，大小，背景色
tts = Tk()
tts.wm_title("Text to Speech")
tts.geometry("225x105")
tts.config(background="#39f")

# 定义窗口，以及位置
f = Frame(tts, height=280, width=500, bg="#bebebe")
f.grid(row=0, column=0, padx=10, pady=5)

# 定义 Label
lbl = Label(f, text="Enter your Text here : ")
lbl.grid(row=1, column=0, padx=10, pady=2)

# 定义输入框
e = Entry(f, width=30)
e.grid(row=2, column=0, padx=10, pady=2)

# 定义按钮
btn = Button(f, text="Speak", command=read)
btn.grid(row=3, column=0, padx=20, pady=10)

# 初始化窗口
tts.mainloop()
