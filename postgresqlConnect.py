import asyncio
from os import close

import asyncpg
import psycopg2

from common import timer

sql = 'select 2'


@timer
def asyncpgConnect(sql):  # asyncpg连接postgresql
    async def run():
        conn = await asyncpg.connect(user='postgres', password='postgres',
                                     database='ec_mcp_db', host='127.0.0.1', port='5432')
        hasChannel = []
        noChannel = []
        # for i in sql:  有 bug list多个值相同的时候，取的下标不正确
        #     try:
        #         await conn.fetch(i)
        #         hasChannel.append(sql.index(i) + 1)
        #     except Exception:
        #         noChannel.append(sql.index(i) + 1)

        # for i in range(len(sql)):
        #     try:
        #         await conn.fetch(sql[i])
        #         hasChannel.append(i + 1)
        #     except Exception:
        #         noChannel.append(i + 1)
        for key in sql:
            try:
                await conn.fetch(sql[key])
                hasChannel.append(key)
            except Exception:
                noChannel.append(key)
        print('hasChannelCode', hasChannel)
        print('noChannelCode', noChannel)
        await conn.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()


@timer
def psycopg2connect(sql):  # psycopg2连接postgresql
    conn = psycopg2.connect(database='ec_mcp_db', user='postgres',
                            password='postgres', host='localhost', port='5432')
    conn.autocommit = True

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)
    cur.close()
    conn.close()


# asyncpgConnect(sql)
# psycopg2connect(sql)
sqlMap = {}
with open(r"sql.txt", 'r', encoding='utf-8') as fp:
    contents = fp.readlines()  # 读取的就是list

for i in contents:
    key = i.split('\t')[0]
    value = i.split('\t')[1]
    sqlMap[key] = value[0: -2]
asyncpgConnect(sqlMap)
