from impala.dbapi import connect

# from krbcontext import krbcontext

# from pyhive import hive


# def pyhive():
#     conn = hive.Connection(
#         host="110.40.137.191",
#         port=10000,
#         username="hive",
#         # password='hive',
#         database="testdb",
#         auth="NONE",
#     )
#     cursor = conn.cursor()
#     cursor.execute("select * from employee")
#     for result in cursor.fetchall():
#         print(result)


# def impala():
#     conn = connect(
#         host="110.40.137.191", port=10000, database="testdb", auth_mechanism="PLAIN"
#     )
#     cur = conn.cursor()
#     cur.execute("select * from employee")
#     for result in cur.fetchall():
#         print(result)


def impala_kerberos():
    with krbcontext(
        using_keytab=True,
        principal="hive.quickstart.cloudera",
        keytab_file="hive.quickstart.cloudera@CLOUDERA.keytab",
    ):
        conn = connect(
            host="110.42.214.104",
            port=10000,
            database="testdb",
            auth_mechanism="GSSAPI",
            kerberos_service_name="hive",
            use_kerberos=True,
            krb_host="quickstart.cloudera",
        )

        cur = conn.cursor()
        cur.execute("select * from customers")
        for result in cur.fetchall():
            print(result)


# pyhive()
# impala()
# impala_kerberos()


import datetime as dt
import os
import random
from datetime import datetime

import numpy as np
# import findspark as fs
# fs.init()
import pandas as pd
import pyspark.sql.functions as F
# from log3 import log, log_to_file
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, SparkSession, SQLContext
from pyspark.sql.types import *

# from krbcontext import krbcontext


active_str = "kinit -kt hive.quickstart.cloudera@CLOUDERA.keytab hive/quickstart.cloudera@CLOUDERA"
os.system(active_str)
# config = {
#     "kerberos_principal": "hive.quickstart.cloudera@CLOUDERA",
#     "keytab_file": "hive.quickstart.cloudera@CLOUDERA.keytab",
#     "kerberos_ccache_file": "/home/tools/wyk/keytab/hive_ccache_uid",
#     "AUTH_MECHANISM": "GSSAPI",
# }
# with krbcontext(
#     using_keytab=True,
#     principal=config["kerberos_principal"],
#     keytab_file=config["keytab_file"],
#     ccache_file=config["kerberos_ccache_file"],
# ):

conf = SparkConf().setMaster("yarn").setAppName("MF_return_calc")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
hiveCtx = HiveContext(sc)
spark = (
    SparkSession.builder.master("yarn")
    .appName("MF_return_calc")
    .config("spark.debug.maxToStringFields", "100")
    .getOrCreate()
)

# Execute SQL
test_sql = """select * from customers"""
res = hiveCtx.sql(test_sql)
type(res)  # Return spark dataframe
res.head(3)
res_pd = res.toPandas()  # Convert spark dataframe to Panda dataframe
res_pd
