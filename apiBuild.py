import os
import threading

reports = ['JO_member', 'JO_order', 'JO_product', 'JO_stock']
filepath = 'C:\develop\workspace_vscode\\'


def run_bat(i):  # 定义运行python文件函数

    cmd1 = 'cd ' + filepath + i
    cmd2 = '.\gradlew build'
    cmd = cmd1 + ' && ' + cmd2
    os.system(cmd)


if __name__ == '__main__':  # 多线程运行python文件
    for i in reports:
        task = threading.Thread(target=run_bat, args=(i, ))
        task.start()

