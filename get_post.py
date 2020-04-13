import random
import time
import requests


# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#  content = '我爱中国'


class Youdao():
    def __init__(self, content):
        self.content = content
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        print(ts)
        return ts

    # '1584683853810'

    def get_md5(self, value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    # def get_content(self):
    #     return content

    def get_sign(self):
        i = self.salt
        e = self.content
        s = 'fanyideskweb' + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # print('s=', s)
        return self.get_md5(s)
        # return 'b4f6d46d7883e2dbb18cd92cbaa411b7'

    def get_salt(self):
        s = str(random.randint(0, 10))
        t = self.ts
        # print('random = ',s)
        # print('ts=',t)
        # print('salt=',t+s)
        return t + s
        # '15846838538107'

    def yield_form_data(self):
        form_date = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'c3d953d5f079ad93810ed7b4b0f76df6',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_date

    def get_headers(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1749741278@10.108.160.19; JSESSIONID=aaauT_-zYnOeR5k6WuYfx; OUTFOX_SEARCH_USER_ID_NCOO=322638183.72189075; ___rl__test__cookies=1586761009751',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 OPR/67.0.3575.53',
        }
        return headers

    def headers_one(self):
        print(self.get_headers())

    def form_data_one(self):
        print(self.yield_form_data())

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ == '__main__':
    # print(form_date)
    # print(get_headers())
    youdao = Youdao('雪碧')
    print(youdao.fanyi())

