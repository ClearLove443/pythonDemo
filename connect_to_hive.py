from impala.dbapi import connect
from krbcontext import krbcontext
from pyhive import hive


def pyhive():
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


def impala():
    conn = connect(
        host='110.40.137.191',
        port=10000,
        database='testdb',
        auth_mechanism='PLAIN')
    cur = conn.cursor()
    cur.execute('select * from employee')
    for result in cur.fetchall():
        print(result)


def impala_kerberos():
    with krbcontext(using_keytab=True,
                    principal='cloudera-scm/admin@CLOUDERA',
                    keytab_file='admin.keytab'):
        conn = connect(host='110.42.214.104',
                            port=10000,
                            database='testdb',
                            auth_mechanism='GSSAPI',
                            kerberos_service_name='hive',
                            use_kerberos=True,
                            krb_host='quickstart.cloudera')

        cur = conn.cursor()
        cur.execute('select * from employee')
        for result in cur.fetchall():
            print(result)


# pyhive()
# impala()
impala_kerberos()
