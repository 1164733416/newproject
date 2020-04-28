import requests


class HeFeng():
    def __init__(self):
        self.url='https://cdn.heweather.com/china-city-list.txt'
        self.encoding='utf8'
        self.pre_requests='https://free-api.heweather.net/s6/weather/now?location='
        self.sub_requests='&key=cc59af1df9aa4eec994be9eb2543df81'

    def get_city_code(self):
        cities=self.get_city()
        for each in cities:
            yield each[2:13]

    def get_weather(self,city_code):
        url=self.pre_requests+city_code+self.sub_requests
        info=requests.get(url)
        info.encoding=self.encoding
        return info.json()

    def get_city(self):
        html = requests.get(self.url)
        html.encoding =self.encoding
        # data=html.text
        cities=html.text.split('\n')
        return cities[6:]
        # print(cities)
        # for each in cities:
        #     print(each)
    def today_weather(self,city_code):
        dic=self.get_weather(city_code)
        print(dic['HeWeather6'][0]['now'])

if __name__ == '__main__':
    hefeng=HeFeng()
    codes=hefeng.get_city_code()
    for each in range (10):
        hefeng.today_weather(codes.__next__())
