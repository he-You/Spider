

# -*- coding: utf-8 -*-

class transCookie:

    def __init__(self, cookie):
        self.cookie = cookie


    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}

        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value

        return itemDict

if __name__ == "__main__":
    cookie = "aliyungf_tc=AQAAAOlGWTqRmAAAiBq/PGH9PUOiL1M7; acw_tc=AQAAANaf5BmyqAAAiBq/PD71bidj43Wr; LATELY_SHOPID=1148601; pgv_pvi=1071216640; pgv_si=s61286400; u_asec=099%23KAFEGYEKEmEEhYTLEEEEEpEQz0yFD6DHDrsMQ6DTDXnIW6tcSryID60FDEFETcZdt9TXE7EFbOR5D3QTEEx6zIywjYFETrZtt3illuYTEHITmobEjUYOI8KNZIYvzaD4kLjBaaLN6wEW6oSq33Nny8gN1EGGP8TC01Tqiwhv0JmSoVbIXXg4kLNowDN7VNGrykxyZBut3aIQqFCccyEaRJfrsEFEpcZdt3illuZdsyaDMlllszJP%2F3mrlllr%2BuZdtkslluWRsyaDy%2FllsUPoE7EIsyaD4hAw3Q9rE7EhssaZtfiMAYFEPOKXD67ScblcL4wsDRMBFEt6iRnpbOiRwEz6uz8nPvS7wSZuDahWFEPc929ibwUq%2BvD3Uoxkq7d71Sss4LpA97A6CsJKHai3woDWuVuCcYUqaMh%2BCapCL7FsLOaicpiRE9suQ6Yyh3Qs1bW4VsonaGhucsnKbOMFCGFuVfpMvw%2F6wEZtC21AaGA3wpw0zwIT%2FLbqzloVb4dq1QlzZjcSL4MR%2BO%2FkPOK6CGhudz2SrMe6iGr8sapX"
    trans = transCookie(cookie)
    print(trans.stringToDict())