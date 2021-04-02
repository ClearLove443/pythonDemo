import os
import shutil
import threading

reports = ['jo_member', 'jo_order', 'jo_product', 'jo_stock', 'jp_stub_server']
filepath = 'C:\develop\workspace_vscode\\'

# filepath = '.\\'


def run_bat(i):  # 定义运行python文件函数
    os.system(filepath + i + '.bat')


if __name__ == '__main__':  # 多线程运行python文件

    filePath = os.getcwd()
    logFilePath = filePath + "\logs"
    print(logFilePath)
    try:
        shutil.rmtree(logFilePath)  # 删除文件夹
    except:
        print('file not exists')

    for i in reports:
        task = threading.Thread(target=run_bat, args=(i, ))
        task.start()
