#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午3:10
# @Author  : Ju1is|落叶挽歌
# @Site    : https://github.com/vompom
# @Email   : 617669559@qq.com
# @File    : Vip.py
# @Software: PyCharm
# @Description: 爬取唯品会 美妆产品类 的数据

# -*- coding: utf-8 -*-

import scrapy
import json


from vip.items import VipItem

class Vip(scrapy.Spider):
    name = 'vip'
    allowed_domains = ['vip']
    # 全部数据
    # 获取到vip的美妆产品所有品牌的json数据：https://category.vip.com/ajax/getSlider.php?callback=getCategory2&type=21007&pageId=2&pageSize=200
    # start_urls = ['file:///Users/mac/Desktop/Python/vip/vip/spiders/vip.json']
    # 测试数据
    start_urls = ['file:///Users/mac/Desktop/Python/spider/vip/vip/spiders/test_vip_json.json']
    cookie = {'vip_address': '%257B%2522pid%2522%253A%2522103103%2522%252C%2522cid%2522%253A%2522103103101%2522%252C%2522pname%2522%253A%2522%255Cu6d59%255Cu6c5f%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu676d%255Cu5dde%255Cu5e02%2522%257D', 'cps': 'adp%3AC01V0000fksf6y76%3A%3Aokxptjjv%3AA100089449yisheng%3A94c0935c3e2f433b929f8f1ed55f0223',
              'vip_new_old_user': '1', 'oversea_jump': 'cn', 'cps_share': 'cps_share', 'm_vip_province': '103103', 'warehouse': 'VIP_SH', 'mars_sid': '0d127ba50a1cdf625057c64e17b44b2e', 'WAP[p_wh]': 'VIP_SH', '_smt_uid': '5b690645.363fbd2a', 'WAP[from]': '', 'visit_id': '4D1FA15F321A8E32A0D9240E88F544FF', 'PAPVisitorId': 'a511c18252e68a894e04d46c9d63cd11', 'vip_cps_cid': '1533609514682_ed91b5384fc9936512102aec7f8d8a39', 'vip_province_name': '%E6%B5%99%E6%B1%9F%E7%9C%81', 'fdc_area_id': '103103101',
              'vip_ipver': '31', 'wap_consumer': 'A1', 'WAP[p_area]': '%25E6%25B5%2599%25E6%25B1%259F', '_jzqco': '%7C%7C%7C%7C%7C1.1853164086.1533609541740.1533612111190.1533612129157.1533612111190.1533612129157.0.0.0.12.12', 'tmp_mars_cid': '1533609515267_9649c2343a41e3f7f4eb6ade663c3c40', 'vip_city_name': '%E6%9D%AD%E5%B7%9E%E5%B8%82', 'vip_first_visitor': '1', 'vip_province': '103103', 'mars_cid': '1533609515267_9649c2343a41e3f7f4eb6ade663c3c40', 'vip_wh': 'VIP_SH', 'vip_city_code': '103103101', 'user_class': 'a', 'VipUINFO': 'luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0',
              'mars_pid': '6', 'mst_csrf_key': '560bebd308bc97bb18d00f5e2bbd957b'}

    def parse(self, response):
        sites = json.loads(str(response.body_as_unicode()))
        for index,site in enumerate(sites):
            brand_url = site.get("url")
            if brand_url.find("http") == -1:  # 有的URL不以http开头，直接补全
                brand_url = "http:"+brand_url
            yield scrapy.Request(brand_url, callback=self.get_brand_id, dont_filter=True, cookies=self.cookie)

    """获取品牌ID"""
    def get_brand_id(self, response):
        brand = response.xpath('/html/head/title/text()').extract_first()
        print("====爬取[",brand,"]的商品=====")
        # 接下来很多请求需要用到 brand_id 和 wareshouse参数，获取方法有待优化
        brand_id = response.xpath('//script').re(r'brand_id":"(.{7})')
        warehouse = response.xpath('//script').re(r'warehouse":"(.{6})')

        # 并不能保证一定能获取到数据，所以进行了相关优化处理
        if len(brand_id) != 0:
            brand_id = brand_id[0]
        if len(warehouse) != 0:
            warehouse = warehouse[0]

        get_category_url = "https://mst.vip.com/Special/getCategory?&access_type=0&brand_id="+brand_id
        request = scrapy.Request(get_category_url, callback=self.get_brand_category, dont_filter=True)
        request.meta['brand_id'] = brand_id
        request.meta['warehouse'] = warehouse
        yield request

    """获取品牌分类目录"""
    def get_brand_category(self, response):
        brand_id = response.meta['brand_id']
        warehouse = response.meta['warehouse']
        category_json = json.loads(str(response.body_as_unicode()))
        product_ids_url = "https://mst.vip.com/special/getVisProductIds?&offset=0&sort=0&size_name=&_=1533695230121" \
                          "&brand_id=" + brand_id+"&warehouse="+warehouse
        categorys = category_json.get("result").get("data")

        for category in categorys:
            category_id = str(category.get("cat_id"))
            category_name = str(category.get("name"))
            get_pruduct_ids_url = product_ids_url+"&cat_id="+category_id
            # print("get_pruduct_ids_url=====>", get_pruduct_ids_url)
            request = scrapy.Request(get_pruduct_ids_url, callback=self.get_product_ids, dont_filter=True)
            request.meta['brand_id'] = brand_id
            request.meta['warehouse'] = warehouse
            request.meta['category_name'] = category_name
            print("====爬取类目[", category_name, "]的商品=====")
            yield request

    """获取商品ID集合"""
    def get_product_ids(self, response):
        brand_id = response.meta['brand_id']
        category_name = response.meta['category_name']
        warehouse = response.meta['warehouse']

        product_json = json.loads(str(response.body_as_unicode()))
        product_ids = product_json.get("data")
        get_pruducts_info_url = "https://mst.vip.com/special/getVisProductDataV2?client=pc&_=1533695230122" \
                                "&brand_id="+brand_id+"&warehouse="+warehouse+"&product_ids="

        ids = ''
        for index,product_id in enumerate(product_ids):
            ids = ids + product_id + "%2C"

            """由于请求接口里面参数数据太大的话超过get请求限制，这里拼接字段做了个限制"""
            if index % 25 == 0 and index != 0:
                # print("====发送了多次请求 count==", index)
                get_pruducts_data_json = get_pruducts_info_url+ids
                # print("get_pruducts_data_json====>", get_pruducts_data_json)
                request = scrapy.Request(get_pruducts_data_json, callback=self.get_content, dont_filter=True)
                request.meta['brand_id'] = brand_id
                request.meta['category_name'] = category_name
                ids = ''
                yield request

        get_products_data_json = get_pruducts_info_url + ids
        # print("get_products_data_json====>", get_products_data_json)
        request = scrapy.Request(get_products_data_json, callback=self.get_content, dont_filter=True)
        request.meta['category_name'] = category_name

        yield request

    """获取商品信息"""
    def get_content(self, response):
        vip_data = VipItem()
        category_name = response.meta['category_name']
        products_data_json = json.loads(str(response.body_as_unicode()))
        products_data = products_data_json.get("data")

        for product_data in products_data:
            vip_data['title'] = product_data.get("product_name")
            vip_data['link'] = product_data.get("brand_name")
            vip_data['price'] = product_data.get("vipshop_price")
            vip_data['comment'] = category_name
            # vip_data['vip_discount'] = product_data.get("vip_discount")
            # vip_data['market_price'] = product_data.get("market_price")
            yield vip_data




