import requests


class HeFeng():
    def __init__(self):
        self.url='https://cdn.heweather.com/china-city-list.txt'

    def get_city_code(self):
        cities=self.get_city()
        for each in cities:
            yield each[2:13]

    def get_weather(self,city_code):
        url='https://free-api.heweather.net/s6/weather/now?location='+city_code+'&key=cc59af1df9aa4eec994be9eb2543df81'
        info=requests.get(url)
        info.encoding='utf8'
        print(info.text)


    def get_city(self):
        html = requests.get(self.url)
        html.encoding = 'utf8'
        # data=html.text
        cities=html.text.split('\n')
        return cities[6:]
        # print(cities)
        # for each in cities:
        #     print(each)


if __name__ == '__main__':
    hefeng=HeFeng()
    codes=hefeng.get_city_code()
    hefeng.get_weather(codes.__next__())

