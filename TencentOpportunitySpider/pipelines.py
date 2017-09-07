# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from datetime import date


class TencentopportunityspiderPipeline(object):
    def __init__(self):
        self.file_obj = open("tencent{date}.csv".format(date=date.today()), "w", encoding='utf_8_sig', newline="")
        self._fields = ["name", "type", "hire_count", "local", "pub_time", "href", "responsibilities", "requirements"]
        self._dictwriter = csv.DictWriter(self.file_obj, fieldnames=self._fields)
        self._dictwriter.writerow({"name": "职位名称", "type": "职位类别", "hire_count": "招聘人数", "local": "工作地点",
                                   "pub_time": "发布时间", "href": "详细链接", "responsibilities": "工作职责",
                                   "requirements": "工作要求"})

    def process_item(self, item, spider):
        self._dictwriter.writerow(item._values)
        return item

    def close_spider(self, spider):
        self.file_obj.close()
