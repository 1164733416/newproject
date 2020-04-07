import requests
import time


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


def get_ts():
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
# '1584683853810'

def get_sign():
    return 'b4f6d46d7883e2dbb18cd92cbaa411b7'


def get_salt():
    s = str(random.randint(0, 10))
    t = get_ts()
    # print('random = ',s)
    # print('ts=',t)
    # print('salt=',t+s)
    return t + s
    # '15846838538107'

    form_date = {
        'i': ' 我爱中国',
        'from': ' AUTO',
        'to': ' AUTO',
        'smartresult': ' dict',
        'client': ' fanyideskweb',
        'salt': get_salt(),
        'sign': get_sign(),
        'ts': get_ts(),
        'bv': ' c3d953d5f079ad93810ed7b4b0f76df6',
        'doctype': ' json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    # 请求表单数据

    response = requests.post(url, data=payload)
    # 将JSON格式字符串转字典

    # 打印翻译后的数据
    if __name__ == '__main__':
        get_translate_date('我爱数据')
