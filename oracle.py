import cx_Oracle

con = cx_Oracle.connect("system/oracle@192.168.2.174/xe")
print(con.version)
cur = con.cursor()
cur.execute("SELECT table_name FROM dba_tables")
rows = cur.fetchall()
print(type(rows))
print(rows)
con.close()
