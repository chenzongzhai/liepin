# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import datetime
import hashlib
import traceback
from spiders import db_update
from scrapy import log


# 每一个招聘信息都会计算出一个md5，作为mysql数据库的UNIQUE KEY，避免重复写入数据
def md5str(strr):
    m = hashlib.md5(strr)
    md5 = m.hexdigest().lower()
    return md5


# 发布日期转换，统一转换成datatime格式
def get_publish(pub):
    today = datetime.date.today()
    if pub.find("小时") != -1 or pub.find("分钟") != -1:
        publish_time = today
    elif pub.find("昨天") != -1:
        publish_time = today - datetime.timedelta(days=1)
    else:
        result = re.search('\d+-\d+-\d+', pub)
        if result:
            publish_time = datetime.datetime.strptime(result.group(), "%Y-%m-%d").date()
        else:
            publish_time = None
    return publish_time


# 将职位需求拼接到一起，方便写入数据库
def get_require(requires):
    require = ''
    for r in requires:
        require += r + ' '
    return require.strip().encode('utf-8')


class LiepinPipeline(object):

    def get_cup(self, item):
        url = item['url']
        name = item['name'][0].strip().encode('utf-8')
        company_name = item['company_name'][0].strip().encode('utf-8')
        if item['company_size']:
            company_size = item['company_size'][4].strip().encode('utf-8')
            company_address = item['company_address'][-1].strip().encode('utf-8')
            company_type = item['company_type'][-3].strip().encode('utf-8')
        else:
            company_size = None
            company_address = None
            company_type = None
        pay = item['pay'][0].strip().encode('utf-8')
        publish_time = get_publish(item['publish_time'][-1].encode('utf-8'))
        require = get_require(item['requires'])
        code_md5 = md5str(url + name + company_name + require)
        return (url, code_md5, name, company_name, publish_time, require, pay,
                company_size, company_address, company_type, publish_time)

    # 捕捉错误信息写入log
    def process_item(self, item, spider):
        try:
            cup = self.get_cup(item)
            db_update.insert(cup, item['url'])
        except Exception, e:
            log.msg('url is: %s, error is: %s.' % (item['url'], traceback.format_exc()),
                    level=log.ERROR)
            print e
            traceback.print_exc()
        # return item
