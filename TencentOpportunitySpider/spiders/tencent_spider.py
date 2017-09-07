# -*- coding: utf-8 -*-
import urllib

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from TencentOpportunitySpider.items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0']

    rules = (
        Rule(LinkExtractor(allow='start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        nodes = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for node in nodes:
            item = TencentItem()
            item["name"] = node.xpath('./td[1]/a/text()').extract()[0]
            item["href"] = node.xpath('./td[1]/a/@href').extract()[0]
            item["href"] = urllib.parse.urljoin('http://hr.tencent.com/position.php?', item["href"])
            type_list = node.xpath('./td[2]/text()').extract()
            if len(type_list) == 0:
                item["type"] = ""
            else:
                item["type"] = type_list[0]
            item["hire_count"] = node.xpath('./td[3]/text()').extract()[0]
            item["local"] = node.xpath('./td[4]/text()').extract()[0]
            item["pub_time"] = node.xpath('./td[5]/text()').extract()[0]
            item["responsibilities"] = ""
            item["requirements"] = ""
            # yield item
            yield scrapy.Request(item["href"], meta={"item": item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta["item"]
        contents = response.xpath('//*[@id="position_detail"]/div/table/tr[3]/td/ul/li/text()').extract()
        for i, content in enumerate(contents, start=1):
            item["responsibilities"] += "{index}. {content}\n".format(index=i, content=content)

        contents = response.xpath('//*[@id="position_detail"]/div/table/tr[4]/td/ul/li/text()').extract()

        for i, content in enumerate(contents, start=1):
            item["requirements"] += "{index}. {content}\n".format(index=i, content=content)

        yield item


