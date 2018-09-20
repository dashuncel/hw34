import requests

TOKEN = 'AQAAAAAAfTi3AAU0U41oq-OZ60AZqlIgJdbWxis'

# класс работы с разделом менеджмент
class YaMetrikaManagement:
    def __init__(self, token):
        self.section = 'https://api-metrika.yandex.ru/management/v1'
        self.token = token

    def get_headers(self):
        headers = {'Authorization': f'OAuth {self.token}'
                  }
        return headers

    @property
    def counters(self):
        response = requests.get(f'{self.section}/counters',
                                headers=self.get_headers())
        return [c['id'] for c in response.json()['counters']]


    def get_counter_info(self, counter_id):
        response = requests.get(f'{self.section}/{counter_id}',
                                headers=self.get_headers())
        return response.json()

    def get_user_counters(self):
        response = requests.get(f'{self.section}/counters',
                                headers=self.get_headers())
        return response.json()

# класс работы с разделом статистики
class YaMetrikaStatistica:

    def __init__(self, token, counter):
        self.token = token
        self.counter = counter
        self.section = 'https://api-metrika.yandex.ru/stat/v1/data'
        self.__visits = 'ym:s:visits'
        self.__pageviews = 'ym:s:pageviews'
        self.__users = 'ym:s:users'

    def get_headers(self):
        headers = {'Authorization': f'OAuth {self.token}'}
        return headers

    def get_params(self):
        params = {'direct_client_logins': 'korovkinada',
                  'ids': self.counter,
                  'metrics': 'ym:s:visits,ym:s:pageviews,ym:s:users'
                 }
        return params

    @property
    def data(self):
        response = requests.get(f'{self.section}',
                                headers=self.get_headers(),
                                params=self.get_params())
        return response.json()

    def get_visits(self):
        return self.data['data'][0]['metrics'][0]

    def get_pageviews(self):
        return self.data['data'][0]['metrics'][1]

    def get_users(self):
        return self.data['data'][0]['metrics'][2]


my_user = YaMetrikaManagement(TOKEN)
counters = my_user.counters
my_stat = YaMetrikaStatistica(TOKEN, counters[0])
print('Количество визитов:', my_stat.get_visits())
print('Количество просмотров:', my_stat.get_pageviews())
print('Количество пользователей:', my_stat.get_users())

