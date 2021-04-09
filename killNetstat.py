import os
import re

# result = os.system('getmac')
port = input('input killed port ')
result = os.system('netstat -ano|findstr ' + port)
# print(str(result))
killPidRe = re.compile(r"[0-9]{4,7}")
# killPid = killPidRe.findall(str(result))
killPid = re.findall(r"[0-9]{4,7}", str(result))
print(killPid)


def get_mac_and_ip():

    with os.popen('ipconfig -all') as pipe:
        str_config = pipe.read()
        # print("完整配置信息：", str_config)
        # 利用正则表达式和re模块检索结果
        mac_re_compile = re.compile(r"物理アドレス[\. ]+: ([\w-]+)")
        ip_re_compile = re.compile(r"IPv4 アドレス[\. ]+: ([\.\d]+)")

        mac = mac_re_compile.findall(str_config)[0]  # 找到MAC
        ip = ip_re_compile.findall(str_config)[0]  # 找到IP

        print("MAC=%s, IP=%s" % (mac, ip))

    return mac, ip


# result = get_mac_and_ip()
