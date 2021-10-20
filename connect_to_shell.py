import paramiko
from scp import SCPClient


# 执行多条命令
def exec_command():
    # ip、用户名、密码
    # ip = "127.0.0.1"
    # port = 1112
    # user = "ubuntu"
    # password = "password"

    ip = "110.40.137.191"
    port = 22
    user = "ubuntu"
    key_filename = 'id_rsa'
    # pkey = paramiko.RSAKey.from_private_key_file('id_rsa')

    # 创建SSHClient 实例对象
    ssh = paramiko.SSHClient()
    # 调用方法，表示没有存储远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    # 连接远程机器，地址，端口，用户名密码
    # ssh.connect(ip, port, user, password, timeout=10)
    ssh.connect(ip, port, user, key_filename=key_filename, timeout=10)

    # 输入linux命令
    command = "cd ~ ; pwd ; ls"
    stdin, stdout, stderr = ssh.exec_command(command)
    # 输出命令执行结果
    result = stdout.read()
    # bytes 转 str
    result = str(result)

    result = result.split('\\n')
    for i in result:
        print(i)


# 上传下载文件、文件夹 SCP
def upload_download_SCP():
    ip = "110.40.137.191"
    port = 22
    user = "ubuntu"
    key_filename = 'id_rsa'
    # pkey = paramiko.RSAKey.from_private_key_file('id_rsa')

    # 创建SSHClient 实例对象
    ssh = paramiko.SSHClient()
    # 调用方法，表示没有存储远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    # 连接远程机器，地址，端口，用户名密码
    # ssh.connect(ip, port, user, password, timeout=10)
    ssh.connect(ip, port, user, key_filename=key_filename, timeout=10)
    scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
    # 设置上传的本地/远程文件路径
    # localpath = "test.txt"
    # remotepath = "/home/ubuntu/test2/test.txt"
    # # 执行上传单个文件
    # scpclient.put(localpath, remotepath)

    # localpath = "test"
    # remotepath = "/home/ubuntu/test2/"
    # # 执行上传文件夹
    # scpclient.put(localpath, remotepath, recursive=True)

    # # 设置下载的本地/远程文件路径
    # localpath2 = "test2.txt"
    # remotepath2 = "/home/ubuntu/test.txt"
    # # 执行下载动作
    # scpclient.get(remotepath2, localpath2)

    # 设置下载的本地/远程文件夹路径
    localpath2 = ""
    remotepath2 = "/home/ubuntu/test2/"
    # 执行下载动作
    scpclient.get(remotepath2, localpath2, recursive=True)


# 上传下载文件 SFTP
def upload_download_File_SFTP():
    ip = "110.40.137.191"
    port = 22
    user = "ubuntu"
    pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
    # 获取Transport实例
    tran = paramiko.Transport((ip, port))
    # 连接SSH服务端，使用password
    tran.connect(username=user, pkey=pkey)
    # 获取SFTP实例
    sftp = paramiko.SFTPClient.from_transport(tran)

    # # 设置上传的本地/远程文件路径
    # localpath = "test.txt"
    # remotepath = "/home/ubuntu/test.txt"
    # # 执行上传动作
    # sftp.put(localpath, remotepath)

    # 设置下载的本地/远程文件路径
    localpath2 = "test2.txt"
    remotepath2 = "/home/ubuntu/test.txt"
    # 执行下载动作
    sftp.get(remotepath2, localpath2)

    # 关闭连接
    tran.close()


# exec_command()
upload_download_SCP()
# upload_download_File_SFTP()
