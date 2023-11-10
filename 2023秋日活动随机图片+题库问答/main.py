# 一些可以调的全局设置
fontsize = 48 # 字体大小

# 预处理
questions = []
with open('题库.txt', 'r', encoding='utf-8') as f:
    tmp = ""
    lines = f.readlines()
    for line in lines:
        if line[0] == '\n':
            continue
        if line[0] == 'Q':
            questions.append(tmp[:-1])
            tmp = ""
        tmp = tmp + line
    questions.append(tmp[:-1])
questions.pop(0)

features = []
with open('特征.txt', 'r', encoding='utf-8') as f:
    features = f.readlines()

import os
images = []
dirs = os.listdir('src')
for i in dirs:
    images.append('.\\src\\' + i)

from tkinter import *
from ttkthemes import *
from tkinter.ttk import *
from ttkbootstrap import Style
import random
from PIL import Image, ImageTk

# 答题（一道文字题）
# 根据特征说角色（一个词）
# 看图猜番名（一张图）


def answer_question():
    global label
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    exit_button.pack_forget()
    label = Label(window, text=random.choice(questions))
    label.pack(ipady=20, expand=True)
    return_button.pack(ipady = 30, expand=True)

def find_character():
    global label
    global label
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    exit_button.pack_forget()
    label = Label(window, text=random.choice(features))
    label.pack(ipady=100, expand=True)
    return_button.pack(ipady = 30, expand=True)

photo_image = 0
def get_img():
    global photo_image
    img_path = random.choice(images)
    img = Image.open(img_path)
    img_w, img_h = img.size
    print(img.size)
    r = min(win_w / img_w, win_h / img_h) * 0.8
    img_w = int(img_w * r)
    img_h = int(img_h * r)
    img = img.resize((img_w, img_h))# , Image.LANCZOS)
    print(img_path)
    photo_image = ImageTk.PhotoImage(img)

def guess_anime():
    global label
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    exit_button.pack_forget()
    # img_path = random.choice(images)
    # img = Image.open(img_path)
    # img_w, img_h = img.size
    # print(img.size)
    # r = min(win_w / img_w, win_h / img_h)
    # img_w = int(img_w * r)
    # img_h = int(img_h * r)
    # img = img.resize((img_w, img_h))# , Image.LANCZOS)
    # print(img_path)
    # photo_image = ImageTk.PhotoImage(img)
    # photo_image.show()
    label = Label(window)
    get_img()
    label.configure(image=photo_image)
    label.pack(ipady=10, expand=True)
    return_button.pack(ipady = 30, expand=True)

def menu():
    global window
    label.pack_forget()
    return_button.pack_forget()
    button1.pack(ipady = 30, pady=30, expand=True)
    button2.pack(ipady = 30, pady=10, expand=True)
    button3.pack(ipady = 30, pady=30, expand=True)
    exit_button.pack(ipady = 30, pady=30, expand=True)
    pass

def withdraw():
    window.destroy()

# window = Tk()
s = Style(theme='darkly')
s.configure('.', font=('SimHei', fontsize))
window = s.master

# root.title('猜影子')
window.attributes('-fullscreen', True)
window.update()
win_w = window.winfo_width()
win_h = window.winfo_height()


text = StringVar()
text.set(random.choice(questions))
button1 = Button(window, text='看图猜番名', command=guess_anime, width=20)
button2 = Button(window, text='根据特征说角色', command=find_character, width=20)
button3 = Button(window, text='答题', command=answer_question, width=20)
return_button = Button(window, text='返回', command=menu)
exit_button = Button(window, text = '退出', width=10, command=withdraw)

def func_key(event):
    if event.keycode == 27:
        # ESc
        window.destroy()
exit_button.bind('<Key>', func_key)

button1.pack(ipady = 30, pady=30, expand=True)
button2.pack(ipady = 30, pady=10, expand=True)
button3.pack(ipady = 30, pady=30, expand=True)
exit_button.pack(ipady = 30, pady=30, expand=True)


# button.focus_set()

window.mainloop()