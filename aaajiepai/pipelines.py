# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class AaajiepaiPipeline(object):
    def process_item(self, item, spider):
        with open("image/"+item['image_name'],'wb') as f:
            f.write(item['image'])
            f.close()
        raise DropItem