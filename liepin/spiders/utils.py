# -*- coding:utf-8 -*-
'''
    可以写一些公共方法
'''

import re


# 正则匹配链接规则，符合规则的返回True
def is_match(url, rule):
    obj = re.compile(rule).match(url)
    if obj is None:
        return False
    else:
        return True
