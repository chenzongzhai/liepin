# -*- coding: utf-8 -*-

import config
from scrapy import log


class cursor_warpper:
    '''对数据库资源的with封装'''
    def __init__(self, dbpool):
        self._conn = dbpool.connection()
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self._cursor, self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print exc_type, exc_val, exc_tb
        if self._cursor is not None:
            self._cursor.close()
        if self._conn is not None:
            self._conn.close()


# 将数据写入数据库中，如果md5已经存在更新发布时间
def insert(cup, url):
    with cursor_warpper(config.pool) as (cursor, conn):
        sql = 'INSERT INTO liepin(url, code_md5, name, company_name, \
        publish_time, requires, pay, company_size, company_address, company_type) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE \
        publish_time = %s;'
        log.msg('do insert: %s, url is: %s.' % (cup, url), level=log.INFO)
        cursor.execute(sql, cup)
        conn.commit()
