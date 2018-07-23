# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http import Request
from aaajiepai.items import AaajiepaiItem
import requests
class AaajiepaiImgSpider(scrapy.Spider):
    name = 'aaajiepai_img'
    allowed_domains = ['3ajiepai.com']
    start_urls = ['http://www.3ajiepai.com/portal.php']

    def parse(self, response):
        a_tag = Selector(response=response).xpath('//ul[@id="mn_N3552_menu"]/li/a/@href').extract()
        for url in a_tag:
            yield Request(
                url=url,
                callback=self.classification
            )
    def classification(self,response):
        page_tag = Selector(response=response).xpath('//div[@class="pg"]/a/@href').extract()
        for page in page_tag:
            yield Request(url=page,callback=self.page)
    def page(self,response):
        image_tag = Selector(response=response).xpath('//a[@class="z"]/@href').extract()
        for img in image_tag:
            yield Request(url=img, callback=self.image)
    def image(self,response):
        src_tag = Selector(response=response).xpath('//img[@class="zoom"]')
        for src in src_tag:
            image_src = src.xpath('./@zoomfile').extract_first()
            image_title = src.xpath('./@title').extract_first()
            image_name = image_src.split('/')[-1]
            req = requests.get(image_src)
            item_obj = AaajiepaiItem(image=req.content, image_src=image_src,image_title=image_title,image_name=image_name)
            yield item_obj
