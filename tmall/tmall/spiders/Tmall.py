#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 下午5:10
# @Author  : Ju1is|落叶挽歌
# @Site    : https://github.com/vompom
# @Email   : 617669559@qq.com
# @File    : Vip.py
# @Software: PyCharm
# @Description: 爬取Tmall 美妆产品类 的数据

# -*- coding: utf-8 -*-
import string

import scrapy
import json
import re
from tmall.items import TmallItem
class Tmall(scrapy.Spider):
    name = 'tmall'
    allowed_domains = ['tmall']
    start_urls = ['https://list.tmall.com/ajax/allBrandShowForGaiBan.htm?t=0&q=%B9%D9%B7%BD%D6%B1%CA%DB&sort=s&style=w&vmarket=29890&active=1&theme=275&spm=875.7931836/B.category2016013.2.661442654HpfCC&smAreaId=330100&userIDNum=1663880338&tracknick=%C7%A7%CD%F2%C2%E4%D2%B6']
    cookie = {'cookie2': '2d4435c1553c26069c92a4f0f89205dc', '_med': 'dw:1366&dh:768&pw:1366&ph:768&ist:0', '_tb_token_': 'ea6da336a3e35', 'cna': 'upfQExfaLF0CAdpLG6g4pOa8', 'tt': 'login.tmall.com', 'skt': '37a30b6fc84b835d', 'csg': '4fd4e40d', 'cookie17': 'UoeyDbCx4mEAKQ%3D%3D', '_nk_': '%5Cu5343%5Cu4E07%5Cu843D%5Cu53F6', 'login': 'true', '_l_g_': 'Ug%3D%3D', 'res': 'scroll%3A990*5342-client%3A799*633-offset%3A799*5342-screen%3A1366*768', '_m_h5_tk': '03f2b5295b9b9f8cb8be367baa1a3b03_1533552350899', 'lgc': '%5Cu5343%5Cu4E07%5Cu843D%5Cu53F6', 'isg': 'BNXVA-9lInw7jAYxB8-w7vs55Ncjw6lHiyKpO1d6n8ybrvWgHyIrtOJgfPK9rqGc', 'tk_trace': '1', 'ck1': '', 'hng': 'CN%7Czh-CN%7CCNY%7C156', 'enc': 'wk0M5zwXkKMC0DMjX%2FTEGXjkhtsJY%2FqZZXaHvZnFkdQz%2BddupOK87a9YCWutoZz0zjpaQENtBYFj5EgOPH%2BFsw%3D%3D', 'uss': '', 'tracknick': '%5Cu5343%5Cu4E07%5Cu843D%5Cu53F6', 'lid': '%E5%8D%83%E4%B8%87%E8%90%BD%E5%8F%B6', 'pnm_cku822': '098%23E1hv6QvUvbpvUvCkvvvvvjiPPsMOQjlnRssW0jljPmPOQjY8PFF90jYjn2zvsj3EiQhvChCvCCptvpvhphvvvvyCvh1CZrwvI1OiHjaHQW97RAYVEvLvqbVQWlX9xKFE%2BFIlBAgRD764d56OVArlKbh6UxW2fEVxI2iI2B%2BKa4p7%2B3%2Brjo2ptE9SEct68fmxuphvmhCvCEZE3wkckphvCyEmmvQfeqyCvm3vpvpYMM%2FqhZCv2b9vvhb8phvZ7pvvp6nvpCBXvvCmu6CvHHyvvh8dvphvCyCCvvvvvvGCvvpvvPMM', 'cookie1': 'UUpjZ3FxkaNPP1XXOzisqCfc%2B66ly0WGpAX4oZLgwA8%3D', 'uc3': 'vt3', 'uc1': 'cookie16', 'cq': 'ccp%3D0', 'unb': '1663880338', 'dnk': '%5Cu5343%5Cu4E07%5Cu843D%5Cu53F6', '_m_h5_tk_enc': 'dfeb65a63d3b2a49091fe5724792df28', 't': '286a604bc1e4e75d99e6a2ebe212dd98'}

    def parse(self, response):
        sites = json.loads(response.body_as_unicode())

        ###测试数据
        # sites = '[{"href":"?brand=1411110865&amp;q=%B9%D9%B7%BD%D6%B1%CA%DB&amp;sort=s&amp;style=w&amp;vmarket=29890&amp;search_condition=23&amp;from=sn__brand&amp;active=1&amp;theme=275&amp;spm=875.7931836/B.category2016013.2.661442654HpfCC&amp;smAreaId=330100#J_crumbs","title":"wis","atpanel":"1,6037878,,,shop-brand-qp,4,brand-qp,","img":"TB1f_2nu1uSBuNjSsplXXbe8pXa"},{"href":"?brand=1439730891&amp;q=%B9%D9%B7%BD%D6%B1%CA%DB&amp;sort=s&amp;style=w&amp;vmarket=29890&amp;search_condition=23&amp;from=sn__brand&amp;active=1&amp;theme=275&amp;spm=875.7931836/B.category2016013.2.661442654HpfCC&amp;smAreaId=330100#J_crumbs","title":"One Leaf/一叶子","atpanel":"2,104506277,,,shop-brand-qp,4,brand-qp,","img":"TB1dZHLRXXXXXc8aXXXXXXXXXXX"}]'
        # sites = '[{"href":"?brand=1411110865&amp;q=%B9%D9%B7%BD%D6%B1%CA%DB&amp;sort=s&amp;style=w&amp;vmarket=29890&amp;search_condition=23&amp;from=sn__brand&amp;active=1&amp;theme=275&amp;spm=875.7931836/B.category2016013.2.661442654HpfCC&amp;smAreaId=330100#J_crumbs","title":"wis","atpanel":"1,6037878,,,shop-brand-qp,4,brand-qp,","img":"TB1f_2nu1uSBuNjSsplXXbe8pXa"}]'
        # sites = '[{"href":"?brand=6037878&q=%B9%D9%B7%BD%D6%B1%CA%DB&sort=s&style=w&vmarket=29890&search_condition=23&from=sn__brand-qp&active=1&theme=275&spm=875.7931836/B.category2016013.2.661442654HpfCC&smAreaId=330100#J_crumbs","title":"wis","atpanel":"1,6037878,,,shop-brand-qp,4,brand-qp,","img":"TB1f_2nu1uSBuNjSsplXXbe8pXa"},{"href":"?brand=1347966232&q=%B9%D9%B7%BD%D6%B1%CA%DB&sort=s&style=w&vmarket=29890&search_condition=23&from=sn__brand-qp&active=1&theme=275&spm=875.7931836/B.category2016013.2.661442654HpfCC&smAreaId=330100#J_crumbs","title":"SU:M37°/苏秘37°","atpanel":"19,1347966232,,,shop-brand-qp,4,brand-qp,","img":"TB1gkXDJVXXXXbWXXXXSutbFXXX.jpg"}]'
        # sites = json.loads(sites)

        ###遍历
        for site in sites:
            # 构建搜索url ->.replace('&amp;', '&')
            search_url = "https://list.tmall.com/search_product.htm" + str(site['href']).replace('&amp;', '&')
            yield scrapy.Request(search_url, callback=self.get_shop_url, dont_filter=True, cookies=self.cookie)

    """获取店铺URL"""
    def get_shop_url(self, response):
        print("=======获取店铺URL=======")
        shop_url = "https://list.tmall.com/"+response.xpath('//*[@id="J_ItemList"]/div/div[1]/div[1]/a/@href').extract_first()
        print("shop_url===>", shop_url)
        yield scrapy.Request(shop_url, callback=self.get_shop_categorys, dont_filter=True)

    """获取店铺内分类的数据"""
    def get_shop_categorys(self, response):
        print("=======获取店铺内分类的数据=======")
        title = response.xpath('/html/head/title').extract();
        categorys = response.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div/div[2]/ul/li/a');
        print("categorys==>", title)
        for category in categorys:
            category_name = category.xpath("text()").extract_first().strip()
            print(category_name)
            category_url = "https://list.tmall.com/search_shopitem.htm"+category.xpath("@href").extract_first()
            print("category_url===========>", category_url);
            request = scrapy.Request(category_url, callback=self.get_content, dont_filter=True)
            request.meta['category'] = category_name
            yield request

    """获取商品具体信息"""
    def get_content(self, response):
        tmall_data = TmallItem()
        print("=======获取商品的数据=======")
        product_list = response.xpath('//*[@class="product-iWrap"]')
        for product in product_list:
            tmall_data['category'] = response.meta['category']
            tmall_data['title'] = product.xpath('p[2]/a/@title').extract_first()
            tmall_data['price'] = re.findall(r"\d+\.?\d*", product.xpath('p[1]/em').extract_first())[0]
            comment_counts = product.xpath('p[3]/span[2]/a/text()').extract_first()

            if comment_counts.find("万")!=-1:
                comment_counts = comment_counts.replace("万","")
                comment_counts = int(float(comment_counts)*10000)

            tmall_data['comment_counts'] = comment_counts

            sale_counts = product.xpath('p[3]/span[1]/em/text()').extract_first()
            sale_counts = str(sale_counts).replace("笔", "")
            if sale_counts.find("万") != -1:
                sale_counts = sale_counts.replace("万", "")
                sale_counts = int(float(sale_counts) * 10000)

            tmall_data['sale_counts'] = sale_counts
            tmall_data['brand'] = product.xpath('div[2]/a/text()').extract_first().replace("旗舰店","").replace("官方","")
            # tmall_data['product_url'] = product.xpath('p[2]/a/@href').extract_first()

            yield tmall_data




