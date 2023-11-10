
'''初始化所有影子'''
import os
path = '.\\src\\'
ld = os.listdir(path)
# print(ld)

'''设置系统dpi缩放'''
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


import time
import random
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.title('猜影子')
root.attributes('-fullscreen', True)
root.update()
win_w = root.winfo_width()
win_h = root.winfo_height()
# print('window size:', win_w, win_h)

photo = 0
# cnt = 0

def get_pic():
    # global cnt
    # cnt = cnt + 1
    # print('cnt', cnt)

    '''获取影子并对其进行缩放适配窗口'''
    global photo
    imgPath = path + random.choice(ld)
    img = Image.open(imgPath)
    img_w, img_h = img.size
    r = min(win_w / img_w, win_h / img_h)
    img_w = int(img_w * r)
    img_h = int(img_h * r)
    img = img.resize((img_w, img_h)) # , Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
# get_pic()

def change_pic():
    get_pic()
    button.configure(image = photo)

button = ttk.Button(
    root,
    # image=photo,
    text='第一次点击此按钮运行\n之后点击图片或按任意切图\n按esc退出',
    command = change_pic,
    # anchor = 'center'
)
# button.focus_set()
button.pack()
def func_key(event):
    if event.keycode == 27:
        # ESc
        root.destroy()
button.bind('<Key>', func_key)

root.mainloop()