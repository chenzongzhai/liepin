# -*- coding:utf-8 -*-

import MySQLdb
from DBUtils.PooledDB import PooledDB

CONFIG = {
    'allowed_domains': ['www.liepin.com', 'job.liepin.com'],
    'start_urls': ['https://www.liepin.com/zhaopin/'],
    'detail_link_rule': ['https://job.liepin.com/\d+_\d+/\?imscid=\w+'],
    'list_link_rule': ['https://www.liepin.com/zhaopin/\?curPage=\d+']
}

pool = PooledDB(MySQLdb, mincached=1, maxcached=62, host='xxx.xxx.xxx.xxx',
                port=xxxx, user='xxxx', passwd='xxxxxx',
                db='test', use_unicode=False, charset='utf8'
                )
