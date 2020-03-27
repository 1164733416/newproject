import requests
import json


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    form_date = {
        'i': ' 我爱中国',
        'from': ' AUTO',
        'to': ' AUTO',
        'smartresult': ' dict',
        'client': ' fanyideskweb',
        'salt': ' 15846838538107',
        'sign': ' b4f6d46d7883e2dbb18cd92cbaa411b7',
        'ts': ' 1584683853810',
        'bv': ' c3d953d5f079ad93810ed7b4b0f76df6',
        'doctype': ' json',
        'version': '2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }
    # 请求表单数据
    response = requests.post(url, data=payload)
    # 将JSON格式字符串转字典
    content = json.loads(response.text)
    # 打印翻译后的数据
    if __name__ == '__main__':
        get_translate_date('我爱数据')
