import os

import requests


def save_image(url, root):
    """
    传入图片的资源地址，和图片要待的文件夹路径，保存单张图片
    """
    image_name = url.split('/')[-1]  # 获取图片名称：xxx.xxx

    try:
        # 如果文件夹不存在，就创建该文件夹
        if not os.path.exists(root):
            os.makedirs(root)
        else:
            pass

        image_path = root + r'\{0}'.format(image_name)  # 注意：反斜杠是怎么处理的

        # 如果图片不存在，就写入图片
        if not os.path.exists(image_path):
            r = requests.get(url)

            with open(image_path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")

    except:
        print('执行出错')


root = r'C:\PersonalFile'  # 图片要待的文件夹 注意：文件路径是反斜杠组织的 由于反斜杠有转义的作用，所以要在前面加r，禁用转义，当作原生字符串看待
for i in range(300):

    url = 'https://jp-d-private-static-contents-s3-001.s3-ap-northeast-1.amazonaws.com/work/static-contents/tkfront/cms/ECST0001/include/gazou/gazou3000' + \
        str(i) + '.jpg'

    save_image(url, root)
