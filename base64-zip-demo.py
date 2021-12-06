import base64
import ctypes
from tkinter import Button, Tk, filedialog
from tkinter.font import BOLD


class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("zip file tool ")  # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry("1068x681+10+10")
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        # 标签
        # self.init_data_label = Label(self.init_window_name, text="待处理数据")
        # self.init_data_label.grid(row=0, column=0)
        # self.result_data_label = Label(self.init_window_name, text="输出结果")
        # self.result_data_label.grid(row=0, column=12)
        # self.log_label = Label(self.init_window_name, text="日志")
        # self.log_label.grid(row=12, column=0)
        # 文本框
        # self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        # self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        # self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        # self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        # self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        # self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        self.str_trans_to_md5_button = Button(
            self.init_window_name,
            text="zip file to base 64",
            bg="lightblue",
            font=("Helvetica", 15, BOLD),
            command=self.encodeZip,
        )  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=0, column=0, padx=200, pady=100)
        self.str_trans_to_md5_button = Button(
            self.init_window_name,
            text="base 64 to zip file",
            bg="lightblue",
            font=("Helvetica", 15, BOLD),
            command=self.decodeBase64Str,
        )  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=0, padx=200, pady=100)

    def openDialog(self):

        file_path = filedialog.askopenfilename()
        return file_path

    def gui_start():
        init_window = Tk()  # 实例化出一个父窗口

        ZMJ_PORTAL = MY_GUI(init_window)
        # 设置根窗口默认属性
        ZMJ_PORTAL.set_init_window()

        # 调用api设置成由应用程序缩放
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        init_window.mainloop()

    def encodeZip(self):
        file_path = self.openDialog()
        print(file_path)
        # encode zip file to base64
        with open(file_path, "rb") as file_input, open(
            "file_output.zip.b64", "wb+"
        ) as file_output:
            base64.encode(file_input, file_output)

    def decodeBase64Str(self):
        # decode base64 to zip file
        file_path = self.openDialog()
        print(file_path)
        with open(file_path, "rb") as file_input, open(
            "file_output.zip", "wb"
        ) as file_output:
            base64.decode(file_input, file_output)


MY_GUI.gui_start()
