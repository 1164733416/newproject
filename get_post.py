import random
import time
import requests
import json
import hashlib


def yield_headers():
    return {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1749741278@10.108.160.19; JSESSIONID=aaauT_-zYnOeR5k6WuYfx; OUTFOX_SEARCH_USER_ID_NCOO=322638183.72189075; ___rl__test__cookies=1586761009751',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 OPR/67.0.3575.53',
    }


class Youdao():
    def __init__(self, content):
        self.content = content
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_ts(self):
        t = time.time()
        return str(int(round(t * 1000)))

    def get_md5(self, value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = 'fanyideskweb' + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_salt(self):
        return self.ts + str(random.randint(0, 10))


    def yield_form_data(self):
        return {
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

    def yield_headers(self):
        return {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1749741278@10.108.160.19; JSESSIONID=aaauT_-zYnOeR5k6WuYfx; OUTFOX_SEARCH_USER_ID_NCOO=322638183.72189075; ___rl__test__cookies=1586761009751',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 OPR/67.0.3575.53',
        }

    def fanyi(self):
        response = requests.post(self.url,data=self.yield_form_data(),headers=self.yield_headers())
        content = json.loads(response.text)
        return content['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    while(True):
        t=input('please input :')
        youdao = Youdao(t)
        print("fanyi result : ",youdao.fanyi())

