import os
import threading

reports = ['jo_member', 'jo_order', 'jo_product', 'jo_stock']
filepath = 'C:\develop\workspace_vscode\\'

# filepath = '.\\'


def run_bat(i):  # 定义运行python文件函数
    os.system(filepath + i + '.bat')


if __name__ == '__main__':  # 多线程运行python文件
    for i in reports:
        task = threading.Thread(target=run_bat, args=(i, ))
        task.start()
