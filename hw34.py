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
        print(response.json()['counters'])
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

    def get_headers(self):
        headers = {'Authorization': f'OAuth {self.token}'}
        return headers

    def get_visits(self):
        response = requests.get(f'{self.section}',
                                headers=self.get_headers(), params='metrics=ym:s:visits,ym:s:users')
        return response.json()

    def get_views(self):
        response = requests.get(f'{self.section}',
                                headers=self.get_headers())
        return response.json()

    def get_visitors(self):
        response = requests.get(f'{self.section}',
                                headers=self.get_headers())
        return response.json()


my_user = YaMetrikaManagement(TOKEN)
counter = my_user.counters[0]
print(counter)
