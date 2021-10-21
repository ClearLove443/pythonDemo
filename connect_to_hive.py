from pyhive import hive

conn = hive.Connection(
    host='110.40.137.191',
    port=10000,
    username='hive',
    # password='hive',
    database='testdb',
    auth='NONE')
cursor = conn.cursor()
cursor.execute('select * from employee')
for result in cursor.fetchall():
    print(result)
