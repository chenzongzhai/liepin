# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from liepin.items import LiepinItem
from urlparse import urljoin
from utils import is_match
from config import CONFIG


class LiepinSpider(Spider):
    name = "liepin"
    allowed_domains = CONFIG['allowed_domains']
    start_urls = CONFIG['start_urls']

    def parse(self, response):
        sel = Selector(response)
        current_url = response.url

        # 详情页分析
        for detail_link in CONFIG['detail_link_rule']:
            if is_match(current_url, detail_link):
                item = LiepinItem()
                # items接收list，防止出现index out of range
                item['url'] = current_url
                item['name'] = sel.xpath('//div[@class="title-info "]/h1/text()').extract()  # [0]
                item['company_name'] = sel.xpath('//div[@class="title-info "]/h3/a/text()').extract()  # [0]
                item['company_size'] = sel.xpath('//div[@class="right-post-top"]/div/text()').extract()  # [4]
                item['company_address'] = sel.xpath('//div[@class="right-post-top"]/div/text()').extract()  # [-1]
                item['company_type'] = sel.xpath('//div[@class="right-post-top"]/div/text()').extract()  # [-3]
                item['pay'] = sel.xpath('//p[@class="job-main-title"]/text()').extract()  # [0]
                item['publish_time'] = sel.xpath('//p[@class="basic-infor"]/span[2]/text()').extract()  # [-1]
                item['requires'] = sel.xpath('//div[@class="resume clearfix"]/span/text()').extract()
                yield item

        # 过滤出所有的列表页和详情页进行回调。
        for url in sel.xpath('//a/@href').extract():
            url = urljoin(current_url, url)

            for list_link in CONFIG['list_link_rule']:
                if is_match(url, list_link):
                    # log.msg('list_url: %s' % url, level=log.INFO)
                    yield Request(url, callback=self.parse)

            for detail_link in CONFIG['detail_link_rule']:
                if is_match(url, detail_link):
                    # log.msg('detail_url: %s' % url, level=log.INFO)
                    yield Request(url, callback=self.parse)
