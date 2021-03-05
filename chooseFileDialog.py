import ctypes
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

# 调用api设置成由应用程序缩放
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 调用api获得当前的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 设置缩放因子
root.tk.call('tk', 'scaling', ScaleFactor/75)

root.withdraw()

file_path = filedialog.askopenfilename()
# print(file_path)

print("输入sheet名:")
sheetName = input()
print(sheetName)

if file_path != "":

    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as fp:
        contents = fp.readlines()
    # print(contents)

    with open(r"abstestbak.py", 'w', encoding='utf-8') as fp2:
        fp2.write("".join(contents))
else:
    print("选择一个文件")
