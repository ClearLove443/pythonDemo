import asyncio
import os
from os import close

import asyncpg

from common import timer

sql = '''
        SELECT
            CHANNEL_CODE
            , MODULE_ID
            , MODULE_VERSION_ID
            , HTML_CONTENT 
        FROM
            EC.T_MODULE_VERSION 
        WHERE
            1 = 1 
            AND MODULE_VERSION_ID IS NOT NULL 
        ORDER BY
            1
    '''


def asyncpgConnect(sql):  # asyncpg连接postgresql
    async def run():
        conn = await asyncpg.connect(user='postgres', password='postgres',
                                     database='ec_mcp_db', host='127.0.0.1', port='5432')
        # row2 = await conn.fetchrow(sql)
        # print(row2)
        row1 = await conn.fetch(sql)
        for i in row1:
            creatHtml(i["channel_code"], i["module_id"],
                      i["module_version_id"], i["html_content"])

        await conn.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()


def creatHtml(channelCode, moduleId, moduleVersionId, htmlContent):

    filePath = os.getcwd()
    htmlPath = filePath + "\\" + channelCode + "\\" + moduleId + "\\"
    htmlFileName = "dm_index_" + str(moduleVersionId) + ".html"
    if not (os.path.exists(htmlPath)):
        os.makedirs(htmlPath)

    htmlFullName = htmlPath + htmlFileName
    with open(r"" + htmlFullName, "w", encoding='utf-8') as fp2:
        fp2.write(htmlContent if htmlContent != None else "")
        fp2.close


@timer
def run():
    asyncpgConnect(sql)


if __name__ == '__main__':
    run()
# creatHtml("ECST0001", "DM000005", "1", '''333''')
