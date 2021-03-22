import os

import psycopg2
from pykeyboard import PyKeyboard

password = input('请输入数据密码:')
try:
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password=password, host='localhost', port='5432')
    conn.autocommit = True

    cur = conn.cursor()
except:
    input('密码输入错误，请重新执行。按回车键退出')
    exit()
else:
    print('数据库连接成功')
# try:
#     cur.execute('drop role "ec_mcp_admin"')
# except:
#     print('用户删除失败')
# else:
#     print('用户删除成功')

# try:
#     cur.execute('create role test superuser login')
#     cur.execute('ALTER USER test PASSWORD "test"')
# except:
#     print('用户创建失败')
# else:
#     print('用户创建成功')postgres
db_name = "ec_mcp_db"
# db_name = input()

try:
    sql = "SELECT PG_TERMINATE_BACKEND(PG_STAT_ACTIVITY.PID) FROM PG_STAT_ACTIVITY WHERE DATNAME = '" + \
        db_name + "' AND PID <> PG_BACKEND_PID()"
    cur.execute(sql)
except:
    input('连接断开失败')
else:
    print('连接断开成功')

try:
    cur.execute('drop database {};'.format(db_name))
except:
    input('数据库删除失败')
else:
    print('数据库删除成功')

try:
    cur.execute('create database {};'.format(db_name))
except:
    input('数据库创建失败')
else:
    print('数据库创建成功')

cur.close()
conn.close()

# os.system('getMac')
os.system('pg_restore -U postgres -d ' + db_name + ' dataBack.dmp')
input('按回车键退出')
# k = PyKeyboard()
# k.type_string('pg_restore -U postgres -d ')
# k.type_string(db_name)
# k.type_string(' dataBack.dmp')
# k.tap_key(k.enter_key)
