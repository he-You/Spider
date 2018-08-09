#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 上午10:35
# @Author  : Ju1is|落叶挽歌
# @Site    : https://github.com/vompom
# @File    : yunji.py
# @Email   : 617669559@qq.com
# @Software: PyCharm
# @Description: 太懒了还没有来得及写备注

import scrapy
import json
from yunji.items import YunjiItem


class Yunji(scrapy.Spider):
    name = 'yunji'
    allowed_domains = ['m.yunjiweidian.com']
    start_urls = ['https://www.baidu.com']
    # 测试数据
    cookie = {'acw_tc': 'AQAAANaf5BmyqAAAiBq/PD71bidj43Wr', 'u_asec': '099%23KAFEGYEKEmEEhYTLEEEEEpEQz0yFD6DHDrsMQ6DTDXnIW6tcSryID60FDEFETcZdt9TXE7EFbOR5D3QTEEx6zIywjYFETrZtt3illuYTEHITmobEjUYOI8KNZIYvzaD4kLjBaaLN6wEW6oSq33Nny8gN1EGGP8TC01Tqiwhv0JmSoVbIXXg4kLNowDN7VNGrykxyZBut3aIQqFCccyEaRJfrsEFEpcZdt3illuZdsyaDMlllszJP%2F3mrlllr%2BuZdtkslluWRsyaDy%2FllsUPoE7EIsyaD4hAw3Q9rE7EhssaZtfiMAYFEPOKXD67ScblcL4wsDRMBFEt6iRnpbOiRwEz6uz8nPvS7wSZuDahWFEPc929ibwUq%2BvD3Uoxkq7d71Sss4LpA97A6CsJKHai3woDWuVuCcYUqaMh%2BCapCL7FsLOaicpiRE9suQ6Yyh3Qs1bW4VsonaGhucsnKbOMFCGFuVfpMvw%2F6wEZtC21AaGA3wpw0zwIT%2FLbqzloVb4dq1QlzZjcSL4MR%2BO%2FkPOK6CGhudz2SrMe6iGr8sapX', 'pgv_si': 's61286400', 'pgv_pvi': '1071216640', 'aliyungf_tc': 'AQAAAOlGWTqRmAAAiBq/PGH9PUOiL1M7', 'LATELY_SHOPID': '1148601'}

    def parse(self, response):
        yunji_product_json_url = "https://m.yunjiweidian.com/yunjibuyer/listItemByCategoryLevel.json?pageSize=15&categoryLevelId1=27&categoryLevelId2=0&pageIndex="
        for i in range(0, 46):
            print("======第", i, "页======")
            request_url = yunji_product_json_url + str(i)
            print(request_url)
            yield scrapy.Request(request_url, callback=self.get_content, dont_filter=True)

    def get_content(self, response):
        data_json = json.loads(str(response.body_as_unicode())).get("itemList")
        yunji = YunjiItem()
        for product in data_json:
            yunji['name'] = product.get('itemName')
            yunji['price'] = product.get('itemPrice')
            yunji['sell_type'] = product.get('sellType')
            yunji['discount_price'] = product.get('itemVipPrice')
            yunji['brand'] = product.get('itemBrandName')
            # print(yunji)
            yield yunji





