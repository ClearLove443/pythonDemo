import os
import re
import sys

port = input('please input port:')
with os.popen('netstat -ano|findstr ' + port) as pipe:
    result = pipe.read()
if result == '':
    sys.exit()

pattern = re.compile(r'0.0.0.0:0\ +LISTENING\ +\d{4,5}')
str = pattern.search(result)[0]

pattern2 = re.compile(r'\d{4,5}')
pid = pattern2.search(str)[0]
with os.popen('taskkill /pid ' + pid + ' /f') as pipe:
    result = pipe.read()

pattern3 = re.compile(r'成功')
if pattern3.search(result)[0] != '':
    input('kill successful')
else:
    input('kill failed')
