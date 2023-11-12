from pyhive import hive, sqlalchemy_hive

con = hive.connect(
    host="110.42.214.104", port=10000, auth="KERBEROS", kerberos_service_name="hive"
)  # host为hiveserver2所在节点，port默认10000，为hs2的端口
cursor = con.cursor()
cursor.execute("select * from customers")  # 不能有分号！
# cursor.execute('desc dl_nccp.account') #不能有分号！
datas = cursor.fetchall()
print(datas)
cursor.close()
con.close()
